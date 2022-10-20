from fastapi import HTTPException, status
from api.model.host_model import Host as HostModel
from api.schema.host_schema import Host, HostBase
from api.schema.user_schema import User
from api.model.user_model import User as UserModel
from api.service import auth_service, elasticSearch_service

def create_host(host: HostBase, current_user: User):
    get_host = HostModel.filter((HostModel.hostName == host.hostName) | (HostModel.hostIp == host.hostIp)).first()
    if get_host:
        msg = "Ip already registered"
        if get_host.hostName == host.hostName:
            msg = "Host name already registered"
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=msg
        )
    get_user = UserModel.get_by_id(current_user.id)
    db_host = HostModel(
        hostName=host.hostName,
        hostIp=host.hostIp,
        user=get_user
    )

    db_host.save()

    return Host(
        id = db_host.id,
        hostName = db_host.hostName,
        hostIp = db_host.hostIp,
        userId = db_host.user.id
    )

def update_host(host: Host):
    try:
        db_host = HostModel.get_or_none(id=host.id)
        db_host.hostName=host.hostName
        db_host.hostIp=host.hostIp
        db_host.save()
        return Host(
            id = db_host.id,
            hostName = db_host.hostName,
            hostIp = db_host.hostIp,
            userId = db_host.user.id
        )
    except Exception as ex:
        return ex

def delete_host(hostId: int):
    try:
        host_to_delete = HostModel.get_by_id(hostId)
        elasticSearch_service.deleteIndexApiAccess(host_to_delete.hostIp)
        host_to_delete.delete_instance(recursive=True)
        return "Host was deleted succesfully"
    except:
        return "The host delete failed"


def get_host_byid(hostId: int):
    try:
        db_host = HostModel.get_by_id(hostId)
        return Host(
            id = db_host.id,
            hostName = db_host.hostName,
            hostIp = db_host.hostIp,
            userId = db_host.user.id
        )
    except Exception as ex:
        return ex


def get_all_hosts():
    hostsList = []
    for h in HostModel.select():     
        host = Host(
            id = h.id, 
            hostName = h.hostName, 
            hostIp = h.hostIp, 
            userId = h.user.id,
        )
        hostsList.append(host)
    return hostsList
