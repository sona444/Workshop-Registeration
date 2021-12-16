# Workshop-Registeration
- A flask app for a photography workshop registeration. 
- Made in Python flask framework.

## Setup (Using VS Code Terminal)
- Clone this repository
- Setup a virtual environment by using the command "<b>python3 -m venv 'Environment-name'</b>".
- Step into that environment by using "<b>source venv(Environment name in my case)/bin/activate</b>".
- Install all the required packages by using "<b>pip3 install requirements.txt".
- <b>Setup the Database(PostgreSQL)</b> by following these commands:
- sudo apt update
- sudo apt install postgresql postgresql-contrib
- After installation run "psql".
- Then login as your desired user.
- Create your database by using "CREATE database workshop(In my case);"
- Then run migrations by using following commands:
- flask db init
- flask db migrate
- flask db upgrade
- Now you are all set to run the application

## How to run
- It's simple. Just run the command "flask run".
- Now you can access the application at localhost "http://127.0.0.1:5000/".
