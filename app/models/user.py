from app import db
from sqlalchemy import func


class User(db.Model):
    __tablename__ = 'User'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    timestamp = db.Column(db.DateTime, default=func.now(), nullable=False)
    userName = db.Column(db.Boolean, nullable=True)
    password = db.Column(db.Boolean, nullable=True)

    def __init__(self, user_name, password):
        self.userName = user_name
        self.password = password

    def save(self):
        db.session.add(self)
        db.session.commit()
