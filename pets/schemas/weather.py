from pydantic import BaseModel


class Weather(BaseModel):
    bring_umbrella: bool
    temperature: float
    category: str
