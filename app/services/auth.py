from app.dao.user import UserDAO
from hashlib import pbkdf2_hmac
from constants import PWD_SALT, PWD_ITERATIONS
import base64


class AuthService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    # def get_all(self, page_num):
    #     return self.dao.get_all(page_num)
    #
    # def get_one(self, did):
    #     return self.dao.get_one(did)

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

        user_data['password'] = generate_password(password)
        return self.dao.create(user_data)

    # def login_user(self, user_data):
    #     email = user_data.get('email')
    #     password = user_data.get('password')
    #     self.verify_user(email, password)

    def verify_user(self, email):
        return self.dao.get_by_email(email)

    def genereate_token(self, data):
        pass

    def check_token(self, token):
        pass


def generate_password(password):
    hash_digest = pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        PWD_SALT,
        PWD_ITERATIONS
    )
    return base64.b64encode(hash_digest)
