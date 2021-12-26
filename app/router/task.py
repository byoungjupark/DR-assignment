from os import stat
from typing import List
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session, composite
from starlette.responses import Response

from app.command.task import TaskCommandCreate
from app.controller import taskcontroller


router = APIRouter(
    prefix="/task",
    responses={404:{"description":"Not Found"}}
)

@router.post("/")
def create_task(request: TaskCommandCreate):
    try:
        controller = taskcontroller.TaskController()
        controller.create(request.name, request.completed)

        return Response(status_code=200)
    except ValueError:
        return Response(status_code=400)

@router.get("/")
def get_all_tasks():
    controller = taskcontroller.TaskController()
    all_tasks=controller.get_all_tasks()
    return all_tasks

@router.get("/{task_id}")
def get_task(task_id:int):
    controller = taskcontroller.TaskController()
    task = controller.get_task(task_id)

    if not task:
        return Response(content="NO_CONTENT", status_code=400)

    return task

@router.patch("/{task_id}")
def update_task(task_id:int):
    controller = taskcontroller.TaskController()
    task = controller.update(task_id)

    if not task:
        return Response(content="NO_CONTENT", status_code=400)

    return Response(status_code=200)

# @router.patch("/{task_id}")
# def update_task(task_id:int, update_task:schemas.TaskUpdate, db:Session=Depends(get_db)):
#     task = db.query(models.Task).get(task_id)

#     if not task:
#         raise HTTPException(status_code=404, detail="Task not found")

#     task_data = update_task.dict(exclude_unset=True)

#     for key, value in task_data.items():
#         setattr(task, key, value)

#     db.add(task)
#     db.commit()
#     db.refresh(task)

#     return Response(status_code=200)

@router.delete("/")
def delete_all_tasks():
    controller = taskcontroller.TaskController()
    tasks = controller.delete_all_tasks()

    if not tasks:
        return Response(content="NO_CONTENT", status_code=400)

    return Response(status_code=204)

@router.delete("/{task_id}")
def delete_task(task_id:int):
    controller = taskcontroller.TaskController()
    task = controller.delete_task(task_id)

    if not task:
        return Response(content="NO_CONTENT", status_code=400)

    return Response(status_code=204)