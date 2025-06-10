from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import date
from typing import List

app = FastAPI()

class TodoCreate(BaseModel):
    name: str
    description: str
    date: date

class Todo(TodoCreate):
    id: int

todos: List[Todo] = []
next_id = 1

@app.post("/todos/", response_model=Todo)
def create_todo(todo: TodoCreate):
    global next_id

    # Check for duplicates
    for existing in todos:
        if (
            existing.name == todo.name and
            existing.description == todo.description and
            existing.date == todo.date
        ):
            raise HTTPException(
                status_code=400,
                detail="Duplicate ToDo entry"
            )

    new_todo = Todo(id=next_id, **todo.dict())
    todos.append(new_todo)
    next_id += 1
    return new_todo


@app.get("/todos/", response_model=List[Todo])
def get_todos():
    return todos

@app.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="ToDo not found")

@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, updated: TodoCreate):
    for i, todo in enumerate(todos):
        if todo.id == todo_id:
            new_todo = Todo(id=todo_id, **updated.dict())
            todos[i] = new_todo
            return new_todo
    raise HTTPException(status_code=404, detail="ToDo not found")

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for i, todo in enumerate(todos):
        if todo.id == todo_id:
            del todos[i]
            return {"detail": "ToDo deleted"}
    raise HTTPException(status_code=404, detail="ToDo not found")
