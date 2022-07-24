import hmac
import base64
import jwt
import calendar
import datetime

from flask_restx import abort

from app.dao.user import UserDAO
from hashlib import pbkdf2_hmac
from constants import PWD_SALT, PWD_ITERATIONS, JWT_SECRET, JWT_ALGORITHM


class AuthService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def register_user(self, user_data):
        email = user_data.get('email')
        password = user_data.get('password')
        if not email:
            return "email not entered"

        if not password:
            return "password not entered"
        result = self.verify_user(email)
        if result:
            return "user already exists"

        user_data['password'] = self.get_hash(password)
        return self.dao.create(user_data)

    def verify_user(self, email):
        return self.dao.get_by_email(email)

    def get_hash(self, password):
        hash_digest = pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_SALT,
            PWD_ITERATIONS
        )
        return base64.b64encode(hash_digest)

    def compare_passwords(self, password_hashed, password) -> bool:
        digest_decoded = base64.b64decode(password_hashed)
        digest_hashed = pbkdf2_hmac('sha256',
                                password.encode('utf-8'),
                                PWD_SALT,
                                PWD_ITERATIONS)

        return hmac.compare_digest(digest_decoded, digest_hashed)

    def genereate_token(self, email, password, is_refresh=False):
        user = self.dao.get_by_email(email)
        if not user:
            abort(400)
            # return "user not found"

        if not is_refresh:
            if not self.compare_passwords(user.password, password):
                abort(400)

        data = {
            "id": user.id,
            "email": email
        }
        min30 = datetime.datetime.now() + datetime.timedelta(minutes=30)
        data['exp'] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)

        days130 = datetime.datetime.now() + datetime.timedelta(days=130)
        data['exp'] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)

        return {
            'access_token': access_token,
            'refresh_token': refresh_token
        }

    # def check_token(self, token):
    #     try:
    #         jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    #         return True
    #     except Exception:
    #         return False

    def approve_refresh_token(self, token):
        data = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        email = data['email']
        return self.genereate_token(email, None, is_refresh=True)
