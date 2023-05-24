from typing import Optional
from uuid import UUID, uuid4
'''
 pydantic enforces type hints at runtime, and 
 provides user friendly errors when data is invalid.
'''
from pydantic import BaseModel 
from enum import Enum

class Priority(str, Enum):
    low = "low" 
    medium = "medium"
    high = "high"

class Task(BaseModel):
    first_name: str
    last_name: str
    email: str
    issue: str
    priority: Optional[Priority]=Priority.low

class Update_Ticket(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    issue: Optional[str]
    priority: Optional[Priority]