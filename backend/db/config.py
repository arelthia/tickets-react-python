import os
# Import dotenv
from dotenv import load_dotenv
load_dotenv() 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
DATABASE_URL = "postgresql://{}:{}@localhost:5432/{}".format(os.getenv('DB_USERNAME'),os.getenv('DB_PASSWORD'),os.getenv('DB_NAME'))

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

