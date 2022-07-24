from marshmallow import Schema, fields

from setup_db import db


user_movie_table = db.Table(
    "user_movie_rel",
    db.Column("user_id", db.ForeignKey("user.id")),
    db.Column("movie_id", db.ForeignKey("movie.id"))
)


class FavouriteSchema(Schema):
    user_id = fields.Int()
    movie_id = fields.Int()
