import uvicorn
from fastapi import FastAPI

from app import tasks
from app.tasks import models, main
from app.database import engine


tasks.models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(tasks.main.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)