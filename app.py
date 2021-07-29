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


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        register = {
            "firstname": request.form.get("firstname").lower(),
            "lastname": request.form.get("lastname").lower(),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(
                request.form.get("password"), "pbkdf2:sha256", salt_length=16
            ),
            "admin": False
        }
        account = mongo.db.users.find_one({"email": register["email"]})

        # Ensure that unique accounts are stored in the database
        if account:
            flash(f"{register['email']} is already a registered account.")
            flash("Please register with another email address.")
            return redirect(url_for("register"))

        mongo.db.users.insert_one(register)
        flash(f"Thank you, {register['firstname'].capitalize()}!")
        flash("To log in use your email address and password.")
        flash("Welcome!")
        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        login = {
            "email": request.form.get("email").lower(),
            "password": request.form.get("password")
        }
        account = mongo.db.users.find_one({"email": login["email"]})

        # Check password for existing account
        if account:
            if check_password_hash(account["password"], login["password"]):
                welcome = (
                    f"Welcome, {account['firstname'].capitalize()} "
                    f"{account['lastname'].capitalize()}!"
                )
                flash(welcome)
                return redirect(url_for("myrecipes"))

    return render_template("login.html")


@app.route("/myrecipes")
def myrecipes():
    return render_template("myrecipes.html")


@app.route("/recipes")
def recipes():
    return render_template("recipes.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
