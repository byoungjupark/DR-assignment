from pydantic import BaseModel, root_validator

class TaskCommandCreate(BaseModel):
    name: str
    completed: bool

    @root_validator
    def is_validated_request(cls, values):
        name, completed = values.get('name'), values.get('completed')
        if not name or not str(completed):
            raise ValueError("INVALIDATED")
        return values
