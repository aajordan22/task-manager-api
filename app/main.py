from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()
tasks = {}
counter = 1

@app.get("/health")
def health_check():
    return {"status" : "ok"}

class TaskCreate(BaseModel):
    title: str
    description: str
    priority: str


@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    global counter
    new_task = {"id" : counter, "title" : task.title, "description" : task.description, "priority" : task.priority, "completed" : False}
    tasks[counter] = new_task
    counter += 1
    return new_task