from typing import List, Optional

from pydantic import BaseModel


class Animal(BaseModel):
    id: int
    name: str
    adopted: bool
    toys: "Optional[List[Toy]]"

    class Config:
        orm_mode = True


from pets.schemas.toy import Toy
Animal.update_forward_refs()
