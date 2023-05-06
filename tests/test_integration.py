import pytest
from datetime import datetime

from fastapi.testclient import TestClient

from src.models.movie import Movie
from src.schemas.movie import Movie as MovieSchema
from src.services.movie_service import MovieService
from tests.test_config import db_session


@pytest.mark.anyio
def test_user_get(db_session):
    obj = MovieSchema(name="fulano", release_date=datetime.now())
    item: Movie = MovieService().create_new(db_session, obj)
    item2: Movie = MovieService().get_by_id(db_session, movie_id = item.movie_id)

    assert item == item2
