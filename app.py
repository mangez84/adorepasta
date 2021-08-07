import os
from flask import (
    Flask, flash, render_template, redirect,
    request, session, url_for
)
from werkzeug.security import (
    generate_password_hash, check_password_hash
)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


def get_ingredients(form):
    ingredients = {}
    num_ingredients = 0
    # Check how many ingredients there are in the recipe
    for key in form.to_dict():
        if key.startswith("ingredient"):
            num_ingredients += 1
    # Build a dictionary for ingredients
    for i in range(1, num_ingredients + 1):
        ingredient = "ingredient-" + str(i)
        quantity = "quantity-" + str(i)
        unit = "unit-" + str(i)
        ingredients.update({ingredient: {
            "name": form.get(ingredient),
            "quantity": form.get(quantity),
            "unit": form.get(unit)}})
    return ingredients


def get_method(form):
    method = {}
    num_steps = 0
    # Check how many steps there are in the recipe
    for key in form.to_dict():
        if key.startswith("method"):
            num_steps += 1
    # Build a dictionary for the steps
    for i in range(1, num_steps + 1):
        step = "method-" + str(i)
        method.update({step: form.get(step)})
    return method


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/recipes")
def recipes():
    recipes = list(mongo.db.recipes.find())
    for recipe in recipes:
        creator = mongo.db.users.find_one({"username": recipe["creator"]})
        userdata = {
            "firstname": creator["firstname"],
            "lastname": creator["lastname"]
        }
        recipe.update(userdata)
    return render_template("recipes.html", recipes=recipes)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        register = {
            "firstname": request.form.get("firstname").lower(),
            "lastname": request.form.get("lastname").lower(),
            "username": request.form.get("username").lower(),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(
                request.form.get("password"), "pbkdf2:sha256", salt_length=16
            ),
            "admin": False
        }
        account = mongo.db.users.find_one({"username": register["username"]})

        # Ensure that unique accounts are stored in the database
        if account:
            flash(
                f"The username {register['username']} is already registered."
            )
            flash("Please register with another username.")
            return redirect(url_for("register"))

        mongo.db.users.insert_one(register)
        flash(f"Thank you, {register['firstname'].capitalize()}!")
        flash("Log in with your username and password.")
        flash("Welcome!")
        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        login = {
            "username": request.form.get("username").lower(),
            "password": request.form.get("password")
        }
        account = mongo.db.users.find_one({"username": login["username"]})
        error = "The username or password is incorrect. Please try again."

        # Check password for existing account
        if account:
            if check_password_hash(account["password"], login["password"]):
                session["username"] = login["username"]
                flash(
                    f"Welcome, {account['firstname'].capitalize()} "
                    f"{account['lastname'].capitalize()}!"
                )
                return redirect(
                    url_for("my_recipes", username=session["username"])
                )
            else:
                flash(error)
                return redirect(url_for("login"))
        else:
            flash(error)
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/my_recipes/<username>")
def my_recipes(username):
    # Check if session cookie is valid otherwise redirect to home
    try:
        if username == session["username"]:
            recipes = list(mongo.db.recipes.find({"creator": username}))
            userdata = mongo.db.users.find_one({"username": username})
            return render_template(
                "my_recipes.html", username=username, recipes=recipes,
                userdata=userdata
            )
    except KeyError:
        return redirect(url_for("login"))
    else:
        return redirect(url_for("home"))


@app.route("/my_recipes/<username>/add_recipe", methods=["GET", "POST"])
def add_recipe(username):
    if request.method == "POST":
        if username == session["username"]:
            recipe = {
                "name": request.form.get("name"),
                "description": request.form.get("description"),
                "image": request.form.get("image"),
                "type": request.form.get("type"),
                "time": request.form.get("time"),
                "serves": request.form.get("serves"),
                "creator": username
            }
            ingredients = get_ingredients(request.form)
            method = get_method(request.form)
            recipe.update({"ingredients": ingredients})
            recipe.update({"method": method})
            mongo.db.recipes.insert_one(recipe)
            flash("The recipe was successfully created!")
            return redirect(url_for("my_recipes", username=username))
    # Check if session cookie is valid otherwise redirect to home
    try:
        if username == session["username"]:
            return render_template("add_recipe.html", username=username)
    except KeyError:
        return redirect(url_for("login"))
    else:
        return redirect(url_for("home"))


@app.route(
    "/my_recipes/<username>/edit_recipe/<recipe_id>", methods=["GET", "POST"]
)
def edit_recipe(username, recipe_id):
    if request.method == "POST":
        if username == session["username"]:
            recipe_update = {
                "name": request.form.get("name"),
                "description": request.form.get("description"),
                "image": request.form.get("image"),
                "type": request.form.get("type"),
                "time": request.form.get("time"),
                "serves": request.form.get("serves"),
                "creator": username
            }
            ingredients = get_ingredients(request.form)
            method = get_method(request.form)
            recipe_update.update({"ingredients": ingredients})
            recipe_update.update({"method": method})
            mongo.db.recipes.update_one(
                {"_id": ObjectId(recipe_id)}, {"$set": recipe_update}
            )
            flash("The recipe was successfully updated!")
            return redirect(url_for("my_recipes", username=username))
    try:
        if username == session["username"]:
            recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
            return render_template(
                "edit_recipe.html", username=username, recipe=recipe
            )
    except KeyError:
        return redirect(url_for("login"))
    else:
        return redirect(url_for("home"))


@app.route(
    "/my_recipes/<username>/delete_recipe/<recipe_id>", methods=["GET", "POST"]
)
def delete_recipe(username, recipe_id):
    if request.method == "POST":
        if username == session["username"]:
            mongo.db.recipes.delete_one({"_id": ObjectId(recipe_id)})
            flash("The recipe was successfully deleted!")
            return redirect(url_for("my_recipes", username=username))
    try:
        if username == session["username"]:
            return redirect(url_for("my_recipes", username=username))
    except KeyError:
        return redirect(url_for("login"))
    else:
        return redirect(url_for("home"))


@app.route("/logout")
def logout():
    flash("You have been logged out successfully!")
    session.pop("username")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
