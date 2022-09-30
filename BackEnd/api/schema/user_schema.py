from typing import Optional
from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr
from datetime import datetime


class UserBase(BaseModel):
    email: EmailStr = Field(
        ...,
        example="myemail@email.com"
    )
    username: str = Field(
        ...,
        min_length=3,
        max_length=50,
        example="MyTypicalUsername"
    )
    name: str = Field(
        ...,
        max_length=50,
        example="yourname"
    )
    surname: str = Field(
        ...,
        max_length=100,
        example="surname"
    )
    userRole: Optional[str]


class User(UserBase):

    id: int = Field(
        ...,
        example="5"
    )


class UserRegister(UserBase):
    password: str = Field(
        ...,
        min_length=8,
        max_length=64,
        example="strongpass"
    )