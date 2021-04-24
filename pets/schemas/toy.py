from typing import Optional

from pydantic import BaseModel
# from pets import schemas


class Toy(BaseModel):
    id: int
    name: str
    owner: "Optional[Animal]"

    class Config:
        orm_mode = True


from pets.schemas.animal import Animal
Toy.update_forward_refs()
