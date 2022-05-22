from dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_all_movies(self, query_args):
        if query_args:
            return self.movie_by_query(query_args)
        else:
            return self.dao.get_all_movies()

    def get_one_movie(self, aid):
        return self.dao.get_one_movie(aid)

    def create_movie(self, data):
        return self.dao.create_movie(data)

    def update_movie(self, data):
        aid = data.get("id")

        movie = self.get_one_movie(aid)

        movie.title = data.get("title")
        movie.description = data.get("description")
        movie.trailer = data.get("trailer")
        movie.year = data.get("year")
        movie.rating = data.get("rating")
        movie.genre_id = data.get("genre_id")
        movie.director_id = data.get("director_id")

        self.dao.update_movie(movie)

        return

    def update_partial_movie(self, data):
        aid = data.get("id")

        movie = self.get_one_movie(aid)

        if 'title' in data:
            movie.title = data.get("title")

        if 'description' in data:
            movie.description = data.get("description")

        if 'trailer' in data:
            movie.trailer = data.get("trailer")

        if 'year' in data:
            movie.year = data.get("year")

        if 'rating' in data:
            movie.rating = data.get("rating")

        if 'genre_id' in data:
            movie.genre_id = data.get("genre_id")

        if 'director_id' in data:
            movie.director_id = data.get("director_id")

        return self.dao.update_movie(movie)

    def delete_movie(self, aid):
        self.dao.delete_movie(aid)

    def movie_by_query(self, query_args):
        director_id = query_args.get("director_id")
        if director_id:
            return self.dao.movie_by_director(director_id)

        genre_id = query_args.get("genre_id")
        if genre_id:
            return self.dao.movie_by_genre(genre_id)

        year = query_args.get("year")
        if year:
            return self.dao.movie_by_year(year)
