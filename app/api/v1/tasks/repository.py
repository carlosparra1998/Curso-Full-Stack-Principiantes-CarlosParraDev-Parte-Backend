from typing import List

from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.task import TaskORM

class TaskRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def get_all_tasks(self) -> List[TaskORM]:
        query = select(TaskORM)
        return self.db.execute(query).scalars().all()