from pydantic import BaseModel
from fastapi import Fields

class UserBase(BaseModel):
    username: str = Fields(..., example="ankur_goel_")
    email: str = Fields(..., example="ankurgoel.1822@gmail.com")
    password: str = Fields(..., example = "xyz195@")

class UserDisplay(BaseModel):
    username: str
    email: str
