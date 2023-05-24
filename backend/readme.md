
# Ticket Class
- id
- first_name
- last_name
- email
- issue
- priority - low, medium, high

# priority enum


# Routes
| Type | Route | DEscription |
| --- | ---  | ---         |
| GET  | /tickets | Get all tickets|
| GET  | /tickets/{id} | Get one ticket by id|
| POST | /tickets  | Create a new ticket|
| PUT  | /tickets/{id} | Update ticket by id |
| DELETE | /tickets/{id} | Delete 1 ticket by id |


## Setup
1. Install virtual environment `python -m venv .venv`
1. Activate the virtual environment
    windows `.venv/Scripts/Activate.ps1`
    mac `source .venv/bin/activate`

    > Note: on windows may need to run `Set-ExecutionPolicy Unrestricted -Scope Process`
1. Install fastapi and uvicorn `pip3 install fastapi "uvicorn[standard]"`
1. Run app `uvicorn main:app --reload`

