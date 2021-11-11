import os
import json

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

BASE_DIR    = os.path.dirname(__file__)
SECRET_FILE = os.path.join(BASE_DIR, 'secrets.json')
secrets     = json.loads(open(SECRET_FILE).read())
DB          = secrets["DB"]

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{DB['user']}:{DB['password']}@{DB['host']}:{DB['port']}/{DB['database']}?charset=utf8"

engine       = create_engine(SQLALCHEMY_DATABASE_URL, encoding = 'utf-8')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base         = declarative_base()