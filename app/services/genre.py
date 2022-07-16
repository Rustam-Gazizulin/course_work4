from app.dao.genre import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_all(self, page_num):
        return self.dao.get_all(page_num)

    def get_one(self, did):
        return self.dao.get_one(did)
