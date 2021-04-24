import orm

from pets import config
from pets.models.common import Common


class Animal(orm.Model):
    __tablename__ = "animals"
    __database__ = config.Database
    __metadata__ = Common

    id = orm.Integer(primary_key=True)
    name = orm.String(max_length=100)
    adopted = orm.Boolean(default=False)
