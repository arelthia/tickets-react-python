from uuid import UUID
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import Ticket, Priority, Update_Ticket
from typing import List

app = FastAPI()

# origins = [
#     "http://localhost:3000/",
# ]

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


db: List[Ticket] = [
    Ticket(
        id=UUID("4722832f-7f3a-4ba0-9588-5212db0ebc79"), 
        first_name="Arelthia",
        last_name="Phillips",
        email="arelthia@gmail.com",
        issue="I need to do the front and the back",
        priority=Priority.low
    ),
    Ticket(
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
@app.get("/api/v1/tickets")
def get_tickets():
    return db

# Get one ticket by id
@app.get("/api/v1/tickets/{ticket_id}")
def get_ticket(ticket_id: UUID):
    for task in db:
        if task.id == ticket_id:
            return task
    raise HTTPException(
        status_code=404,
        detail=f"Task with id: {ticket_id} does not exist"
    )

# Create a new ticket
@app.post("/api/v1/tickets")
def create_ticket(task: Ticket):
    db.append(task)
    return {"id": task.id}

# Update ticket by id
@app.put("/api/v1/tickets/{ticket_id}")
def update_task(updated_ticket: Update_Ticket, ticket_id: UUID):
    for task in db:
        if task.id == ticket_id:
            if updated_ticket.first_name is not None:
                task.first_name = updated_ticket.first_name
            if updated_ticket.last_name is not None:
                task.last_name = updated_ticket.last_name  
            if updated_ticket.email is not None:
                task.email = updated_ticket.email 
            if updated_ticket.issue is not None:
                task.issue = updated_ticket.issue
            if updated_ticket.priority is not None:
                task.priority = updated_ticket.priority
            return task  
    raise HTTPException(
        status_code=404,
        detail=f"Task with id: {ticket_id} does not exist"
    )

# Delete 1 ticket by id
@app.delete("/api/v1/tickets/{ticket_id}")
def delete_task(ticket_id: UUID):
    for task in db:
        if task.id == ticket_id:
            db.remove(task)
            return
    raise HTTPException(
        status_code=404,
        detail=f"Task with id: {ticket_id} does not exist"
    )