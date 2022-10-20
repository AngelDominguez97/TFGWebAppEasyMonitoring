from http.client import HTTPException
from wsgiref.validate import IteratorWrapper
from pydantic import SecretStr
from pysnmp.entity.rfc3413.oneliner import cmdgen
from pysnmp.hlapi import SnmpEngine, UdpTransportTarget, ContextData, ObjectType, ObjectIdentity, getCmd
from pysnmp.hlapi import UsmUserData, usmHMACMD5AuthProtocol, usmDESPrivProtocol

from api.utils.settings import EnvVariables

envVariables = EnvVariables()

class SnmpHandler:

    # snmpwalk -v 2c -c EM-TFG IP OID
    def getInfoSnmpV2(ip: str, oid: str):
        try:
            global envVariables
            auth = cmdgen.CommunityData(envVariables.ro_comm)
            cmdGen = cmdgen.CommandGenerator()
            errorIndication, errosStatus, errorIndex, varBinds = cmdGen.getCmd(auth, cmdgen.UdpTransportTarget((ip, 161)), cmdgen.MibVariable(oid), lookupMib=False)
            if errorIndication:
                return errorIndication
            response = []
            for oid, val in varBinds:
                response.append(val.prettyPrint())
            return response
        except Exception as ex:
            raise HTTPException(status_code=500, detail=ex)

    # snmpwalk -v 3 -l authPriv -u user -a SHA -A EM-TFG-auth -x AES -X EM-TFG-priv IP OID
    def getInfoSnmpV3(ip: str, oid: str):
        try:
            global envVariables
            prueba = envVariables.user_snmp_v3
            auth = UsmUserData(
                userName=envVariables.user_snmp_v3, 
                authKey=envVariables.auth_snmp_v3, 
                authProtocol=usmHMACMD5AuthProtocol, 
                privKey=envVariables.priv_snmp_v3, 
                privProtocol=usmDESPrivProtocol
            )
            iterator = getCmd(
                SnmpEngine(), 
                auth, 
                UdpTransportTarget((ip, 161)), 
                ContextData(), 
                ObjectType(ObjectIdentity(oid))
            )
            errorIndication, errosStatus, errorIndex, varBinds = next(iterator)
            if errorIndication:
                return errorIndication
            response = []
            for oid, val in varBinds:
                response.append(val.prettyPrint())
            return response
        except Exception as ex:
            raise HTTPException(status_code=500, detail=ex)
