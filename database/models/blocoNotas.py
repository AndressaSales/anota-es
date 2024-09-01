from peewee import Model, CharField, TextField, DateTimeField
from database.database import db
import datetime

class bancoNotas(Model):
    nome = CharField()
    text = TextField()
    time = DateTimeField(default = datetime.datetime.now)

    class Meta:
        database = db
