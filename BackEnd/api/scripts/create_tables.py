from api.model.host_model import Host
from api.model.lastCheck_model import LastCheck
from api.model.user_model import User

from api.utils.db import db

def create_tables():
    with db:
        db.create_tables([LastCheck])