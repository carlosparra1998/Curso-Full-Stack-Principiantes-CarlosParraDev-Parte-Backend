from typing import List

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
    
    def create_task(self, task: TaskPost) -> TaskORM:
        task_obj = TaskORM(title= task.title, is_complete= task.is_complete)
        self.db.add(task_obj)
        self.db.flush()
        return task_obj