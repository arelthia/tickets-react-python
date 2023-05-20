from uuid import UUID
from fastapi import FastAPI, HTTPException
from models import Task, Priority, Update_Task
from typing import List
from db.models import Ticket
# import db.config
from db.config import session


app = FastAPI()


@app.get("/")
def root():
    return {"Hello": "World"}

# Get all tickets
@app.get("/api/v1/tickets")
async def get_tickets():
    tickets = session.query(Ticket)
    return tickets.all()

# Get one ticket by id
@app.get("/api/v1/tickets/{ticket_id}")
async def get_ticket(ticket_id: UUID):
    task = session.query(Ticket).filter(Ticket.id == ticket_id).first()
    if task is not None:
        return task
    raise HTTPException(
        status_code=404,
        detail=f"Task with id: {ticket_id} does not exist"
    )


# Create a new ticket
@app.post("/api/v1/tickets")
async def create_ticket(task: Task):
    ticket = Ticket(
        id = task.id,
        first_name = task.first_name,
        last_name = task.last_name,
        email = task.email,
        issue = task.issue,
        priority = task.priority
    )
    session.add(ticket)
    session.commit()
    return {"id": ticket.id}

# Update ticket by id
@app.put("/api/v1/tickets/{ticket_id}")
async def update_task(updated_task: Update_Task, ticket_id: UUID):
    task = session.query(Ticket).filter(Ticket.id == ticket_id).first()
    if task is not None:
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
        session.add(task)
        session.commit()   
        return {"message":"Update successful"}
    raise HTTPException(
        status_code=404,
        detail=f"Task with id: {ticket_id} does not exist"
    )

# Delete 1 ticket by id
@app.delete("/api/v1/tickets/{ticket_id}")
async def delete_task(ticket_id: UUID):
    task = session.query(Ticket).filter(Ticket.id == ticket_id).first()
    if task is not None:
        session.delete(task)
        session.commit()
        return {"message": "Delete Successful"}
    raise HTTPException(
        status_code=404,
        detail=f"Task with id: {ticket_id} does not exist"
    )
    