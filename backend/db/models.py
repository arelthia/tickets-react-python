import db.config
from bson import ObjectId
from schematics.models import Model
from schematics.types import StringType


class Ticket(Model):
    id = StringType()
    first_name = StringType(required=True)
    last_name = StringType(required=True)
    email = StringType(required=True)
    issue = StringType(required=True)
    priority = StringType()




