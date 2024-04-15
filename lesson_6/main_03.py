from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str = Field(..., title='Name', max_length=50)
    price: float = Field(..., title='Price', gt=0, le=100_000)
    description: str = Field(default=None, title='Description', max_length=1000)
    tax: float = Field(0, title='Tax', ge=0, le=10)


class User(BaseModel):
    username: str = Field(title='Username', min_length=3, max_length=50)
    full_name: str = Field(None, title='Full Name', min_length=3, max_length=100)
