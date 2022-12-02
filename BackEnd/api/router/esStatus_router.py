from fastapi import Depends, status
from fastapi import APIRouter
from api.schema import user_schema
from api.service import auth_service, esStatus_service

esStatus_router = APIRouter(prefix="/api/esStatus")

@esStatus_router.get(
    "/getEsClusterStatus/",
    tags=["esStatus"], 
    status_code=status.HTTP_200_OK,
    summary="Function for get the status about the elastic search cluster"
)
def getEsClusterStatus(current_user: user_schema.User = Depends(auth_service.get_current_user)):
    response = esStatus_service.getEsClusterStatus()
    return response

@esStatus_router.get(
    "/getEsClusterHealth/",
    tags=["esStatus"], 
    status_code=status.HTTP_200_OK,
    summary="Function for get the general info about the elastic search culster status"
)
def getEsClusterHealth(current_user: user_schema.User = Depends(auth_service.get_current_user)):
    response = esStatus_service.getEsClusterHealth()
    return response