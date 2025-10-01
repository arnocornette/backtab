from pydantic import BaseModel


class Price(BaseModel):
    member: float
    guest: float
