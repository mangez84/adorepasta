# Adore Pasta

![Adore Pasta](static/images/adorepasta.png)

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
        - [Colours](#colours)
        - [Fonts](#fonts)
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
5. [Test](#test)
    - [Validation Services](TEST.md#validation-services)
        - [W3C Markup Validation Service](TEST.md#w3c-markup-validation-service)
        - [W3C CSS Validation Service](TEST.md#w3c-css-validation-service)
        - [JSHint](TEST.md#jshint)
        - [PEP8 Online](TEST.md#pep8-online)
    - [Testing User Stories](TEST.md#testing-user-stories)
        - [Common Users](TEST.md#common-users)
        - [Unregistered Users](TEST.md#unregistered-users)
        - [Registered Users](TEST.md#registered-users)
        - [Administrator Users](TEST.md#administrator-users)
    - [Further Testing](TEST.md#further-testing)
    - [Known Bugs](TEST.md#known-bugs)
        - [Unfixed](TEST.md#unfixed)
6. [Deployment](#deployment)
7. [Credits](#credits)
    - [Code](#code)
    - [Content](#content)
    - [Media](#media)
        - [Images](#images)
    - [Acknowledgements](#acknowledgements)

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

#### Colours

- The colors on the website are inspired by the Italian flag. The Italian theme fits well as the website is about pasta dishes.

#### Fonts

- The Sacramento font is used for the site logo in the upper left corner. The font is cursive and is meant to give a welcoming feeling when you enter the website.
- The Nunito font is used for navigation links, headings, buttons and text content. The font is easy to read and gives a playful impression.

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

    ![View Recipes](static/images/recipes.png)

- Users can search for recipes without being logged in.

    ![Search Recipes](static/images/search.png)

- Users can register an account and log in.

    ![Register](static/images/register.png)
    ![Log In](static/images/login.png)

- Links for logging in and out are clearly visible on the website.

    ![Navbar Log In](static/images/navbar-login.png)
    ![Navbar Register](static/images/navbar-logout.png)

- Registered users have access to a page where their own recipes are displayed.

    ![My Recipes](static/images/my-recipes.png)

- A registered user can add, edit and delete their own recipes.

    ![My Recipes CRUD](static/images/my-recipes-crud.png)
    ![My Recipes Add](static/images/my-recipes-add.png)
    ![My Recipes Edit](static/images/my-recipes-edit.png)

- A confirmation from the user is required to delete a recipe.

    ![My Recipes Delete Confirm](static/images/my-recipes-del-confirm.png)

- Statistics about the recipes are displayed on the home page when a user is logged in.

    ![Statistics](static/images/statistics.png)

- An administrator user can delete recipes created by other users.

    ![Admin Edit Delete](static/images/admin-edit-delete.png)

- The website is easy to use, nice to look at and works well on many device types.

    ![Responsive](static/images/responsive.png)

### Upcoming Features

- Statistics on the most common ingredient in the database will be added in a later release.
- A dialog box to confirm logout will be added in a later release.

## Technologies Used

### Languages Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/CSS)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks, Libraries and Software Used

- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
    - The website has been created using the Flask micro-framework with dependent libraries.
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

## Test

- Tests performed are documented in [TEST.md](TEST.md).

## Deployment

### Heroku

Adore Pasta was deployed to Heroku using the following procedure.

- Log into [Heroku](https://www.heroku.com/) and click on the **New** button and choose **Create new app**.
- Choose a name and region for the app and click **Create app**.
- Create a file with a list of dependencies that must be installed for the application to run properly:
    ```
    pip3 freeze --local > requirements.txt
    ```
- Create a file named Procfile with the following content:
    ```
    web: python app.py
    ```
- In Heroku click on **Settings** and then **Reveal Config Vars**.
- Add names and values for environment variables.
    - Required environment variables:
    ```
    IP
    MONGO_DBNAME
    MONGO_URI
    PORT
    SECRET_KEY
    ```
- Click on **Deploy** in the navigation bar. Choose [Github](https://github.com/) next to **Deployment method**.
- Next to **Connect to GitHub** search for your [repository](https://github.com/mangez84/adorepasta) and click **Connect**.
- In the **Automatic deploys** section choose a branch and click on **Enable Automatic Deploys**.
- In a little while, the [application](http://adorepasta.herokuapp.com/) will be available on Heroku.

### Fork the GitHub Repository

To make a **fork** of this repository to your own account use the following procedure.

- Log into your [GitHub](https://github.com/) account and browse to [this repository](https://github.com/mangez84/adorepasta).
- Locate the **Fork** button in the upper right corner and click it.
- You should now have a copy of the repository in your own account.

### Clone the GitHub Repository

To make a **clone** of this repository use the following procedure.

- Log into your [GitHub](https://github.com/) account and browse to the [repository](https://github.com/mangez84/adorepasta).
- Locate the **Code** button and click it.
- Choose **Download ZIP** from the dropdown menu to download the project as a compressed file or copy the **HTTPS** link.
- If you copied the HTTPS link open a terminal with access to [`git`](https://git-scm.com/).
- Navigate to or create a desired working directory for the project.
- Type **git clone** followed by the HTTPS link you copied.

    ```
    git clone https://github.com/mangez84/adorepasta
    ```

- Press Enter and a local clone will be created in your current working directory.

### Run the Application Locally

After cloning the repository use the following procedure to run the application locally.

- Change directory to adorepasta

    ```
    cd adorepasta
    ```

- Use pip to install dependencies.

    ```
    pip install -r requirements.txt
    ```

- Create a file named env.py and configure environment variables.
    - Required environment variables:

    ```
    IP
    MONGO_DBNAME
    MONGO_URI
    PORT
    SECRET_KEY
    ```

- Run the application.

    ```
    python app.py
    ```

## Credits

### Code

- The registration and login functionality is highly inspired by the Flask mini project developed by Tim Nelson at [Code Institute](https://codeinstitute.net/).
- A useful tip about the Jinja loop.index variable was found in this [Stack Overflow](https://stackoverflow.com/questions/7537439/how-to-increment-a-variable-on-a-for-loop-in-jinja-template/7537466#7537466) post.

### Content

- The description for the spaghetti bolognese recipe was copied from [from Wikipedia](https://en.wikipedia.org/wiki/Bolognese_sauce).
- The description for the spaghetti carbonara recipe was copied from [from Wikipedia](https://en.wikipedia.org/wiki/Carbonara).
- The spaghetti bolognese recipe was copied from [BBC Food](https://www.bbc.co.uk/food/recipes/easy_spaghetti_bolognese_93639).
- The spaghetti carbonara recipe was copied from [Jamie Oliver's](https://www.jamieoliver.com/recipes/pasta-recipes/easy-carbonara/) website.
- The garlic shrimp pasta recipe was copied from [tasty.co](https://tasty.co/recipe/one-pot-lemon-garlic-shrimp-pasta).
- The pesto pasta recipe was copied from [BBC goodfood](https://www.bbcgoodfood.com/recipes/easy-pesto-pasta).
- The tomato spaghetti recipe was copied from [Jamie Oliver's](https://www.jamieoliver.com/recipes/pasta-recipes/classic-tomato-spaghetti/) website.
- The lasagne recipe was copied from [BBC goodfood](https://www.bbcgoodfood.com/recipes/classic-lasagne-0).

### Media

#### Images

- The image for the spaghetti bolognese recipe was obtained from [RitaE on Pixabay](https://pixabay.com/photos/spaghetti-noodles-bolognese-1987454/).
- The image for the spaghetti carbonara recipe was obtained from [Hans Braxmeier on Pixabay](https://pixabay.com/photos/spaghetti-spaghetti-carbonara-7113/).
- The image for the garlic shrimp pasta recipe was obtained from [RitaE on Pixabay](https://pixabay.com/photos/pasta-italian-cuisine-dish-3547078/).
- The image for the pesto pasta recipe was obtained from [Pexels on Pixabay](https://pixabay.com/photos/pasta-pesto-farfalle-pesto-pasta-1854245/).
- The image for the tomato spaghetti recipe was obtained from [RitaE on Pixabay](https://pixabay.com/photos/spaghetti-tomatoes-tomato-sauce-1392266/).
- The image for the lasagne recipe was obtained from [RitaE on Pixabay](https://pixabay.com/photos/lasagna-cheese-tomatoes-noodles-1900529/).

### Acknowledgements

- My Code Institute mentor Gerard McBride for valuable tips and feedback.