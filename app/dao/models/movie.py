from app.dao.models.director import DirectorSchema
from app.dao.models.genre import GenreSchema
from setup_db import db
from sqlalchemy.orm import relationship
from marshmallow import Schema, fields
from app.dao.models.user_movie_rel import user_movie_table


class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    trailer = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'), nullable=False)
    genre = relationship('Genre')
    director_id = db.Column(db.Integer, db.ForeignKey('director.id'), nullable=False)
    director = relationship('Director')
    users = relationship('User', secondary=user_movie_table, back_populates='movies')


# class MovieSchema(Schema):
#     id = fields.Int()
#     title = fields.Str()
#     description = fields.Str()
#     trailer = fields.Str()
#     year = fields.Int()
#     rating = fields.Float()
#     genre_id = fields.Int()
#     director_id = fields.Int()

class MovieSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
    genre = fields.Nested(GenreSchema)
    director = fields.Nested(DirectorSchema)
