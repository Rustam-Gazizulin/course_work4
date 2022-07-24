from app.dao.models.user_movie_rel import user_movie_table
from setup_db import db
import jwt
from constants import JWT_SECRET, JWT_ALGORITHM
from sqlalchemy import select


class FavouriteService:
    def __init__(self):
        pass

    def get_one(self, uid):
        return self.get_one(uid)

    def get_by_id(self, uid):
        stmt = select(user_movie_table.c.movie_id).where(user_movie_table.c.user_id == uid)
        favourite_movies = db.session.execute(stmt).fetchall()
        return favourite_movies


    def post(self, user_id, movie_id):
        pass

    def delete(self):
        pass

    def get_id_by_token(self, data_headers):
        token = data_headers['Authorization'].split('Bearer ')[-1]
        data = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        uid = data['id']
        return uid
