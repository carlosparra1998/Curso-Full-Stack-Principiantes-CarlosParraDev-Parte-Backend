from typing import Optional

from pydantic import BaseModel, ConfigDict

class TaskGet(BaseModel):
    id: int
    title: str
    is_complete: bool
    model_config = ConfigDict(from_attributes=True)
    
class TaskPost(BaseModel):
    title: str
    is_complete: Optional[bool] = None
