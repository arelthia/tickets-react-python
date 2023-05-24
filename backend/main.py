from uuid import UUID
from fastapi import FastAPI, HTTPException
from models import Task, Priority, Update_Task
from typing import List

app = FastAPI()

db: List[Task] = [
    Task(
        id=UUID("4722832f-7f3a-4ba0-9588-5212db0ebc79"), 
        first_name="Arelthia",
        last_name="Phillips",
        email="arelthia@gmail.com",
        issue="I need to do the front and the back",
        priority=Priority.low
    ),
    Task(
        id=UUID("ab8434e6-c1d4-4bca-a3ff-68081d140f11"), 
        first_name="Denise",
        last_name="Harris",
        email="denise@gmail.com",
        issue="Hair needs to hold",
        priority=Priority.low
    )
]


@app.get("/")
def root():
    return {"Hello": "World"}

# Get all tickets
@app.get("/api/v1/tasks")
def get_tickets():
    return db

# Get one ticket by id
@app.get("/api/v1/tasks/{task_id}")
def get_ticket(task_id: UUID):
    for task in db:
        if task.id == task_id:
            return task
    raise HTTPException(
        status_code=404,
        detail=f"Task with id: {task_id} does not exist"
    )

# Create a new ticket
@app.post("/api/v1/tasks")
def create_ticket(task: Task):
    db.append(task)
    return {"id": task.id}

# Update ticket by id
@app.put("/api/v1/tasks/{task_id}")
def update_task(updated_task: Update_Task, task_id: UUID):
    for task in db:
        if task.id == task_id:
            if updated_task.first_name is not None:
                task.first_name = updated_task.first_name
            if updated_task.last_name is not None:
                task.last_name = updated_task.last_name  
            if updated_task.email is not None:
                task.email = updated_task.email 
            if updated_task.issue is not None:
                task.issue = updated_task.issue
            if updated_task.priority is not None:
                task.priority = updated_task.priority
            return task  
    raise HTTPException(
        status_code=404,
        detail=f"Task with id: {task_id} does not exist"
    )

# Delete 1 ticket by id
@app.delete("/api/v1/tasks/{task_id}")
def delete_task(task_id: UUID):
    for task in db:
        if task.id == task_id:
            db.remove(task)
            return
    raise HTTPException(
        status_code=404,
        detail=f"Task with id: {task_id} does not exist"
    )