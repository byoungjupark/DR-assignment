from typing import List
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.responses import Response

from . import models, schemas


def create_task(db:Session, task:schemas.TaskCreate):
    task = models.Task(**task.dict())
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def get_all_tasks(db:Session):
    return db.query(models.Task).all()

def get_task(db:Session, id:int):
    task = db.query(models.Task).get(id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

def update_task(db:Session, id:int, update_task:schemas.TaskUpdate):
    task = db.query(models.Task).get(id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    task_data = update_task.dict(exclude_unset=True)

    for key, value in task_data.items():
        setattr(task, key, value)

    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def delete_all_tasks(db:Session):
    tasks = db.query(models.Task).all()
    for task in tasks:
        db.delete(task)
        db.commit()
    return Response(status_code=200)

def delete_task(db:Session, id:int):
    task = db.query(models.Task).get(id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(task)
    db.commit()
    return Response(status_code=200)