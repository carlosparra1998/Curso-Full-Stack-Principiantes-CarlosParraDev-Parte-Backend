from typing import List

from fastapi import APIRouter, Body, Depends, HTTPException, Path, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.core.db import get_db
from .repository import TaskRepository
from .schemas import TaskGet, TaskPost, TaskPut

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

@router.put("/{task_id}", response_model=TaskGet, status_code=status.HTTP_200_OK)
def modify_task(task_id: int = Path(..., ge=1), task: TaskPut = Body(...), db : Session = Depends(get_db)):
    repository = TaskRepository(db)
    try:
        task_obj = repository.get_task_by_id(task_id=task_id)
        if not task_obj:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No existe una tarea con ese id')
        
        updates = task.model_dump(exclude_unset=True)
        task_obj = repository.modify_task(task_obj, updates)
        db.commit()
        db.refresh(task_obj)
        return task_obj
    
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Error en la base de datos')

@router.delete("/{task_id}", status_code=status.HTTP_200_OK)
def delete_task(task_id: int = Path(..., ge=1), db : Session = Depends(get_db)):
    repository = TaskRepository(db)
    try:
        task_obj = repository.get_task_by_id(task_id=task_id)
        if not task_obj:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No existe una tarea con ese id')
        
        repository.delete_task(task_obj)
        db.commit()
        return
    
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Error en la base de datos')