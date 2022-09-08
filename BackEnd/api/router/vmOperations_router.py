from fastapi import status
from fastapi import Depends
from fastapi import APIRouter
from api.service import vmOperations_service
from api.service.auth_service import get_current_user

vmOperations_router = APIRouter(prefix="/api/VmOperations")

@vmOperations_router.post(
    "/rebootMachineByIP/",
    tags=["vmOperations"],  
    status_code=status.HTTP_200_OK,
    summary="Reboot the specified virtual machine by an Ip"
)
def rebootMachineByIP(ip: str):
    response = vmOperations_service.rebootMachineByIP(ip)
    return response

@vmOperations_router.get(
    "/getCPUInfo/",
    tags=["vmOperations"], 
    status_code=status.HTTP_200_OK,
    summary="Function for get the CPU info of the system"
)
def getCPUInfo():
    response = vmOperations_service.getCPUInfo()
    return response

@vmOperations_router.get(
    "/getMemmoryInfo/",
    tags=["vmOperations"], 
    status_code=status.HTTP_200_OK,
    summary="Function for get the Memmory info of the system"
)
def getMemmoryInfo():
    response = vmOperations_service.getMemmoryInfo()
    return response

@vmOperations_router.get(
    "/getDiskInfo/",
    tags=["vmOperations"], 
    status_code=status.HTTP_200_OK,
    summary="Function for get the Disk info of the system"
)
def getDiskInfo():
    response = vmOperations_service.getDiskInfo()
    return response

@vmOperations_router.get(
    "/getNetworkInfo/",
    tags=["vmOperations"],
    status_code=status.HTTP_200_OK,
    summary="Function for get the Network info of the system"
)
def getNetworkInfo():
    response = vmOperations_service.getNetworkInfo()
    return response
