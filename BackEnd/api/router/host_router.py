from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Body

from api.schema import user_schema
from api.schema import host_schema
from api.service import auth_service, host_service

from api.utils.db import get_db

from typing import List


host_router = APIRouter(prefix="/api", tags=["Hosts"])


@host_router.post(
    "/host/",
    status_code=status.HTTP_201_CREATED,
    response_model=host_schema.Host,
    dependencies=[Depends(get_db)],
    summary="Create a new host"
)
def create_host(host: host_schema.HostBase = Body(...), current_user: user_schema.User = Depends(auth_service.get_current_user)):
    """
    ## Create a new host in the app

    ### Args
    The app can recive next fields into a JSON
    - host name: A valid name for the host
    - host ip: Unique Ip for the device

    ### Returns
    - host: Host info
    """
    return host_service.create_host(host, current_user)


@host_router.post(
    "/host/update",
    status_code=status.HTTP_200_OK,
    response_model=host_schema.Host,
    dependencies=[Depends(get_db)],
    summary="Update an existing host"
)
def update_host(host: host_schema.Host = Body(...)):
    """
    ## Update a new host in the app

    ### Args
    The app can recive next fields into a JSON
    - host name: A new name for the host
    - host ip: Unique Ip for the device

    ### Returns
    - host: Host info
    """
    return host_service.update_host(host)


@host_router.delete(
    "/host/delete{hostId}",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)],
    summary="Delete an existing host"
)
def delete_host(hostId: str):
    """
    ## Delete one host in the app

    ### Args
    The app can recive next fields into a JSON
    - id: the id fo the host you want to delete

    ### Returns
    - host: Host info
    """
    return host_service.delete_host(hostId)


@host_router.get(
    "/host{hostId}",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)],
    summary="select an existing host by id"
)
def select_host(hostId: str):
    """
    ## Select one host in the app

    ### Args
    The app can recive next fields into a JSON
    - id: the id fo the host you want to select

    ### Returns
    - host: Host info
    """
    return host_service.get_host_byid(hostId)


@host_router.get(
    "/allhosts",
    status_code=status.HTTP_200_OK,
    response_model=List[host_schema.Host],
    dependencies=[Depends(get_db)],
    summary="Get all hosts in the database"
)
def get_all_users():
    """
    ## Get all hosts registered in the app

    ### Args
    NONE

    ### Returns
    - Json with all the hosts in the app
    """
    return host_service.get_all_hosts()