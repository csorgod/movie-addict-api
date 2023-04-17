from typing import Any, Generator

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from main import get_application
from db import db, engine, session_local
from src.dependencies.database import get_db


@pytest.fixture(autouse=True)
def app() -> Generator[FastAPI, Any, None]:
    db.metadata.create_all(bind = engine)
    _app = get_application()
    yield _app
    db.metadata.drop_all(bind = engine)

@pytest.fixture
def db_session() -> Generator[session_local, Any, None]:
    # Start the connection and yield until the end of the transaction
    connection = engine.connect()
    transaction = connection.begin()
    session = session_local(bind=connection)
    yield session 

    # Close and rollback the transaction to undo everything persisted in the test
    session.close()
    transaction.rollback()
    connection.close()

@pytest.fixture()
def client(app: FastAPI, db_session: session_local) -> Generator[TestClient, Any, None]:

    # Yields a db_session using the fixture `db_session`
    def _get_test_db():
        try:
            yield db_session
        finally:
            pass

    # overrides the dependency from the fastAPI instance
    app.dependency_overrides[get_db] = _get_test_db
    
    with TestClient(app) as client:
        yield client