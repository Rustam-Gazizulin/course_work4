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
        # movies = movie_service.get_all(page_num)
        movies = movie_service.get_all(page_num, director, genre)
        return movies_schema.dump(movies), 200

        # return {
        #            "id": 1,
        #            "title": "Йеллоустоун",
        #            "description": "Владелец ранчо пытается сохранить землю своих предков. Кевин Костнер в неовестерне от автора «Ветреной реки»",
        #            "trailer": "https://www.youtube.com/watch?v=UKei_d0cbP4",
        #            "year": 2018,
        #            "rating": 8.6,
        #            "genre": {
        #                "id": 17,
        #                "name": "Вестерн"
        #            },
        #            "director": {
        #                "id": 1,
        #                "name": "Тейлор Шеридан"
        #            }
        #        }, 200
        # return {
        #            "id": 1,
        #            "title": "Йеллоустоун",
        #            "description": "Владелец ранчо пытается сохранить землю своих предков. Кевин Костнер в неовестерне от автора «Ветреной реки»",
        #            "trailer": "https://www.youtube.com/watch?v=UKei_d0cbP4",
        #            "year": 2018,
        #            "rating": 8.6,
        #            "genre_id": 17,
        #            "director_id": 1
        #        }, 200



@movie_ns.route('/<int:did>/')
class MoviesView(Resource):
    def get(self, did):
        movie = movie_service.get_one(did)
        return movie_schema.dump(movie), 200
