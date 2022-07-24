from app.dao.user import UserDAO
import jwt
from hashlib import pbkdf2_hmac
from constants import JWT_ALGORITHM, JWT_SECRET, PWD_ITERATIONS, PWD_SALT
import base64
import hmac
from flask import abort


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_by_email(self, email):
        return self.dao.get_by_email(email).id

    def patch(self, uid, user_data):
        return self.dao.patch(uid, user_data)

    def get_id_by_token(self, data_headers):
        token = data_headers['Authorization'].split('Bearer ')[-1]
        data = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        uid = data['id']
        return uid

    def put(self, uid, user_data):
        user = self.get_one(uid)
        if not self.compare_passwords(user.password, user_data['old_password']):
            abort(400)
        user.password = self.get_hash(user_data['new_password'])
        self.dao.put(user)

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