from typing import List

from fastapi import APIRouter, Body, Depends, status, HTTPException
from .schemas import TaskPriorityGet, TaskPriorityPost
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.core.db import get_db
from .repository import TaskPriorityRepository

router = APIRouter(prefix="/task-priorities", tags=["task-priorities"])

@router.get("/", response_model=List[TaskPriorityGet], status_code=status.HTTP_200_OK)
def get_all_task_priorities(db: Session = Depends(get_db)):
    repository = TaskPriorityRepository(db)
    try:
        return repository.get_all_task_priorities()
    except SQLAlchemyError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Error en la base de datos')
        
@router.post("/", response_model=TaskPriorityGet, status_code=status.HTTP_201_CREATED)
def create_task_priority(task_priority: TaskPriorityPost = Body(...), db : Session = Depends(get_db)):
    repository = TaskPriorityRepository(db)
    try:
        previous_obj = repository.get_task_priority_by_name(task_priority.name)
        if previous_obj:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Ya existe una prioridad con ese nombre')
        
        object = repository.create_task_priority(priority=task_priority)
        db.commit()
        db.refresh(object)
        return object
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Error en la base de datos')