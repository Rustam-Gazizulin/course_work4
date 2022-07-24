from flask import Flask
from flask_restx import Api
from config import Config
from app.views.directors import director_ns
from app.views.genres import genre_ns
from app.views.movies import movie_ns
from app.views.favourite_movie import favourite_ns
from app.views.auth import auth_ns
from app.views.user import user_ns
from setup_db import db
from flask_cors import CORS

cors = CORS()


def create_app(config: Config):
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()
    cors.init_app(application)
    register_extensions(application)
    return application


def register_extensions(app):
    api = Api(app)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(auth_ns)
    api.add_namespace(user_ns)
    api.add_namespace(favourite_ns)
    db.init_app(app)


def create_db():
    db.create_all()



app_config = Config()
app = create_app(app_config)


if __name__ == '__main__':
    app.run()
    create_db()

