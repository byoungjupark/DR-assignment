from typing import Optional, List
from fastapi import FastAPI, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from starlette.responses import Response

from app import models, schemas, crud
from app.database import engine, SessionLocal


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/task")
def create_task(task:schemas.TaskCreate, db:Session=Depends(get_db)):
    return crud.create_task(db=db, task=task)

@app.get("/task", response_model=List[schemas.Task])
def get_all_tasks(db:Session=Depends(get_db)):
    return crud.get_all_tasks(db=db)

@app.get("/task/{task_id}", response_model=schemas.Task)
def get_task(task_id:int, db:Session=Depends(get_db)):
    return crud.get_task(db=db, id=task_id)

@app.patch("/task/{task_id}")
def update_task(task_id:int, task:schemas.TaskUpdate, db:Session=Depends(get_db)):
    return crud.update_task(db=db, id=task_id, update_task=task)

@app.delete("/task")
def delete_all_tasks(db:Session=Depends(get_db)):
    return crud.delete_all_tasks(db=db)

@app.delete("/task/{task_id}")
def delete_task(task_id:int, db:Session=Depends(get_db)):
    return crud.delete_task(db=db, id=task_id)