from dao.genre import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_all_genres(self):
        return self.dao.get_all_genres()

    def get_one_genre(self, aid):
        return self.dao.get_one_genre(aid)
