from urllib import response
from fastapi import APIRouter
from fastapi import status
from api.service import elasticSearch_service
from api.model.elasticSearch_model import ApiAccessModel

elasticSearch_router = APIRouter(prefix="/api/elasticSearch", tags=["elasticSearch"])

@elasticSearch_router.post(
    "/indexApiAccess/",
    status_code=status.HTTP_201_CREATED,
    summary="Insert every access that any user make to an API function"
)
def indexApiAccess(data: ApiAccessModel):
    response = elasticSearch_service.insertApiAccess(data)
    return response


@elasticSearch_router.get(
    "/getApiAccessByid{id}/",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Getting an index from elastic search using an id"
)   
def getApiAccessByid(id: str):
    response = elasticSearch_service.getApiAccessByid(id)
    return response

@elasticSearch_router.get(
    "/refreshApiAccess/",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Refresh an index from elastic search"
)   
def refreshApiAccess(index: str):
    response = elasticSearch_service.refreshApiAccess(index)
    return response

@elasticSearch_router.get(
    "/searchAllApiAccess/",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Search all the items by an index from elastic search"
) 
def searchAllApiAccess(index: str):
    response = elasticSearch_service.searchAllApiAccess(index)
    return response

@elasticSearch_router.get(
    "/searchApiAccessByUser/",
    status_code=status.HTTP_200_OK,
    summary="Update an existing document from an index"
) 
def searchApiAccessByUser(user: str):
    response = elasticSearch_service.searchApiAccessByUser(user)
    return response

@elasticSearch_router.post(
    "/updateApiAccessByid/",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Update an existing document from an index"
) 

def updateApiAccessByid(id: str, index: str, data: ApiAccessModel):
    response = elasticSearch_service.updateApiAccessByid(id, index, data)
    return response

@elasticSearch_router.delete(
    "/deleteDocumentAccess/",
    status_code=status.HTTP_200_OK,
    summary="Delete an existing document"
) 
def deleteDocumentAccess(id: str):
    response = elasticSearch_service.deleteDocumentApiAccess(id)
    return response

@elasticSearch_router.delete(
    "/deleteIndexAccess/",
    status_code=status.HTTP_200_OK,
    summary="Delete an existing index"
) 
def deleteIndex(index: str):
    response = elasticSearch_service.deleteIndex(index)
    return response