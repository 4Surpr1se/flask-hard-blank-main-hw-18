from dao.model.genres import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_all_genres(self):
        return self.session.query(Genre).all()

    def get_one_genre(self, aid):
        return self.session.query(Genre).get(aid)
