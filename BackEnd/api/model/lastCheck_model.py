import peewee
from datetime import datetime
from api.model.host_model import Host

from api.utils.db import db

class LastCheck(peewee.Model):
    host = peewee.ForeignKeyField(Host, backref='lastCheck')
    ping = peewee.CharField()
    cpuUsage = peewee.CharField()
    cpuName = peewee.CharField()
    ramUsed = peewee.CharField()
    ramFree = peewee.CharField()
    ramCached = peewee.CharField()
    netIn = peewee.CharField()
    netOut = peewee.CharField()

    class Meta:
        database = db