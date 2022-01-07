from app import db

from werkzeug.security import generate_password_hash, check_password_hash


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200))
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.Text)
    
    def __init__(self, username, password, email, name):
        self.username = username
        self.password = password
        self.email = email
        self.name = name

    def setPassword(self, password):
        self.password = generate_password_hash(password)

    def checkPassword(self, password):
        return check_password_hash(self.password, password)