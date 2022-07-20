from setup_db import db


user_movie_table = db.Table(
    "user_movie_rel",
    db.Column("user_id", db.ForeignKey("user.id")),
    db.Column("movie_id", db.ForeignKey("movie.id"))
)

