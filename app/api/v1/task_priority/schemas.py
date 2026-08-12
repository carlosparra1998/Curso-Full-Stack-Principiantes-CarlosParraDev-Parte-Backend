from pydantic import BaseModel, ConfigDict, field_validator

class TaskPriorityGet(BaseModel):
    id: int
    name: str
    order: int
    model_config = ConfigDict(from_attributes=True)
    
class TaskPriorityPost(BaseModel):
    name: str
    order: int
    
    @field_validator("name")
    @classmethod
    def normalize_name(cls, value: str) -> str:
        return value.strip().upper()