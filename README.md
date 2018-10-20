[![Maintainability](https://api.codeclimate.com/v1/badges/d660a69253618dfb3ce9/maintainability)](https://codeclimate.com/github/sylviawanjiku/Store_manager_Api/maintainability)
[![Build Status](https://travis-ci.org/sylviawanjiku/Store_manager_Api.svg?branch=ch-test-user-endpoints-161360489)](https://travis-ci.org/sylviawanjiku/Store_manager_Api)

# StoreManager

Store Manager is an app that allows users to control sales and inventory.
The store manager app has two type of users store attendant and store owner(admin).
Each of the two users have their indivindual roles to play but in this case what the store attendant can do the admin can also do.

### The store attendant can perform the following:

1. Login to the app
2. View all products 
3. View a single product
4. Make a sale 
5. View a personal sales record

### The store owner can perform the following:

1. Login to the app
2. register a new user
3. add a product to inventory
4. view sales record
5. view a specific sales record with respect to te user who made the sale

### Running the application
1. clone this repository
2. navigate to the project directory
3. Activate the virtual environment $ source .env
4. Install dependencies needed for the project to run $ pip install -r requirements.txt
5. install flask $ pip install flask
6. Run the application $ FLASK_APP=run.py flask run
7. To test the test $ pytest

### The API Endpoints
1. post-register user   http://127.0.0.1:5000/api/v1/users   
2. post-login user  http://127.0.0.1:5000/api/v1/login   
3. post-create products     http://127.0.0.1:5000/api/v1/products   
4. post-create sale record  http://127.0.0.1:5000/api/v1/sales 
5. get-fetch products   http://127.0.0.1:5000/api/v1/products
6. get-fetch single product     http://127.0.0.1:5000/api/v1/products/product_id
6. get-fetch sale records   http://127.0.0.1:5000/api/v1/sales
6. get-fetch single sale record     http://127.0.0.1:5000/api/v1/sales/sale_id
7. get-fetch user   http://127.0.0.1:5000/api/v1/users 
7. get-fetch single user    http://127.0.0.1:5000/api/v1/users/user_id

### Testing the app

The endpoints above can be tested using Postman.

The tests have been automated through continousintergration in TravisCI
### Hosting the app
The app has been hosted on Heroku
https://andstore.herokuapp.com/
