# Adore Pasta

[Adore Pasta](https://adorepasta.herokuapp.com/) is a platform for pasta lovers to find and share delicious pasta recipes.

[Create an account](https://adorepasta.herokuapp.com/register), log in and share your pasta knowledge with the world!

## Table of Contents

1. [UX](#ux)
    - [User Stories](#user-stories)
        - [Common User Goals](#common-user-goals)
        - [Unregistered User Goals](#unregistered-user-goals)
        - [Registered User Goals](#registered-user-goals)
        - [Administrator User Goals](#administrator-user-goals)
    - [Developer And Business Goals](#developer-and-business-goals)
    - [Design](#design)
    - [Wireframes](#wireframes)
2. [Features](#features)
    - [Existing Features](#existing-features)
    - [Upcoming Features](#upcoming-features)
3. [Technologies Used](#technologies-used)
    - [Languages Used](#languages-used)
    - [Frameworks, Libraries and Software Used](#frameworks-libraries-and-software-used)
4. [Data Model](#data-model)
    - [Collections](#collections)
    - [Indexes](#indexes)
5. [Credits](#credits)
    - [Code](#code)
    - [Content](#content)
    - [Media](#media)
        - [Images](#images)

## UX

### User Stories

#### Common User Goals

- As a user, I want the opportunity to see all existing recipes.
- As a user, I want to be able to search for recipes.

#### Unregistered User Goals

- As an unregistered user, I want to be able to register an account and log in.

#### Registered User Goals

- As a registered user, I want to be able to add my own recipes.
- As a registered user, I want to be able to update my own recipes.
- As a registered user, I want to be able to delete my own recipes.
- As a registered user, I want a profile page that only shows my own recipes.
- As a registered user, I want to see statistics on the number of recipes in the database.
- As a registered user, I want to see statistics on the most common ingredient in the database.
- As a registered user, I want to see statistics on how many registered users there are.
- As a registered user, I want to be able to log out.

#### Administrator User Goals

- As an administrator user, I want to be able to edit and delete recipes that were not created by myself.

### Developer And Business Goals

- Improve my programming skills in the Python language.
- Write good code that follows the DRY principle.
- Learn more about MongoDB and document databases.
- Create an easy-to-use website for those who share an interest in Italian food.

### Design

### Wireframes

- [Home](static/wireframes/home.pdf)
- [Register](static/wireframes/register.pdf)
- [Log In](static/wireframes/login.pdf)
- [Recipes](static/wireframes/recipes.pdf)
- [Recipe Details](static/wireframes/recipe-details.pdf)
- [My Recipes](static/wireframes/myrecipes.pdf)
- [My Recipes Add/Edit](static/wireframes/myrecipes-add-edit.pdf)
- [My Recipes Delete](static/wireframes/myrecipes-delete.pdf)
- [Log Out](static/wireframes/logout.pdf)

## Features

### Existing Features

- Users can view all recipes without being logged in.
- Users can search for recipes without being logged in.
- Users can register an account and log in.
- Links for logging in and out are clearly visible on the website.
- Registered users have access to a page where their own recipes are displayed.
- A registered user can add, edit and delete their own recipes.
- A confirmation from the user is required to delete a recipe.
- Statistics about the recipes are displayed on the home page when a user is logged in.
- An administrator user can delete recipes created by other users.
- The website is easy to use, nice to look at and works well on many device types.

### Upcoming Features

- None at the moment.

## Technologies Used

### Languages Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/CSS)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks, Libraries and Software Used

- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
    - The website has been created using the Flask microframework with dependent libraries.
    - Dependent libraries include [Jinja](https://jinja.palletsprojects.com/en/3.0.x/) and [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/).
- [MongoDB](https://www.mongodb.com/)
    - Recipes and registered users are stored in a MongoDB document database.
- [Flask-PyMongo](https://flask-pymongo.readthedocs.io/en/latest/)
    - The Flask-PyMongo library is used to interact with the MongoDB document database.
- [Bootstrap 5.0.2](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
    - The Bootstrap 5.0.2 framework is widely used in this project.
    - Code for the grid system, navigation bar, forms and cards have been copied and later modified to suit this project.
- [jQuery 3.6.0](https://jquery.com/)
    - jQuery is used for the interactive parts when adding, editing or deleting recipes.
- [Git](https://git-scm.com/)
    - Git is used for version control of the code in the project.
- [Github](https://github.com/)
    - The files for this project are stored in GitHub.
- [Gitpod](https://gitpod.io/)
    - Gitpod has been used as a development environment for this project.
- [Heroku](https://www.heroku.com/)
    - The production version of the website is hosted on Heroku.
- [Balsamiq](https://balsamiq.com/)
    - Balsamiq was used to create wireframes for this project.
- [Google Fonts](https://fonts.google.com/)
    - The fonts used on the website are imported from Google Fonts.
- [Font Awesome](https://fontawesome.com/)
    - Icons from Font Awesome can be seen when you add or remove ingredients and steps.
- [favicon.io](https://favicon.io/)
    - The favicon used on the website was obtained from [favicon.io](https://favicon.io/).
- [Chrome DevTools](https://developer.chrome.com/docs/devtools/)
    - Chrome DevTools was used extensively during the development of the website.

## Data Model

- The website uses a [MongoDB](https://www.mongodb.com/) document database with two collections to store recipes and registered users.
- The `username` field from the `users` collection is stored in a session cookie after a successful login. When a recipe is added, the `username` is stored in the `creator` field in the `recipes` collection.
- Users who have the `admin` field set to true have the right to edit and delete all recipes on the site.
- The value from the `creator` field is used in a function that queries the users collection to get user details.
- The `ingredient` field contains an object for each ingredient added by the user.
- The `method` field contains an item for each step required to prepare the recipe.

### Collections

- adorePastaDB.recipes

    ```json
    {
        "_id": {
            "$oid": "***"
        },
        "name": "Spaghetti Bolognese",
        "description": "Bolognese sauce is a meat-based sauce in Italian cuisine.",
        "image": "https://i.imgur.com/image.jpg",
        "type": "Dinner",
        "time": "30",
        "serves": "4",
        "creator": "foody",
        "ingredients": {
            "ingredient-1": {
                "name": "Spaghetti",
                "quantity": "500",
                "unit": "g"
            },
            "ingredient-2": {
                "name": "Onions",
                "quantity": "2",
                "unit": ""
            }
        },
        "method": {
            "method-1": "Boil water.",
            "method-2": "Cook pasta.",
            "method-3": "Slice onions."
        }
    }
    ```

- adorePastaDB.users

    ```json
    {
        "_id": {
            "$oid": "***"
        },
        "firstname": "foody",
        "lastname": "harrelson",
        "username": "foody",
        "email": "foody@adorepasta.com",
        "password": "***",
        "admin": false
    }
    ```

### Indexes

- A [wildcard text index](https://docs.mongodb.com/manual/core/index-text/#wildcard-text-indexes) has been created in the recipes collection to support the search function on the website.

## Credits

### Code

- The registration and login functionality is highly inspired by the Flask mini project developed by Tim Nelson at [Code Institute](https://codeinstitute.net/).
- A useful tip about the Jinja loop.index variable was found in this [Stack Overflow](https://stackoverflow.com/questions/7537439/how-to-increment-a-variable-on-a-for-loop-in-jinja-template/7537466#7537466) post.

### Content

- The description for the spaghetti bolognese recipe was copied from [from Wikipedia](https://en.wikipedia.org/wiki/Bolognese_sauce).
- The description for the spaghetti carbonara recipe was copied from [from Wikipedia](https://en.wikipedia.org/wiki/Carbonara).
- The recipes are otherwise created by the developer himself.

### Media

#### Images

- The image for the spaghetti bolognese recipe was obtained from [RitaE on Pixabay](https://pixabay.com/photos/spaghetti-noodles-bolognese-1987454/).
- The image for the spaghetti carbonara recipe was obtained from [Hans Braxmeier on Pixabay](https://pixabay.com/photos/spaghetti-spaghetti-carbonara-7113/).
- The image for the spaghetti with shrimps recipe was obtained from [RitaE on Pixabay](https://pixabay.com/photos/pasta-italian-cuisine-dish-3547078/).
- The image for the farfalle with pesto recipe was obtained from [Pexels on Pixabay](https://pixabay.com/photos/pasta-pesto-farfalle-pesto-pasta-1854245/).
- The image for the spaghetti with tomato sauce recipe was obtained from [RitaE on Pixabay](https://pixabay.com/photos/spaghetti-tomatoes-tomato-sauce-1392266/).
- The image for the lasagna recipe was obtained from [RitaE on Pixabay](https://pixabay.com/photos/lasagna-cheese-tomatoes-noodles-1900529/).