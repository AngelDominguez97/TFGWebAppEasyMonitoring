import json
from typing import Optional
from pydantic import SecretStr
from fastapi import APIRouter, status
from api.service import  statusDevice_service
from api.service import host_service
from api.model.optionsEnum_model import ChooseMinutes, ChooseSnmpVersion
from api.utils.settings import Oids
from api.utils.operations_util import Utils
from api.schema.host_schema import Host

checksHandler_router = APIRouter(prefix="/api/elasticSearch", tags=["elasticSearch"])
oids = Oids()


@checksHandler_router.post(
    "/checkAllDevices",
    tags=["checksHandler"],
    status_code=status.HTTP_202_ACCEPTED,
    summary="Raise the check For all devices available in the system"
)
def checkAllDevices():
    hosts = host_service.getAllHosts()
    return hosts
