from flask_restx import Namespace, Resource
from flask import request
from implemented import auth_service


auth_ns = Namespace('auth')


@auth_ns.route('/register/')
class AuthRegisterView(Resource):
    def post(self):
        user_data = request.json
        email = user_data.get('email')
        if ('@' not in email) or ('.' not in email):
            return "invalid email", 400
        user = auth_service.register_user(user_data)
        if user == 'user already exists':
            return "Такой пользователь уже существует", 400
        if user == 'email not entered':
            return "Email не задан", 400
        if user == 'password not entered':
            return "Пароль не задан", 400

        return "", 201


@auth_ns.route('/login/')
class AuthLoginView(Resource):
    def post(self):
        user_data = request.json
        email = user_data.get('email')
        password = user_data.get('password')
        if None in [email, password]:
            return "Не введен логин или пароль", 400

        return auth_service.genereate_token(email, password)

    def put(self):
        data = request.json
        token = data.get('refresh_token')
        return auth_service.approve_refresh_token(token)
