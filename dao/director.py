from dao.model.directors import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_all_directors(self):
        return self.session.query(Director).all()

    def get_one_director(self, aid):
        return self.session.query(Director).get(aid)
