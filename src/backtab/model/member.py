from pydantic import BaseModel


class Member(BaseModel):
    display_name: str
    name: str
    pin: int
