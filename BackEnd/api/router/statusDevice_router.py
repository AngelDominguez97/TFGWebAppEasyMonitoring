import json
from typing import Optional
from pydantic import SecretStr
from fastapi import APIRouter, status
from api.service import  statusDevice_service
from api.model.optionsEnum_model import ChooseMinutes, ChooseSnmpVersion
#from api.utils.settings import Oids
#from api.utils.operations_util import Operations_utils

statusDevice_router = APIRouter(prefix="/api/statusDevice")
#oids = Oids()

