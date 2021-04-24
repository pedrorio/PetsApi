from typing import Optional

from pydantic import BaseModel


class Location(BaseModel):
    city: str
    country: str = 'pt'
    state: Optional[str] = None
