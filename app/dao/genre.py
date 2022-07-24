from app.dao.models.genre import Genre
from constants import PAGE_LIMIT


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self, page_num=None):
        if page_num:
            offset_rec = (int(page_num) - 1) * PAGE_LIMIT
            page_limit = PAGE_LIMIT
        else:
            offset_rec = None
            page_limit = None

        return self.session.query(Genre).order_by(Genre.id).offset(offset_rec).limit(page_limit).all()

    def get_one(self, gid):
        return self.session.query(Genre).get(gid)



