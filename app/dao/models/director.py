from setup_db import db
from marshmallow import Schema, fields
from sqlalchemy.orm import relationship


class Director(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)


class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    movies = relationship('Movie')
