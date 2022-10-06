from ast import Return
from re import S
from api.utils.snmpHandler_util import SnmpHandler
from pydantic import SecretStr
from api.model.optionsEnum_model import ChooseSnmpVersion
import subprocess 
import os

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