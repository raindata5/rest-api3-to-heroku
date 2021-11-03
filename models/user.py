import sqlite3
from sqlalc import db


class UserModel(db.Model):  # why do we create a user object?
    __tablename__ = 'User'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))

    def __init__(self, username, password):  # see if we have to change the _id?
        self.username = username
        self.password = password

    def save_to_database(self):
        db.session.add(self)
        db.session.commit()

    @classmethod  # Why are we making a class method?
    def get_user_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def get_user_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
