import pytest

from run import app, db


TEST_DATABASE_URL = "postgresql+psycopg://postgres:Prokopyizanagi1107@localhost:5432/notes_test_db"


@pytest.fixture
def client():
    app.config["SQLALCHEMY_DATABASE_URI"] = TEST_DATABASE_URL
    app.config["TESTING"] = True

    with app.app_context():
        db.drop_all()
        db.create_all()

    with app.test_client() as client:
        yield client

    with app.app_context():
        db.drop_all()