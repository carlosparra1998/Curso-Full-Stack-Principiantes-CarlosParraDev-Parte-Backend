from typing import List

from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.task_priority import TaskPriorityORM
from .schemas import TaskPriorityPost

class TaskPriorityRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def get_all_task_priorities(self) -> List[TaskPriorityORM]:
        query = select(TaskPriorityORM)
        return self.db.execute(query).scalars().all()

    def create_task_priority(self, priority: TaskPriorityPost) -> TaskPriorityORM:
        object = TaskPriorityORM(name= priority.name, order= priority.order)
        self.db.add(object)
        self.db.flush()
        return object