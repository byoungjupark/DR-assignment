from typing import List
from app.DAO import crud


class TaskController:
    def __init__(self):
        self.crud = crud.TaskCRUD

    def create(self, name, completed) -> None:
        self.crud.create(name, completed)
        return None

    def get_all_tasks(self):
        return self.crud.get_all_tasks()

    def get_task(self, id) -> str:
        return self.crud.get_task(id)

    def update(self, id, **kwargs) -> bool:
        return self.crud.update(id, **kwargs)

    def delete_all_tasks(self) -> bool:      
        return self.crud.delete_all_task()

    def delete_task(self, id) -> bool:
        return self.crud.delete_task(id)