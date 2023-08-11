from pydantic import BaseModel



class Task(BaseModel):
    task_id: str 
    title: str
    complete:bool

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "task_id": "64cfd2d26e5e4b91d60ee8ac",
                "title": "My important task",
                "complete": True,
            }
        }

class UpdateTask(BaseModel):
    complete: bool

    class Config:
        json_schema_extra = {
            "example": {
                "complete": True,
            }
        }
