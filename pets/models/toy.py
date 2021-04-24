import orm

from pets import config
from pets.models.animal import Animal
from pets.models.common import Common


class Toy(orm.Model):
    __tablename__ = "toys"
    __database__ = config.Database
    __metadata__ = Common

    id = orm.Integer(primary_key=True)
    name = orm.String(max_length=100)
    owner = orm.ForeignKey(Animal)
