from sqlalchemy import desc

from app.dao.models.movie import Movie
from constants import PAGE_LIMIT


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self, page_num=None, director=None, genre=None, status=None):
        if page_num:
            offset_rec = (int(page_num) - 1) * PAGE_LIMIT
            page_limit = PAGE_LIMIT
        else:
            offset_rec = None
            page_limit = None

        req = self.session.query(Movie)
        if status == 'new':
            req = req.order_by(desc(Movie.year))

        if director:
            req = req.filter(Movie.director_id == director)

        if genre:
            req = req.filter(Movie.genre_id == genre)

        return req.offset(offset_rec).limit(page_limit).all()

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)
