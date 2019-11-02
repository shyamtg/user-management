from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from marshmallow import fields

db = SQLAlchemy()
ma = Marshmallow()

# User DB Class/Model
class UserData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(32), nullable=False)
    last_name = db.Column(db.String(32), nullable=True)
    email = db.Column(db.String(32), nullable=False, unique=True)
    phone_number = db.Column(db.String(15), nullable=False, unique=True)
    dob= db.Column(db.Date, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    __tablename__ = 'user_data'

    def __repr__(self):
        return '<User {} {}>'.format(self.first_name, self.last_name)

    def __init__(self, first_name, last_name, email,
                 phone_number,dob, date_created=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.dob = dob
        self.date_created = date_created

class UserDataSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    first_name = fields.String(required=True)
    last_name = fields.String(required=False)
    email = fields.String(required=True)
    phone_number = fields.String(required=True)
    dob = fields.Date(required=True)
    date_created = fields.DateTime()

user_schema = UserDataSchema()
user_schema_list = UserDataSchema(many=True)



