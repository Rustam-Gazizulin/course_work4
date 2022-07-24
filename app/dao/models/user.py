from setup_db import db
from sqlalchemy.orm import relationship
from marshmallow import Schema, fields
from app.dao.models.user_movie_rel import user_movie_table
from app.dao.models.user_movie_rel import FavouriteSchema

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    favourite_genre = db.Column(db.Integer, db.ForeignKey('genre.id'))
    movies = relationship('Movie', secondary=user_movie_table, back_populates='users')


class UserSchema(Schema):
    id = fields.Int()
    email = fields.Str()
    password = fields.Str()
    name = fields.Str()
    surname = fields.Str()
    favourite_genre = fields.Int()
    movies = fields.Nested(FavouriteSchema)
