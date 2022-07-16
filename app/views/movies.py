from flask_restx import Resource, Namespace
from implemented import movie_service, movie_schema, movies_schema
from flask import request


movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        page_num = request.args.get('page')
        movies = movie_service.get_all(page_num)
        return movies_schema.dump(movies), 200


@movie_ns.route('/<int:did>')
class MoviesView(Resource):
    def get(self, did):
        movie = movie_service.get_one(did)
        return movie_schema.dump(movie), 200
