from datetime import datetime
from pydantic import BaseModel

class ApiAccessModel(BaseModel):
    endpoint: str
    dateTimeDone: datetime
    user: str