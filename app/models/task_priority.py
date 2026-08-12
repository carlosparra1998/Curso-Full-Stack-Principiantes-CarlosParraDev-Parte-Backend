from typing import List

from sqlalchemy import Integer, String

from app.core.db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

class TaskPriorityORM(Base):
    __tablename__ = "task_priorities"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(20), index=True, nullable=False, unique=True)
    order: Mapped[int] = mapped_column(Integer, index=True, nullable=False)
    
    tasks: Mapped[List["TaskORM"]] = relationship("TaskORM", back_populates="priority")