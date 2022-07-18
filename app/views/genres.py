from flask import request
from flask_restx import Resource, Namespace
from implemented import genre_service, genres_schema, genre_schema


genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        page_num = request.args.get('page', None)
        genres = genre_service.get_all(page_num)
        return genres_schema.dump(genres), 200


@genre_ns.route('/<int:did>/')
class GenreView(Resource):
    def get(self, did):
        genre = genre_service.get_one(did)
        return genre_schema.dump(genre), 200
