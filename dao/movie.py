from dao.model.movies import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all_movies(self):
        return self.session.query(Movie).all()

    def get_one_movie(self, aid):
        return self.session.query(Movie).get(aid)

    def create_movie(self, data):
        movie = Movie(**data)

        self.session.add(movie)
        self.session.commit()

        return movie

    def update_movie(self, movie):

        self.session.add(movie)
        self.session.commit()

        return movie

    def delete_movie(self, aid):
        movie = self.get_one_movie(aid)
        self.session.delete(movie)
        self.session.commit()

    def movie_by_director(self, director_id):
        return self.session.query(Movie).filter(Movie.director_id == director_id).all()

    def movie_by_genre(self, genre_id):
        return self.session.query(Movie).filter(Movie.genre_id == genre_id).all()

    def movie_by_year(self, year):
        return self.session.query(Movie).filter(Movie.year == year).all()