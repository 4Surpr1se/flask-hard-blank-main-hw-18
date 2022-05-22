from flask_restx import Resource, Namespace

from container import director_service
from dao.model.directors import DirectorSchema


director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)



@director_ns.route('/')
class MoviesView(Resource):
    def get(self):
        all_directors = director_service.get_all_directors()
        return directors_schema.dump(all_directors), 200


@director_ns.route('/<int:uid>')
class MovieView(Resource):
    def get(self, uid):
        director = director_service.get_one_director(uid)
        return director_schema.dump(director), 200
