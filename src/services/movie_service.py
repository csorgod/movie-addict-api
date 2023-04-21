from sqlalchemy.orm import Session

from src.models.movie import Movie as MovieModel
from src.schemas.movie import Movie as MovieSchema

class MovieService():

    def get_all(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(MovieModel).offset(skip).limit(limit).all()

    def get_by_id(self, db: Session, movie_id: int):
        return db.query(MovieModel).filter(MovieModel.movie_id == movie_id).first()

    def create_new(self, db: Session, movie: MovieSchema):
        _movie = MovieModel(name = movie.name, release_date = movie.release_date)
        db.add(_movie)
        db.commit()
        db.refresh(_movie)
        return _movie
