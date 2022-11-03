# Something Borrowed (backend)

Something Borrowed is an iOS app that invites users to buy and sell gently used wedding attire. This app was created by Tiffini Hyatt as an Ada Developers Academy capstone project.

[Capstone Presentation](https://vimeo.com/754350452/9f75a4b668)

[Front End Repository](https://github.com/tiffinihyatt/front-end-something-borrowed)

<img width="260" alt="A white app launch screen with 'something borrowed' and an image of two interlocked wedding bands at the center." src="https://user-images.githubusercontent.com/95541002/199756017-3f187a9c-14c4-4d7b-9f02-f74f6563a739.png"><img width="261" alt="An app landing page with the text 'something borrowed - once loved wedding attire for the modern nearlywed' centered in a teal semi-circle. Below, text reads 'Welcome! Please select an option below' and points to four choices: 'home'; 'browse'; 'list an item'; and 'bag'." src="https://user-images.githubusercontent.com/95541002/199756088-c081192a-aa21-49bf-bc0a-f5ecc8841152.png">


## Application Features

### Create New Listing

Users can access photos from their camera roll to list a new item for sale. Listed items are posted to the app's database and appear in the application's "Browse" view.

<img width="261" alt="A screenshot from the 'Something Borrowed' iOS app with 'List an Item' as a heading and several empty fields for user input" src="https://user-images.githubusercontent.com/95541002/199757541-fd1eda5d-5115-42c4-9db1-0efc67845858.png"><img width="261" alt="sb - cue the confetti" src="https://user-images.githubusercontent.com/95541002/199757746-6a979bf1-8944-4c2f-ae89-683a97fe997b.png">


### Browse + Add to Cart

Users can also view listing details and add items to their shopping cart. Adding an item to one's shopping cart toggles the item's availability and removes that item from the "Browse" view. When a user removes an item from their cart, the availability is toggled again and the item becomes visible in the "Browse" view.

<img width="261" alt="sb - browse view" src="https://user-images.githubusercontent.com/95541002/199757803-b2e210c9-c97f-4d7a-af02-d3f3ac9f2914.png"><img width="261" alt="sb - detailed listing view" src="https://user-images.githubusercontent.com/95541002/199759592-5fa801fe-7959-430e-88ed-cd69ebf9bf47.png"><img width="262" alt="sb - shopping cart" src="https://user-images.githubusercontent.com/95541002/199759970-2027a9c8-2626-4ddf-be0d-8e12310f3aa4.png">


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
