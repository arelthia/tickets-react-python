from sqlalchemy import  Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base
from db.config import engine
Base = declarative_base()


class Ticket(Base):
    __tablename__ ="tickets"

    id = Column(UUID(as_uuid=True), primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    issue = Column(String, nullable=False)
    priority = Column(String)




Base.metadata.create_all(engine)