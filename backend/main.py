from uuid import UUID
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pymongo import ReturnDocument
from models import Task, Update_Ticket
from db.config import collection
from db.models import Ticket
from bson import ObjectId

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

@app.get("/")
def root():
    return {"Hello": "World"}

# Get all tickets - or filter by priority
@app.get("/api/v1/tickets")
async def get_tickets(priority: str | None = None):
    tickets=[]
    if priority:
        tasks = collection.find({"priority": priority})
    else:
        tasks = collection.find({})

    for ticket in list(tasks):
        tickets.append(
            {
                "id": str(ticket["_id"]),
                "first_name": ticket["first_name"],
                "last_name" : ticket["last_name"],
                "email" : ticket["email"],
                "issue": ticket["issue"],
                "priority": ticket["priority"]
            }
        )

    if len(tickets) > 0:    
        return tickets
    raise HTTPException(
        status_code=404,
        detail=f"No tickets found"
    )



# Get one ticket by id
@app.get("/api/v1/tickets/{ticket_id}")
async def get_ticket(ticket_id: str):
    ticket = collection.find_one({"_id": ObjectId(ticket_id)})
    found_ticket = {
                "id": str(ticket["_id"]),
                "first_name": ticket["first_name"],
                "last_name" : ticket["last_name"],
                "email" : ticket["email"],
                "issue": ticket["issue"],
                "priority": ticket["priority"]
            }
    return found_ticket

# Create a new ticket
@app.post("/api/v1/tickets")
async def create_ticket(task: Task):
    ticket = Ticket()
    ticket.first_name = task.first_name
    ticket.last_name = task.last_name
    ticket.email = task.email
    ticket.issue = task.issue
    ticket.priority = task.priority
    result = collection.insert_one(dict(ticket))
    return {"id": str(result.inserted_id)}


# Update ticket by id
@app.put("/api/v1/tickets/{ticket_id}")
async def update_ticket(ticket_update: Update_Ticket, ticket_id: str):
    ticket = {}
    if ticket_update.first_name is not None:
        ticket["first_name"] = ticket_update.first_name
    if ticket_update.last_name is not None:
        ticket["last_name"] = ticket_update.last_name  
    if ticket_update.email is not None:
        ticket["email"] = ticket_update.email 
    if ticket_update.issue is not None:
        ticket["issue"] = ticket_update.issue
    if ticket_update.priority is not None:
        ticket["priority"] = ticket_update.priority
    updated_ticket = collection.find_one_and_update({"_id": ObjectId(ticket_id)}, {'$set': ticket}  ,return_document = ReturnDocument.AFTER)
    
    if updated_ticket:
        return {
                "id": str(updated_ticket["_id"]),
                "first_name": updated_ticket["first_name"],
                "last_name" : updated_ticket["last_name"],
                "email" : updated_ticket["email"],
                "issue": updated_ticket["issue"],
                "priority": updated_ticket["priority"]
            }
    raise HTTPException(
        status_code=404,
        detail=f"Ticket with id: {ticket_id} does not exist"
    )
    

# Delete 1 ticket by id
@app.delete("/api/v1/tickets/{ticket_id}")
async def delete_ticket(ticket_id: str):
    deleted_ticket = collection.find_one_and_delete({"_id": ObjectId(ticket_id)})
    if deleted_ticket is not None:
        return {"message": "Ticket deleted"}
    
    raise HTTPException(
        status_code=404,
        detail=f"Ticket with id: {ticket_id} does not exist"
    )
    