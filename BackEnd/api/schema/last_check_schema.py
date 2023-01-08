from datetime import datetime
from pydantic import BaseModel
from pydantic import Field
from api.schema.host_schema import Host

from api.schema.user_schema import User


class LastCheck(BaseModel):
  
    host: Host = Field(
        ...,
        example="nombredetuhost"
    )
    ping: str = Field(
        ...,
        example="UP"
    )
    cpuUsage: str = Field(
        ...,
        example="45.21 %"
    )
    cpuName: str = Field(
        ...,
        example="Intel core i7"
    )
    ramUsed: str = Field(
        ...,
        example="8 GB"
    )
    ramFree: str = Field(
        ...,
        example=" 4 GB"
    )
    ramCached: str = Field(
        ...,
        example="2 GB"
    )
    netIn: str = Field(
        ...,
        example="4.3 MB"
    )
    netOut: str = Field(
        ...,
        example="4.52 MB"
    )

    timestamp: datetime = Field(
        ...,
        example=datetime.now()
    )
