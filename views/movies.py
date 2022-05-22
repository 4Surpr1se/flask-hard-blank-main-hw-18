from flask import request
from flask_restx import Resource, Namespace

from container import movie_service
from dao.model.movies import MovieSchema

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        req_args = request.args
        all_movies = movie_service.get_all_movies(req_args)
        return movies_schema.dump(all_movies), 200

    def post(self):
        req_json = request.json
        movie_service.create_movie(req_json)
        return "", 201


@movie_ns.route('/<int:uid>')
class MovieView(Resource):
    def get(self, uid):
        movie = movie_service.get_one_movie(uid)
        return movie_schema.dump(movie)

    def put(self, uid):
        req_json = request.json
        req_json["id"] = uid
        movie_service.update_movie(req_json)

        return "", 204

    def patch(self, uid):
        req_json = request.json
        req_json["id"] = uid
        movie_service.update_partial_movie(req_json)

        return "", 204

    def delete(self, uid):
        movie_service.delete_movie(uid)
        return "", 204
