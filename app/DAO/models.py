from sqlalchemy import Boolean, Column, Integer, String
from app.database import Base


class Task(Base):
    __tablename__ = "tasks"

    id        = Column(Integer, primary_key=True, index=True)
    name      = Column(String(150))
    completed = Column(Boolean, default=False)