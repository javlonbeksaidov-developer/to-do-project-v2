from fastapi import APIRouter

from app.database import delete, insert, select, update
from app.schemas import TodoCreate, TodoUpdate

router = APIRouter()


@router.get("/todos")
def get_todos():
    data = select()
    return data


@router.post("/todos")
def create_todo(todo: TodoCreate):
    print(todo)
    insert(todo.title, todo.description, todo.status)
    return {"message": "created"}


@router.put("/todos/{id}")
def update_todo(id: int, todo: TodoUpdate):
    print(todo)
    update(id, todo.title, todo.description, todo.status)
    return {"message": "updated"}


@router.delete("/todos/{id}")
def delete_todo(id: int):
    delete(id)
    return {"message": "deleted"}
