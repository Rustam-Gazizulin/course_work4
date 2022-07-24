from flask_restx import Resource, Namespace
from implemented import movie_service, movie_schema, movies_schema
from flask import request


movie_ns = Namespace('movies')



@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        page_num = request.args.get('page', None)
        director = request.args.get('director', None)
        genre = request.args.get('genre', None)
        status = request.args.get('status', None)
        movies = movie_service.get_all(page_num, director, genre, status)
        return movies_schema.dump(movies), 200


@movie_ns.route('/<int:mid>/')
class MoviesView(Resource):
    def get(self, mid):
        movie = movie_service.get_one(mid)
        return movie_schema.dump(movie), 200


