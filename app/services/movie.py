from app.dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_all(self, page_num, director, genre):
        return self.dao.get_all(page_num, director, genre)

    def get_one(self, did):
        return self.dao.get_one(did)

    def get_by_director(self, did):
        pass
