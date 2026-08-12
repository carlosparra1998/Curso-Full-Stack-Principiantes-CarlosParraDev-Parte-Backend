from typing import Optional

from pydantic import BaseModel, ConfigDict

class TaskPriorityGet(BaseModel):
    id: int
    name: str
    order: int
    model_config = ConfigDict(from_attributes=True)

class TaskGet(BaseModel):
    id: int
    title: str
    is_complete: bool
    priority: Optional[TaskPriorityGet] = None
    model_config = ConfigDict(from_attributes=True)
    
class TaskPost(BaseModel):
    title: str
    is_complete: Optional[bool] = None
    priority_id: Optional[int] = None

class TaskPut(BaseModel):
    title: Optional[str] = None
    is_complete: Optional[bool] = None
    priority_id: Optional[int] = None
