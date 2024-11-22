from typing import Optional
from pydantic import BaseModel

class SandwichBase(BaseModel):
    sandwich_name: str
    price: float

class SandwichCreate(SandwichBase):
    pass

class SandwichUpdate(BaseModel):
    sandwich_name: Optional[str] = None
    price: Optional[float] = None

class Sandwich(SandwichBase):
    id: int

    class Config:
        from_attributes  = True