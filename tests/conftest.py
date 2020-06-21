import pytest

from flask_resty.testing import ApiClient, assert_response, assert_shape
from unittest.mock import ANY

from comments import app

@pytest.fixture(scope="session")
def db():
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    db = app.extensions["sqlalchemy"].db
    db.create_all()
    return db

@pytest.fixture(autouse=True)
def clean_tables(db):
    for table in reversed(db.metadata.sorted_tables):
        db.session.execute(table.delete())

    db.session.commit()
    yield
    db.session.rollback()

@pytest.fixture
def client(monkeypatch):
    monkeypatch.setattr(app, "testing", True)
    monkeypatch.setattr(app, "test_client_class", ApiClient)
    return app.test_client()
