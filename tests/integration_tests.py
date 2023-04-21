import pytest

from fastapi.testclient import TestClient

from src.models.movie import Movie
from src.schemas.movie import Movie as MovieSchema
from src.services.movie_service import MovieService


@pytest.mark.anyio
def test_user_get(session):
    obj = MovieSchema(name="fulano", age="24")
    item: Movie = MovieService().create_new(session, obj)
    item2: Movie = MovieService().get_by_id(session, movie_id = item.movie_id)

    assert item == item2
