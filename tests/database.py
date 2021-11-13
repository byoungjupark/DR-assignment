import os
import json

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base
from app.dependencies import get_db
from app.main import app


BASE_DIR    = os.path.dirname(__file__)
SECRET_FILE = os.path.join(BASE_DIR, 'secrets.json')
secrets     = json.loads(open(SECRET_FILE).read())
DB          = secrets["DB"]

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{DB['user']}:{DB['password']}@{DB['host']}:{DB['port']}/{DB['database']}?charset=utf8"

engine              = create_engine(SQLALCHEMY_DATABASE_URL, encoding='utf-8')
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()     

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)