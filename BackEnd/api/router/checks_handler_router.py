import json
from fastapi import APIRouter, Depends, status
from api.schema import user_schema
from api.schema.last_check_schema import LastCheck
from api.service import auth_service, snmp_checks_service 
from api.service import host_service
from api.model.optionsEnum_model import ChooseSnmpVersion
from api.utils.settings import Oids

checksHandler_router = APIRouter(prefix="/api/checksHandler", tags=["checksHandler"])
oids = Oids()


@checksHandler_router.post(
    "/checkAllDevices",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Raise the check For all devices available in the system"
)
async def checkAllDevices(snmpVersion: ChooseSnmpVersion, current_user: user_schema.User = Depends(auth_service.get_current_user)):

    await snmp_checks_service.check_all_devices(snmpVersion)   
    return "Todos los checks se han realizado correctamente"

@checksHandler_router.post(
    "/checkCpuDevice",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Raise the check for cpu in a specific device"
)
def checkCpuDevice(snmpVersion: ChooseSnmpVersion, hostId: int, current_user: user_schema.User = Depends(auth_service.get_current_user)):
    host = host_service.get_host_byid(hostId)
    newCpuUsage = snmp_checks_service.getInfoDeviceByIpAndOid(oids.CPU_AVERAGE_1M, host.hostIp, snmpVersion)
    return newCpuUsage

@checksHandler_router.post(
    "/checkRamDevice",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Raise the check for ram in a specific device"
)
def checkRamDevice(snmpVersion: ChooseSnmpVersion, hostId: int, current_user: user_schema.User = Depends(auth_service.get_current_user)):
    host = host_service.get_host_byid(hostId)
    newRamUsed = snmp_checks_service.getInfoDeviceByIpAndOid(oids.RAM_USED, host.hostIp, snmpVersion)
    newRamFree = snmp_checks_service.getInfoDeviceByIpAndOid(oids.RAM_FREE, host.hostIp, snmpVersion)
    newRamCached = snmp_checks_service.getInfoDeviceByIpAndOid(oids.RAM_CACHED, host.hostIp, snmpVersion)
    return (newRamUsed, newRamFree, newRamCached)

@checksHandler_router.post(
    "/checkNetDevice",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Raise the check for net in a specific device"
)
def checkNetDevice(snmpVersion: ChooseSnmpVersion, hostId: int, current_user: user_schema.User = Depends(auth_service.get_current_user)):
    host = host_service.get_host_byid(hostId)
    newNetIn = snmp_checks_service.getInfoDeviceByIpAndOid(oids.NET_TRAFFIC_IN_1M, host.hostIp, snmpVersion)
    newNetOut = snmp_checks_service.getInfoDeviceByIpAndOid(oids.NET_TRAFFIC_OUT_1M, host.hostIp, snmpVersion)
    return (newNetIn, newNetOut)


@checksHandler_router.get(
    "/getallchecks",
    status_code=status.HTTP_202_ACCEPTED,
    summary="get all the last checks available"
)
def checkNetDevice(current_user: user_schema.User = Depends(auth_service.get_current_user)):
    last_checks = snmp_checks_service.get_all_last_checks()
    last_checks_final = []
    for lc in last_checks:
        last_checks_final.append({
            "hostName": lc.host.hostName,
            "hostIp": lc.host.hostIp,
            "ping": lc.ping,
            "cpuUsage": lc.cpuUsage,
            "cpuName": lc.cpuName,
            "ramUsed": lc.ramUsed,
            "ramFree": lc.ramFree,
            "ramCached": lc.ramCached,
            "netIn": lc.netIn,
            "netOut": lc.netOut
        })
    return last_checks_final