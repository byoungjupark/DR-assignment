from pydantic import BaseModel


class TaskBase(BaseModel):
    name: str
    completed: bool

class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True

