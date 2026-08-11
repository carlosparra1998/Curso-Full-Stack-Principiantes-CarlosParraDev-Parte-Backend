from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Boolean, Integer, String
from app.core.db import Base

class TaskORM(Base):
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(100), index=True, nullable=False)
    is_complete: Mapped[bool] = mapped_column(Boolean, default=False, index=True, nullable=False)