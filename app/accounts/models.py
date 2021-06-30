from ..extensions import db
from datetime import datetime
from werkzeug.security import generate_password_hash


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String, nullable=False)

    joined = db.Column(db.DateTime, default=datetime.utcnow())
    last_updated = db.Column(db.DateTime,  default=datetime.utcnow(), onupdate=datetime.utcnow())

    def __repr__(self):
        return '<User %s>' % self.email

    def __init__(self, email, password):
        self.email = email
        self.password_hash = generate_password_hash(password)

