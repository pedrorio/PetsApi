import fastapi
import orm

from pets import models, schemas


async def get_animals():
    return await models.Animal.objects.all()


async def get_animal(id: int):
    try:
        return await models.Animal.objects.get(id=id)
    except orm.exceptions.NoMatch:
        raise fastapi.HTTPException(status_code=404)


async def create_animal(animal: schemas.Animal):
    await models.Animal.objects.create(name=animal.name, adopted=animal.adopted)
