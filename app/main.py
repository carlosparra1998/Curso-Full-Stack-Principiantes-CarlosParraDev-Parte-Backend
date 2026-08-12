from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI
from app.core.db import Base, engine
from app import models
from app.api.v1.tasks.router import router as task_router
from app.api.v1.task_priority.router import router as task_priority_router

def create_app() -> FastAPI:
    Base.metadata.create_all(bind=engine)
    app = FastAPI(title='My Tasks Backend')
    app.include_router(task_router)
    app.include_router(task_priority_router)
    return app

app = create_app()

@app.get("/")
def ping():
    return {"msg" : "pong"}