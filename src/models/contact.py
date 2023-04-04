from server import db
import sqlalchemy
from enum import Enum
class degree(Enum):
    associate = 0
    bachelor = 1
    master = 1
    doctoral = 1
    professional = 1


class Contact(db.Model):
    __tablename__ = 'contacts'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), unique=False, nullable=False, primary_key=True)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    national_id = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=True)
    gender = db.Column(db.String(6))
    gpa = db.Column(db.Float, nullable=True)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=sqlalchemy.sql.func.now())
    birthday = db.Column(db.DateTime(timezone=True),nullable = True)
    description = db.Column(db.Text(1000), nullable=True, primary_key=False)
    degree = db.Column(sqlalchemy.Enum(degree), nullable=True, primary_key=False)
    def __repr__(self):
        return "<Title: {}>".format(self.first_name + " " + self.last_name)