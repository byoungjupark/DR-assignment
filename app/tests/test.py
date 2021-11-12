import os
import json
import requests
import pytest

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from app.database import Base
from app.dependencies import get_db
from app.main import app
from app import tasks

BASE_DIR    = os.path.dirname(__file__)
SECRET_FILE = os.path.join(BASE_DIR, 'secrets.json')
secrets     = json.loads(open(SECRET_FILE).read())
DB          = secrets["DB"]

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{DB['user']}:{DB['password']}@{DB['host']}:{DB['port']}/{DB['database']}?charset=utf8"

engine              = create_engine(SQLALCHEMY_DATABASE_URL, encoding='utf-8')
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

@pytest.fixture(scope="module")
def client():
    app.dependency_overrides[get_db] = override_get_db
    test_client = TestClient(app)
    return test_client



def test_create_task(client):
    response = client.post(
        "task/",
        json = {"id":1, "name":"test", "completed":False}
    )
    assert response.status_code == 200


def test_get_all_tasks(client):
    response = client.get("task/")
    assert response.status_code == 200
    assert response.json() == [{
        "id"       : 1,
        "name"     : "test",
        "completed": False
    }]


def test_get_task(client):
    response = client.get("task/1")
    assert response.status_code == 200
    assert response.json() == {
        "id"       : 1,
        "name"     : "test",
        "completed": False
    }


def test_update_task(client):
    response = client.patch(
        "task/1",
        json = {"name":"change"}
    )
    assert response.status_code == 200


def test_delete_task(client):
    response = client.delete("task/1")
    assert response.status_code == 200


def test_delete_all_tasks(client):
    response = client.delete("task/")
    assert response.status_code == 200