from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.task import TaskORM
from .schemas import TaskPost

class TaskRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def get_all_tasks(self) -> List[TaskORM]:
        query = select(TaskORM)
        return self.db.execute(query).scalars().all()

    def get_task_by_id(self, task_id: int) -> Optional[TaskORM]:
        query = select(TaskORM).where(TaskORM.id == task_id)
        return self.db.execute(query).scalar_one_or_none()
  
    def create_task(self, task: TaskPost) -> TaskORM:
        task_obj = TaskORM(title= task.title, is_complete= task.is_complete)
        self.db.add(task_obj)
        self.db.flush()
        return task_obj

    def modify_task(self, task: TaskORM, updates: dict) -> TaskORM:
        for field, value in updates.items():
            setattr(task, field, value)
        
        self.db.add(task)        
        self.db.flush()
        return task