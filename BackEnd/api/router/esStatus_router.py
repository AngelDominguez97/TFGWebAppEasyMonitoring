from fastapi import status
from fastapi import APIRouter
from api.service import esStatus_service

esStatus_router = APIRouter(prefix="/api/esStatus")

@esStatus_router.get(
    "/getEsClusterStatus/",
    tags=["esStatus"], 
    status_code=status.HTTP_200_OK,
    summary="Function for get the status about the elastic search cluster"
)
def getEsClusterStatus():
    response = esStatus_service.getEsClusterStatus()
    return response

@esStatus_router.get(
    "/getEsClusterHealth/",
    tags=["esStatus"], 
    status_code=status.HTTP_200_OK,
    summary="Function for get the general info about the elastic search culster status"
)
def getEsClusterHealth():
    response = esStatus_service.getEsClusterHealth()
    return response