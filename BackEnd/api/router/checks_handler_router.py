import json
from typing import Optional
from pydantic import SecretStr
from fastapi import APIRouter, status
from api.model.lastCheck_model import LastCheck as LastCheckModel
from api.schema.last_check_schema import LastCheck
from api.service import snmp_checks_service 
from api.service import host_service
from api.model.optionsEnum_model import ChooseMinutes, ChooseSnmpVersion
from api.utils.settings import Oids

checksHandler_router = APIRouter(prefix="/api/checksHandler", tags=["checksHandler"])
oids = Oids()


@checksHandler_router.post(
    "/checkAllDevices",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Raise the check For all devices available in the system"
)
def checkAllDevices(snmpVersion: ChooseSnmpVersion):
    hosts = host_service.get_all_hosts()
    for h in hosts:
        #ping = snmp_checks_service.getPingStatusByIp(h.hostIp)
        cpuUsage = snmp_checks_service.getInfoDeviceByIpAndOid(oids.CPU_AVERAGE_1M, h.hostIp, snmpVersion)
    return hosts
