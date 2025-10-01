from pydantic import BaseModel


class Config(BaseModel):
    data: str
    host: str
    port: int
    slowdown: int
