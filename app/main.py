from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI
from app.core.db import Base, engine
from app import models

def create_app() -> FastAPI:
    Base.metadata.create_all(bind=engine)
    app = FastAPI(title='My Tasks Backend')
    return app

app = create_app()

@app.get("/")
def ping():
    return {"msg" : "pong"}