import os
import json

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager


BASE_DIR    = os.path.dirname(__file__)
SECRET_FILE = os.path.join(BASE_DIR, 'secrets.json')
secrets     = json.loads(open(SECRET_FILE).read())
DB          = secrets["DB"]


class Database:
    def __init__(self):
        self.engine = create_engine(f"mysql+pymysql://{DB['user']}:{DB['password']}@{DB['host']}:{DB['port']}/{DB['database']}?charset=utf8")
        self._session = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    @contextmanager
    def get_db(self):
        db = self._session()
        try:
            yield db
        finally:
            db.close()


db = Database()
Base = declarative_base()