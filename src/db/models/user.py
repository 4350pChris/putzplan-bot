import orm
from ..config import models


class User(orm.Model):
    tablename = 'users'
    registry = models
    fields = {
        'id': orm.Integer(primary_key=True),
        'user_id': orm.String(max_length=24, unique=True)
    }
