from datetime import datetime
import peewee
from api.utils.operations_util import Utils


from api.utils.db import db

class User(peewee.Model):
    email = peewee.CharField(unique=True, index=True)
    username = peewee.CharField(unique=True, index=True)
    name = peewee.CharField()
    surname = peewee.CharField()
    registerDate = peewee.DateTimeField(default=datetime.now)
    updateDate = peewee.DateTimeField(default=datetime.now)
    userRole = peewee.CharField(default="user")
    password = peewee.CharField()

    class Meta:
        database = db