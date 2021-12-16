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

    def __init__(self, name, email, phone, age, education, state):
        self.name = name
        self.email = email
        self.phone = phone
        self.age = age
        self.education = education
        self.state = state