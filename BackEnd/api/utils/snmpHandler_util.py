from wsgiref.validate import IteratorWrapper
from pysnmp.entity.rfc3413.oneliner import cmdgen
from pysnmp.hlapi import SnmpEngine, UdpTransportTarget, ContextData, ObjectType, ObjectIdentity, getCmd
from pysnmp.hlapi import UsmUserData, usmHMACSHAAuthProtocol, usmAesCfb256Protocol

class SnmpHandler:

    def getInfoSnmpV2(snmp_ro_comm: str, ip: str, oid: str):
        auth = cmdgen.CommunityData(snmp_ro_comm)
        cmdGen = cmdgen.CommandGenerator()
        errorIndication, errosStatus, errorIndex, varBinds = cmdgen.getCmd(auth, cmdgen.UdpTransportTarget(ip, 161), cmdgen.MibVariable(oid), lookupMib=False)
        if errorIndication:
            return errorIndication
        response = []
        for oid, val in varBinds:
            response.append(val.prettyPrint())
        return response

    def getInfoSnmpV3(ip: str, oid: str, userv3: str, authpass: str, privpass: str):
        auth = UsmUserData(userName=userv3, authKey=authpass, authProtocol=usmHMACSHAAuthProtocol, privKey=privpass, privProtocol=usmAesCfb256Protocol)
        iterator = getCmd(SnmpEngine(), auth, UdpTransportTarget(ip, 161), ContextData(), ObjectType(ObjectIdentity(oid)))
        errorIndication, errosStatus, errorIndex, varBinds = next(iterator)
        if errorIndication:
            return errorIndication
        response = []
        for oid, val in varBinds:
            response.append(val.prettyPrint())
        return response