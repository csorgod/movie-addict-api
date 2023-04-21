from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from db import db

class Movie(db):
    __tablename__ = "movie"

    movie_id = Column(Integer, primary_key=True, index=True, nullable=False)
    
    name = Column(String(50), nullable = False)
    release_date = Column(DateTime, nullable = False)
    

    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.release_date = kwargs.get('release_date')
