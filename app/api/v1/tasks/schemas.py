from pydantic import BaseModel, ConfigDict

class TaskGet(BaseModel):
    id: int
    title: str
    is_complete: bool
    model_config = ConfigDict(from_attributes=True)