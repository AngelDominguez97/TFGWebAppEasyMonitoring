from enum import unique
import peewee
from datetime import datetime
from api.model.user_model import User

from api.utils.db import db

class Host(peewee.Model):
    hostName = peewee.CharField(unique=True)
    hostIp = peewee.CharField(unique=True)
    user = peewee.ForeignKeyField(User, backref='hosts')
    registerDate = peewee.DateTimeField(default=datetime.now)
    updateDate = peewee.DateTimeField(default=datetime.now)

    class Meta:
        database = db