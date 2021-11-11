from typing import Optional

from pydantic import BaseModel


class TaskCreate(BaseModel):
    name: str
    completed: bool


class TaskUpdate(BaseModel):
    name: Optional[str] = None
    completed: Optional[bool] = None


class Task(TaskCreate):
    id: int

    class Config:
        orm_mode = True

