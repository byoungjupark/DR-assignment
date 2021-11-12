from typing import List
from fastapi import Depends, HTTPException, APIRouter
from pydantic.error_wrappers import ValidationError
from sqlalchemy.orm import Session
from starlette.responses import Response

from app.dependencies import get_db
from . import models, schemas


router = APIRouter(
    prefix="/task",
    responses={404:{"description":"Not Found"}}
)


@router.post("/")
def create_task(task:schemas.TaskCreate, db:Session=Depends(get_db)): 
    task = models.Task(**task.dict())
    db.add(task)
    db.commit()
    db.refresh(task)
    return task



@router.get("/", response_model=List[schemas.Task])
def get_all_tasks(db:Session=Depends(get_db)):
    return db.query(models.Task).all()


@router.get("/{task_id}", response_model=schemas.Task)
def get_task(task_id:int, db:Session=Depends(get_db)):
    task = db.query(models.Task).get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.patch("/{task_id}")
def update_task(task_id:int, update_task:schemas.TaskUpdate, db:Session=Depends(get_db)):
    task = db.query(models.Task).get(task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    task_data = update_task.dict(exclude_unset=True)

    for key, value in task_data.items():
        setattr(task, key, value)

    db.add(task)
    db.commit()
    db.refresh(task)
    return task


@router.delete("/")
def delete_all_tasks(db:Session=Depends(get_db)):
    tasks = db.query(models.Task).all()
    for task in tasks:
        db.delete(task)
        db.commit()
    return Response(status_code=200)


@router.delete("/{task_id}")
def delete_task(task_id:int, db:Session=Depends(get_db)):
    task = db.query(models.Task).get(task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(task)
    db.commit()
    return Response(status_code=200)