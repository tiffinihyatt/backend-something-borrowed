# Something Borrowed (backend)

Something Borrowed is an iOS app that invites users to buy and sell gently used wedding attire. This app was created by Tiffini Hyatt as an Ada Developers Academy capstone project.

[Capstone Presentation](https://vimeo.com/754350452/9f75a4b668)

## Application Features

### Create New Listing

Users can access photos from their camera roll to list a new item for sale. Listed items are posted to the app's database and appear in the application's "Browse" view.

### Add to Cart

Users can also view listing details and add items to their shopping cart. Adding an item to one's shopping cart toggles the item's availability and removes that item from the "Browse" view. When a user removes an item from their cart, the availability is toggled again and the item becomes visible in the "Browse" view.

## Setup

After forking this repository, clone it into your desired local directory.

### Install Dependencies

Inside of your local project directory, create your virtual environment:

    $ python3 -m venv venv
    $ source venv/bin/activate

Next, install project dependencies:

    (venv) $ pip install -r requirements.txt

### Create Database

Create a database to store your backend data (you can choose any name you'd like).

Create a `.env` file.

Inside of `.env`, add this environment variable: `FLASK_ENV=development`

Also inside of `.env`, add a second environment variable: `SQLALCHEMY_DATABASE_URI`. Set this variable's value equal to the path to your development database.

Before attempting to run your backend, be sure to initialize your database by running `flask db init`.
