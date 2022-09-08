from urllib import response
from fastapi import APIRouter
from fastapi import status
from api.service import esOperations_service
from api.model.esOperations_model import ApiAccessModel

esOperations_router = APIRouter(prefix="/api/EsOperations")

@esOperations_router.post(
    "/indexApiAccess/",
    tags=["esOperations"],
    status_code=status.HTTP_201_CREATED,
    summary="Insert every access that any user make to an API function"
)
def indexApiAccess(data: ApiAccessModel):
    response = esOperations_service.insertApiAccess(data)
    return response


@esOperations_router.get(
    "/getApiAccessByid{id}/",
    tags=["esOperations"],
    status_code=status.HTTP_202_ACCEPTED,
    summary="Getting an index from elastic search using an id"
)   
def getApiAccessByid(id: str):
    response = esOperations_service.getApiAccessByid(id)
    return response

@esOperations_router.get(
    "/refreshApiAccess/",
    tags=["esOperations"],
    status_code=status.HTTP_202_ACCEPTED,
    summary="Refresh an index from elastic search"
)   
def refreshApiAccess(index: str):
    response = esOperations_service.refreshApiAccess(index)
    return response

@esOperations_router.get(
    "/searchAllApiAccess/",
    tags=["esOperations"],
    status_code=status.HTTP_202_ACCEPTED,
    summary="Search all the items by an index from elastic search"
) 
def searchAllApiAccess(index: str):
    response = esOperations_service.searchAllApiAccess(index)
    return response

@esOperations_router.get(
    "/searchApiAccessByUser/",
    tags=["esOperations"],
    status_code=status.HTTP_200_OK,
    summary="Update an existing document from an index"
) 
def searchApiAccessByUser(user: str):
    response = esOperations_service.searchApiAccessByUser(user)
    return response

@esOperations_router.post(
    "/updateApiAccessByid/",
    tags=["esOperations"],
    status_code=status.HTTP_202_ACCEPTED,
    summary="Update an existing document from an index"
) 

def updateApiAccessByid(id: str, index: str, data: ApiAccessModel):
    response = esOperations_service.updateApiAccessByid(id, index, data)
    return response

@esOperations_router.delete(
    "/deleteDocumentAccess/",
    tags=["esOperations"],
    status_code=status.HTTP_200_OK,
    summary="Delete an existing document"
) 
def deleteDocumentAccess(id: str):
    response = esOperations_service.deleteDocumentApiAccess(id)
    return response

@esOperations_router.delete(
    "/deleteIndexAccess/",
    tags=["esOperations"],
    status_code=status.HTTP_200_OK,
    summary="Delete an existing index"
) 
def deleteIndex(index: str):
    response = esOperations_service.deleteIndex(index)
    return response