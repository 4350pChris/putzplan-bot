import orm
from ..config import models


class Room(orm.Model):
    tablename = 'rooms'
    registry = models
    fields = {
        'id': orm.Integer(primary_key=True),
        'name': orm.String(max_length=80)
    }
