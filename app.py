import os
from flask import Flask, render_template, request
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
# app.config.from_object(os.environ['APP_SETTINGS'])

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://sonakshi:sonakshi@localhost/workshop'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True

db = SQLAlchemy(app)
migrate = Migrate(app, db)
from models import user, avatars

# two decorators, same function
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register')
def register():
    avatar=avatars.query.all()
    return render_template("register.html",avatars=avatar)

@app.route('/attendees')
def attendees():
    users=user.query.all()
    avatar=avatars.query.all()
    usr_list = []
    for u in users:
        for av in avatar:
            if av.id==u.avatar_id:
                lin=av.link
                break
        usr = {
            'id': u.id,
            'name': u.name,
            'age': u.age,
            'education': u.education,
            'state': u.state,
            'avatar': lin
            }
        usr_list.append(usr)
    return render_template("attendees.html",users=usr_list)

@app.route('/add-user', methods = ['POST'])
def addUser():
    try :
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        age = request.form.get('age')
        education = request.form.get('education')
        state = request.form.get('state')
        avatar = request.form.get('avatar')

        if name and email and phone and age and education and state:

            if user.query.filter_by(email=email).first():
                return("Email ID already Exists")
            else:
                db.session.add(user(name=name, email=email, phone=phone, age=age, education=education, state=state, avatar_id=avatar))
                db.session.commit()
                return("Thank you for registering")
        else:
            return("Please fill all the fields")
    except Exception as e:
        print(e)
        return("Something went wrong")

if __name__ == '__main__':
    app.run(debug=True)