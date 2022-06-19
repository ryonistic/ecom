# ecom

A sample ecommerce website with payment integration

[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: MIT

## Settings

Moved to [settings](https://github.com/ryonistic/ecom/tree/main/ecom/config/settings).

To get started, clone the repository and add a file called .env in the folder where the manage.py file is.
This .env file will contain the following information:-

STRIPE_PUBLIC_KEY = "Whatever your public stripe key is, you need to setup stripe payments, there are many tutorials for that"
STRIPE_SECRET_KEY = "This will be the secret key for stripe, also available in your stripe account"

DJANGO_SECRET_KEY = "Whatever secret key you may want to use. Make it complicated."

This is a sample database name, you may create a database in your PC using this command:- 

        $ createdb --username=postgres ecommerce

LOCAL_DATABASE_NAME = "ecommerce"
LOCAL_DATABASE_PASSWORD = "password321"

## Showcase
[![Django eCommerce website](https://github.com/ryonistic/ecom/blob/main/ecom/showcase/home.png?raw=true)](https://youtu.be/eGP8SJQ3nOs "Django eCommerce website with stripe integration Portfolio project")

Click on the above image to go to the portfolio video youtube link

More from [showcase](https://github.com/ryonistic/ecom/tree/main/ecom/showcase).

## Basic Commands

### Setting Up Your Users

-   To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

-   To create a **superuser account**, use this command:

        $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy ecom

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html#sass-compilation-live-reloading).
