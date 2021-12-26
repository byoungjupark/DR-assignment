import uvicorn
from fastapi import FastAPI

from app.database import db

import app
from app.router import task



app.DAO.models.Base.metadata.create_all(bind=db.engine)

app = FastAPI()

app.include_router(task.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)