from dao.director import DirectorDAO


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_all_directors(self):
        return self.dao.get_all_directors()

    def get_one_director(self, aid):
        return self.dao.get_one_director(aid)
