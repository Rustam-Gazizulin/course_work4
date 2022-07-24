from app.dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_all(self, page_num, director, genre, status):
        return self.dao.get_all(page_num, director, genre, status)

    def get_one(self, mid):
        return self.dao.get_one(mid)
