import json
import pytest
from models import Task
from fastapi.testclient import TestClient
from unittest import mock

from main import app, get_tickets

client = TestClient(app)

@pytest.fixture
def mock_collection():
    return mock.Mock()

def test_get_tickets_without_priority(mock_collection):
    mock_collection.find.return_value = [
        {
            "_id": "64695007d0adeed0e8e82e8f",
            "first_name": "James",
            "last_name": "Brown",
            "email": "jbrown@gmail.com",
            "issue": "Create the hello world",
            "priority": "high"
        },
        {
            "_id": "646951461efd01b4f28668c6",
            "first_name": "Stormy",
            "last_name": "Green",
            "email": "stormy@gmail.com",
            "issue": "Let it go let it go",
            "priority": "low"
        },
        {
            "_id": "64695a3b013f2f99a17972f1",
            "first_name": "Karla",
            "last_name": "Allen",
            "email": "karla.allen@gmail.com",
            "issue": "distracted by the world",
            "priority": "medium"
        }
    ]

    with mock.patch("main.collection", mock_collection):
        response = client.get("/api/v1/tickets")

    assert response.status_code == 200
    assert response.json() == [
        {
            "id": "64695007d0adeed0e8e82e8f",
            "first_name": "James",
            "last_name": "Brown",
            "email": "jbrown@gmail.com",
            "issue": "Create the hello world",
            "priority": "high"
        },
        {
            "id": "646951461efd01b4f28668c6",
            "first_name": "Stormy",
            "last_name": "Green",
            "email": "stormy@gmail.com",
            "issue": "Let it go let it go",
            "priority": "low"
        },
        {
            "id": "64695a3b013f2f99a17972f1",
            "first_name": "Karla",
            "last_name": "Allen",
            "email": "karla.allen@gmail.com",
            "issue": "distracted by the world",
            "priority": "medium"
        }
    ]



def test_get_tickets_with_priority(mock_collection):
    mock_collection.find.return_value = [
        {
            "_id": "64695007d0adeed0e8e82e8f",
            "first_name": "James",
            "last_name": "Brown",
            "email": "jbrown@gmail.com",
            "issue": "Create the hello world",
            "priority": "high"
        }
    ]

    with mock.patch("main.collection", mock_collection):
        response = client.get("/api/v1/tickets?priority=high")

    assert response.status_code == 200
    assert response.json() == [
        {
            "id": "64695007d0adeed0e8e82e8f",
            "first_name": "James",
            "last_name": "Brown",
            "email": "jbrown@gmail.com",
            "issue": "Create the hello world",
            "priority": "high"
        }
    ]



def test_get_tickets_with_invalid_priority(mock_collection):
    mock_collection.find.return_value = []

    with mock.patch("main.collection", mock_collection):
        response = client.get("/api/v1/tickets?priority=Invalid")

    assert response.status_code == 404
    assert response.json() == {
        "detail": "No tickets found"
    }


def test_get_ticket_with_valid_id(mock_collection):  
    mock_collection.find_one.return_value = {
            "_id": "64695007d0adeed0e8e82e8f",
            "first_name": "James",
            "last_name": "Brown",
            "email": "jbrown@gmail.com",
            "issue": "Create the hello world",
            "priority": "high"
        }
    

    with mock.patch("main.collection", mock_collection):
        response = client.get("/api/v1/tickets/64695007d0adeed0e8e82e8f") 

    assert response.status_code == 200 
    assert response.json() == {
            "id": "64695007d0adeed0e8e82e8f",
            "first_name": "James",
            "last_name": "Brown",
            "email": "jbrown@gmail.com",
            "issue": "Create the hello world",
            "priority": "high"
        } 



def test_create_ticket(mock_collection): 
    mock_insert_one = mock_collection.insert_one
    mock_insert_one.return_value = mock.MagicMock()
    mock_insert_one.return_value.inserted_id = "64695007d0adeed0e8e82e8f"
    
    task = Task(
        first_name="John", 
        last_name="Doe", 
        email="john.doe@example.com", 
        issue="Bug", 
        priority="high")
    
    with mock.patch("main.collection", mock_collection):
        response = client.post("/api/v1/tickets", json=task.__dict__) 
        response_data = response.json()
    assert response_data["id"] == '64695007d0adeed0e8e82e8f'

def test_update_ticket(mock_collection):
    mock_collection.find_one_and_update.return_value = {
        "_id": "64695007d0adeed0e8e82e8f",
        "first_name": "James",
        "last_name": "Brown",
        "email": "jbrown@gmail.com",
        "issue": "Done one thing",
        "priority": "high"
    }

    task = Task(
        first_name="James", 
        last_name="Brown", 
        email="jbrown@gmail.com", 
        issue="Done one thing", 
        priority="high")

    with mock.patch("main.collection", mock_collection):
        response = client.put("/api/v1/tickets/64695007d0adeed0e8e82e8f", json=task.__dict__) 

    assert response.status_code == 200
    assert response.json() == {
        "id": "64695007d0adeed0e8e82e8f",
        "first_name": "James",
        "last_name": "Brown",
        "email": "jbrown@gmail.com",
        "issue": "Done one thing",
        "priority": "high"
    }    

def test_delete_ticket(mock_collection):
    mock_collection.find_one_and_delete.return_value = {
        "message": "Ticket deleted"
    }    

    with mock.patch("main.collection", mock_collection):
        response = client.delete("/api/v1/tickets/64695007d0adeed0e8e82e8f")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Ticket deleted"
    }

