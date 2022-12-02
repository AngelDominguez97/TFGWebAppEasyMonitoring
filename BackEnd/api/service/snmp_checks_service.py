from api.schema.host_schema import Host
from api.service import elasticSearch_service, host_service
from api.utils.settings import Oids
from api.utils.snmpHandler_util import SnmpHandler
from api.model.optionsEnum_model import ChooseSnmpVersion
from api.model.lastCheck_model import LastCheck as LastCheckModel
from api.schema.last_check_schema import LastCheck
import subprocess 

oids = Oids()


def getInfoDeviceByIpAndOid(oid: str, ip: str, snmpVersion: ChooseSnmpVersion):
    if snmpVersion == "v2c":
        return SnmpHandler.getInfoSnmpV2(ip, oid)
    elif snmpVersion == "v3":
        return SnmpHandler.getInfoSnmpV3(ip, oid)

def getPingStatusByIp(ip: str):
    command = ['ping', '-c', '1', ip]
    response = subprocess.call(command) == 0
    if response:
        return "UP"
    else:
        return "DOWN"

def insertLastCheck(lastCheck: LastCheck):
    check_to_udpate = LastCheckModel.get_or_none(host = lastCheck.host.id)
    if check_to_udpate:
        check_to_udpate.ping = lastCheck.ping
        check_to_udpate.cpuUsage = lastCheck.cpuUsage
        check_to_udpate.cpuName = lastCheck.cpuName
        check_to_udpate.ramUsed = lastCheck.ramUsed
        check_to_udpate.ramFree = lastCheck.ramFree
        check_to_udpate.ramCached = lastCheck.ramCached
        check_to_udpate.netIn = lastCheck.netIn
        check_to_udpate.netOut = lastCheck.netOut
        check_to_udpate.save() 
    else:
        db_lastCheck = LastCheckModel(
            host = lastCheck.host,
            ping = lastCheck.ping,
            cpuUsage = lastCheck.cpuUsage,
            cpuName = lastCheck.cpuName,
            ramUsed = lastCheck.ramUsed,
            ramFree = lastCheck.ramFree,
            ramCached = lastCheck.ramCached,
            netIn = lastCheck.netIn,
            netOut = lastCheck.netOut,
        )
        db_lastCheck.save()
    return lastCheck

async def check_all_devices(snmpVersion: ChooseSnmpVersion):
    hosts = host_service.get_all_hosts()
    for h in hosts:
        newping = getPingStatusByIp(h.hostIp)
        if newping == "UP":
            newCpuUsage = getInfoDeviceByIpAndOid(oids.CPU_AVERAGE_1M, h.hostIp, snmpVersion)
            newCpuName = getInfoDeviceByIpAndOid(oids.CPU_NAME, h.hostIp, snmpVersion)
            newRamUsed = getInfoDeviceByIpAndOid(oids.RAM_USED, h.hostIp, snmpVersion)
            newRamFree = getInfoDeviceByIpAndOid(oids.RAM_FREE, h.hostIp, snmpVersion)
            newRamCached = getInfoDeviceByIpAndOid(oids.RAM_CACHED, h.hostIp, snmpVersion)
            newNetIn = getInfoDeviceByIpAndOid(oids.NET_TRAFFIC_IN_1M, h.hostIp, snmpVersion)
            newNetOut = getInfoDeviceByIpAndOid(oids.NET_TRAFFIC_OUT_1M, h.hostIp, snmpVersion)
            lastCheck = LastCheck(
                host=h,
                ping=newping,
                cpuUsage=newCpuUsage[0],
                cpuName=newCpuName[0],
                ramUsed=newRamUsed[0],
                ramFree=newRamFree[0],
                ramCached=newRamCached[0],
                netIn=newNetIn[0],
                netOut=newNetOut[0]
            )
            # Aqui insertariamos los datos en el indice (IP) de elastic de cada host
            elasticSearch_service.insert_last_check(lastCheck)
            insertLastCheck(lastCheck)
        elif newping == "DOWN":
            newCpuUsage = "0"
            newCpuName = "0"
            newRamUsed = "0"
            newRamFree = "0"
            newRamCached = "0"
            newNetIn = "0"
            newNetOut = "0"
            lastCheck = LastCheck(
                host=h,
                ping=newping,
                cpuUsage=newCpuUsage,
                cpuName=newCpuName,
                ramUsed=newRamUsed,
                ramFree=newRamFree,
                ramCached=newRamCached,
                netIn=newNetIn,
                netOut=newNetOut
            )
            # Aqui insertariamos los datos en el indice (IP) de elastic de cada host
            elasticSearch_service.insert_last_check(lastCheck)
            insertLastCheck(lastCheck)

def get_all_last_checks():
    last_check_list = []
    for lc in LastCheckModel.select():     
        last_check = LastCheck(
            host = Host(
                id = lc.host.id, 
                hostName = lc.host.hostName, 
                hostIp = lc.host.hostIp, 
                userId = lc.host.user.id,
            ),
            ping = lc.ping,
            cpuUsage = lc.cpuUsage,
            cpuName = lc.cpuName,
            ramUsed = lc.ramUsed,
            ramFree = lc.ramFree,
            ramCached = lc.ramCached,
            netIn = lc.netIn,
            netOut = lc.netOut
        )
        last_check_list.append(last_check)
    return last_check_list