from typing import List

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status

from src.schemas.movie import Movie, MovieResponse
from src.services.movie_service import MovieService
from src.dependencies import database

router = APIRouter(prefix="/movies", tags=["Movies"])


@router.get("", response_model=List[MovieResponse], response_model_exclude_unset=True, status_code=status.HTTP_200_OK)
async def get_all(skip=0, limit=10, db: Session = Depends(database.get_db)):
    return MovieService().get_all(db, skip=skip, limit=limit)

@router.get("/{id}", response_model=MovieResponse, response_model_exclude_unset=True, status_code=status.HTTP_200_OK)
async def get_by_id(id: int, db: Session = Depends(database.get_db)):
    return MovieService().get_by_id(db, id)

@router.post("", status_code=status.HTTP_201_CREATED)
async def create(cat: Movie, db: Session = Depends(database.get_db)):
    return MovieService().create_new(db, cat)
