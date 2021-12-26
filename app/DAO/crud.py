from typing import List
# from fastapi.param_functions import Depends
# from sqlalchemy.orm import Session
from sqlalchemy import select, update, delete
from sqlalchemy.sql.functions import mode
from app.database import db

from app.DAO import models


class TaskCRUD:
    def create(name, completed) -> None:
        with db.get_db() as session:
            task = models.Task(name=name, completed=completed)
            session.add(task)
            session.commit()
            session.refresh(task)
            return None
           
        
    def get_all_tasks():
        with db.get_db() as session:
            # tasks = session.execute(
            #     select(models.Task).order_by(models.Task.id)
            # ).all()
            tasks = session.query(models.Task).order_by(models.Task.id).all()
            print(tasks)
            task_list = [{"id":task.id, "name":task.name, "completed":task.completed} for task in tasks]
            print(task_list)
            return task_list


    def get_task(task_id) -> str:
        with db.get_db() as session:
            task = session.execute(
                select(models.Task).where(models.Task.id==task_id)
            ).scalar()

            if not task:
                return False

            return task
        # Session.execute(
        #     select(models.Task).where(models.Task.id==task_id)
        # )
        # return Session.query(models.Task).get(task_id)

    def update(task_id, name, completed) -> bool:
        with db.get_db() as session:
            task = select(models.Task).where(models.Task.id==task_id)
            
            if not task:
                return False
                
            session.execute(
                update(task)
                .values(name=name, completed=completed)
            )

            return True

    def delete_all_task() -> bool:
        with db.get_db() as session:
            tasks = select(models.Task).all()

            if not tasks:
                return False

            session.execute(delete(tasks))
            return True
    
    def delete_task(task_id) -> bool:
        with db.get_db() as session:
            task = select(models.Task).where(models.Task.id==task_id)
            
            if not task:
                return False

            session.execute(
                delete(task)
            )
            return True