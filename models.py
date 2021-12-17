from app import db
 
class user(db.Model):
    __tablename__="user"
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String)
    email=db.Column(db.String)
    phone=db.Column(db.String)
    age=db.Column(db.Integer)
    education=db.Column(db.String)
    state=db.Column(db.String)
    
    avatar_id = db.Column(db.Integer, db.ForeignKey('avatars.id'))

    def __init__(self, name, email, phone, age, education, state, avatar_id):
        self.name = name
        self.email = email
        self.phone = phone
        self.age = age
        self.education = education
        self.state = state
        self.avatar_id = avatar_id

class avatars(db.Model):
    __tablename__="avatars"
    id=db.Column(db.Integer, primary_key=True)
    link=db.Column(db.String)

    def __init__(self, link):
        self.link = link