from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import string
import random

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    date_of_registration = db.Column(db.DateTime, default=datetime.now())
    date_of_update = db.Column(db.DateTime, onupdate=datetime.now())
    storeitems = db.relationship('Storeitem', backref=db.backref('user'))

    def __repr__(self) -> str:
        return 'User>>> {self.username}'


class Storeitem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description= db.Column(db.Text, nullable=False)
    url = db.Column(db.Text, nullable=False)      
    short_url = db.Column(db.String(3), nullable=False)
    visits = db.Column(db.Integer, default=0)
    user_id  = db.Column(db.Integer, db.ForeignKey("user.id"))
    date_of_registration = db.Column(db.DateTime, default=datetime.now())
    date_of_update = db.Column(db.DateTime, onupdate=datetime.now())

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.url = self.generate_short_url()

    def generate_short_url(self):
        characters = string.digits + string.ascii_letters
        picked_chars = ''.join(random.choices(characters, k=3))

        link  = self.query.filter_by(short_url=picked_chars).first()

        if link:
            pass
        else:
            return picked_chars

    def __repr__(self) -> str:
        return 'User>>> {self.url}'


