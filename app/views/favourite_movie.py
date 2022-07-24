from flask_restx import Resource, Namespace
from flask import request, jsonify
from implemented import user_service, movie_service, favourite_service
from setup_db import db


favourite_ns = Namespace('favorites')


@favourite_ns.route('/movies/')
class FavouriteMovies(Resource):
    def get(self):
        user_id = user_service.get_id_by_token(request.headers)
        favourite_movies = favourite_service.get_by_id(user_id)
        fm = []
        for item in favourite_movies:
            dict_ = {"id": item[0]}
            fm.append(dict_)
        return jsonify(fm)


@favourite_ns.route('/movies/<int:movie_id>/')
class FavouriteMovie(Resource):
    def post(self, movie_id):
        user_id = user_service.get_id_by_token(request.headers)
        user = user_service.get_one(user_id)
        movie = movie_service.get_one(movie_id)
        user.movies.append(movie)
        db.session.add(user)
        db.session.commit()
        return "", 201

    def delete(self, movie_id):
        user_id = user_service.get_id_by_token(request.headers)
        user = user_service.get_one(user_id)
        movie = movie_service.get_one(movie_id)
        user.movies.remove(movie)
        db.session.add(user)
        db.session.commit()
        return "", 200
