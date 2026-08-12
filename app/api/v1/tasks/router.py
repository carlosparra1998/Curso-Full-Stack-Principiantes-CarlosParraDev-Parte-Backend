from typing import List

from fastapi import APIRouter, Body, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.core.db import get_db
from .repository import TaskRepository
from .schemas import TaskGet, TaskPost

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.get("/", response_model=List[TaskGet], status_code=status.HTTP_200_OK)
def get_all_tasks(db : Session = Depends(get_db)):
    repository = TaskRepository(db)
    try:
        return repository.get_all_tasks()
    except SQLAlchemyError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Error en la base de datos')

@router.post("/", response_model=TaskGet, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskPost = Body(...), db : Session = Depends(get_db)):
    repository = TaskRepository(db)
    try:
        task_obj = repository.create_task(task=task)
        db.commit()
        db.refresh(task_obj)
        return task_obj
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Error en la base de datos')