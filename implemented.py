from setup_db import db
from app.dao.director import DirectorDAO
from app.services.director import DirectorService
from app.dao.models.director import DirectorSchema

from app.dao.genre import GenreDAO
from app.services.genre import GenreService
from app.dao.models.genre import GenreSchema

from app.dao.movie import MovieDAO
from app.services.movie import MovieService
from app.dao.models.movie import MovieSchema

from app.services.auth import AuthService
from app.dao.user import UserDAO
from app.dao.models.user import UserSchema



director_dao = DirectorDAO(db.session)
director_service = DirectorService(dao=director_dao)
directors_schema = DirectorSchema(many=True)
director_schema = DirectorSchema()

genre_dao = GenreDAO(db.session)
genre_service = GenreService(dao=genre_dao)
genres_schema = GenreSchema(many=True)
genre_schema = GenreSchema()

movie_dao = MovieDAO(db.session)
movie_service = MovieService(dao=movie_dao)
movies_schema = MovieSchema(many=True)
movie_schema = MovieSchema()

user_dao = UserDAO(db.session)
users_schema = UserSchema(many=True)
user_schema = UserSchema()

auth_service = AuthService(dao=user_dao)
