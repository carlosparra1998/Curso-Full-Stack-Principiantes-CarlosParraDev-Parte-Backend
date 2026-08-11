from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.core.db import get_db
from .repository import TaskRepository

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.get("/")
def get_all_tasks(db : Session = Depends(get_db)):
    repository = TaskRepository(db)
    try:
        return repository.get_all_tasks()
    except SQLAlchemyError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Error en la base de datos')