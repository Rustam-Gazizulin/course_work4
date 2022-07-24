import jwt
from flask_restx import Namespace, Resource
from implemented import user_service, user_schema
from flask import request, abort
from constants import JWT_SECRET, JWT_ALGORITHM


user_ns = Namespace('user')


def auth_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)
        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]
        try:
            jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        except Exception:
            abort(401)
        return func(*args, **kwargs)

    return wrapper


@user_ns.route('/')
class UserView(Resource):
    @auth_required
    def get(self):
        uid = user_service.get_id_by_token(request.headers)
        user = user_service.get_one(uid)
        if user:
            return user_schema.dump(user), 200
        else:
            return "Пользователь не найден", 404

    @auth_required
    def patch(self):
        user_data = request.json
        uid = user_service.get_id_by_token(request.headers)
        result = user_service.patch(uid, user_data)
        if not result:
            return "Пользователь не найден", 404

        return "Данные пользователя обновлены", 204


@user_ns.route('/password/')
class UserUpdateView(Resource):
    @auth_required
    def put(self):
        user_data = request.json
        uid = user_service.get_id_by_token(request.headers)
        user_service.put(uid, user_data)


