from typing import Optional
from fastapi.exceptions import HTTPException
from pydantic import BaseModel, Field
from pydantic.error_wrappers import ValidationError


class TaskCreate(BaseModel):
    name: str = Field(min_length=1, max_length=150)
    completed: bool

    def __init__(self, **data):
        try:
            super(TaskCreate, self).__init__(**data)
        except ValidationError:
            raise HTTPException(status_code=400, detail="ValidationError")


class TaskUpdate(BaseModel):
    name: Optional[str] = Field(min_length=1, max_length=150)
    completed: Optional[bool] = None

    def __init__(self, **data):
        try:
            super(TaskUpdate, self).__init__(**data)
        except ValidationError:
            raise HTTPException(status_code=400, detail="ValidationError")


class Task(TaskCreate):
    id: int

    class Config:
        orm_mode = True

