from flask import request
from flask_restx import Resource, Namespace
from implemented import director_service, directors_schema, director_schema


director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        page_num = request.args.get('page', None)
        directors = director_service.get_all(page_num)
        return directors_schema.dump(directors), 200


@director_ns.route('/<int:did>/')
class DirectorView(Resource):
    def get(self, did):
        director = director_service.get_one(did)
        return director_schema.dump(director), 200
