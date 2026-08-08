from pydantic import BaseModel


class TodoCreate(BaseModel):
    title: str
    description: str
    status: bool = False


class TodoUpdate(BaseModel):
    title: str
    description: str
    status: bool
