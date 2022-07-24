from app.dao.models.user import User
from constants import PAGE_LIMIT


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self, page_num=None):
        if page_num:
            offset_rec = (int(page_num) - 1) * PAGE_LIMIT
            page_limit = PAGE_LIMIT
        else:
            offset_rec = None
            page_limit = None

        return self.session.query(User).order_by(User.id).offset(offset_rec).limit(page_limit).all()

    def get_one(self, uid):
        return self.session.query(User).get(uid)

    def get_by_email(self, email):
        try:
            user = self.session.query(User).filter(User.email == email.strip()).one()
            return user
        except Exception:
            return False

    def create(self, user_data):
        user = User(**user_data)
        self.session.add(user)
        self.session.commit()
        return user

    def patch(self, uid, user_data):
        user = self.get_one(uid)
        if not user:
            return False
        if user_data.get('name'):
            user.name = user_data.get('name')
        if user_data.get('surname'):
            user.surname = user_data.get('surname')
        if user_data.get('favourite_genre'):
            user.favourite_genre = user_data.get('favourite_genre')

        self.session.add(user)
        self.session.commit()
        return user

    def put(self, user):
        self.session.add(user)
        self.session.commit()
