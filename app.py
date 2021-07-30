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


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/recipes")
def recipes():
    return render_template("recipes.html")


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
            return render_template("my_recipes.html", username=username)
    except KeyError:
        return redirect(url_for("login"))
    else:
        return redirect(url_for("home"))


@app.route("/my_recipes/<username>/add_recipe")
def add_recipe(username):
    # Check if session cookie is valid otherwise redirect to home
    try:
        if username == session["username"]:
            return render_template("add_recipe.html", username=username)
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
