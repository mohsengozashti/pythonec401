from database import getDB
from sqlalchemy.sql import func
from sqlalchemy import Enum as AlchemyEnum
from models.address import Address

db = getDB()

from enum import Enum
class Degree(Enum):
    associate = 0
    bachelor = 1
    master = 2 
    doctoral = 3
    professional = 4


class Contact(db.Model):
    __tablename__ = 'contacts'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    first_name = db.Column(db.String(80), unique=False, nullable=False, primary_key=True)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    national_id = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=True)
    gender = db.Column(db.Boolean)
    gpa = db.Column(db.Float, nullable=True)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    birthday = db.Column(db.DateTime(timezone=True),nullable = True)
    description = db.Column(db.Text(1000), nullable=True, primary_key=False)
    degree = db.Column(AlchemyEnum(Degree), nullable=True, primary_key=False)
    addresses = db.relationship('Address', backref='contact', lazy=True)

    def __repr__(self):
        return "<NationalId: {}>".format(self.first_name + " " + self.last_name)