from typing import List

import fastapi

from pets import schemas, services

router = fastapi.APIRouter()


@router.get('/api/animal/{id}', response_model=schemas.Animal)
async def find_one_animal_by_id(id: int):
    return await services.animal.get_animal(id)


@router.get('/api/animals', response_model=List[schemas.Animal])
async def find_all_animals():
    return await services.animal.get_animals()

@router.post('/api/animals')
async def create_one_animal(animal: schemas.Animal):
    return await services.animal.create_animal(animal)