import os
# Import dotenv
from dotenv import load_dotenv
load_dotenv() 
from pymongo import MongoClient
## may not need serapi
from pymongo.server_api import ServerApi

uri = os.getenv('DB_URI')

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client["supportdb"]
collection = db["tickets"]
