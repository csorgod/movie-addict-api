from datetime import datetime

from src.schemas.base_schema import BaseSchema as BaseModel

class Movie(BaseModel):
    movie_id: int
    name: str
    release_date: datetime

class MovieResponse(BaseModel):
    movie_id: int
    name: str
    release_date: datetime
