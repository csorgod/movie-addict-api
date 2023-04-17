from sqlalchemy.orm import Session

from src.models.movie import Movie as MovieModel
from src.schemas.movie import Movie as MovieSchema

class MovieService():

    def get_all(db: Session, skip: int = 0, limit: int = 100):
        return db.query(MovieModel).offset(skip).limit(limit).all()

    def get_by_id(db: Session, cat_id: int):
        return db.query(MovieModel).filter(MovieModel.cat_id == cat_id).first()

    def create_new(db: Session, adventurer: MovieSchema):
        _adventurer = MovieModel(adventurer.name, adventurer.breed, adventurer.profession)
        db.add(_adventurer)
        db.commit()
        db.refresh(_adventurer)
        return _adventurer
