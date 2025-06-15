from fastapi import FastAPI, HTTPException
from models import TodoItem

app = FastAPI()

# In-memory DB
todo_list = []

@app.get("/")
def home():
    return {"message": "Welcome to Todo API"}

@app.get("/todos")
def get_todos():
    return todo_list

@app.post("/todos")
def add_todo(todo: TodoItem):
    todo_list.append(todo)
    return {"message": "Todo added", "todo": todo}

@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated: TodoItem):
    for index, item in enumerate(todo_list):
        if item.id == todo_id:
            todo_list[index] = updated
            return {"message": "Todo updated", "todo": updated}
    raise HTTPException(status_code=404, detail="Todo not found")

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for index, item in enumerate(todo_list):
        if item.id == todo_id:
            del todo_list[index]
            return {"message": "Todo deleted"}
    raise HTTPException(status_code=404, detail="Todo not found")