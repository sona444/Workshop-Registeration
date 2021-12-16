import os
from flask import Flask, render_template, request
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy
import json
from werkzeug.datastructures import ImmutableMultiDict

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://sonakshi:sonakshi@localhost/workshop'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
from models import user

# two decorators, same function
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/attendees')
def attendees():
    users=user.query.all()
    return render_template("attendees.html",users=users)

@app.route('/add-user', methods = ['GET', 'POST'])
def addUser():
   if request.method == "POST":
         jsonData=request.form
         jsonData.to_dict(flat=True)
         print(jsonData)
         name = request.form.get('name')
         email = request.form.get('email')
         phone = request.form.get('phone')
         age = request.form.get('age')
         education = request.form.get('education')
         state = request.form.get('state')
         new_user = user(name=name, email=email, phone=phone, age=age, education=education, state=state)
         db.session.add(new_user)
         db.session.commit()
         return("updated")

if __name__ == '__main__':
    app.run(debug=True)