from atexit import register
from typing import Optional
from pydantic import BaseModel
from pydantic import Field

from api.schema.user_schema import User


class HostBase(BaseModel):
 
    hostName: str = Field(
        ...,
        example="nombredetuhost"
    )
    hostIp: str = Field(
        ...,
        example="127.0.0.1"
    )
    

class Host(HostBase):

    id: int = Field(
        ...,
        example="5"
    )

    userId:  int = Field(
        ...,
        example="2"
    )
