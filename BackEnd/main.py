from fastapi import FastAPI
from api.router.elasticSearch_router import elasticSearch_router
from api.router.vmOperations_router import vmOperations_router
from api.router.user_route import user_router
from api.router.esStatus_router import esStatus_router
from api.router.checksHandler_router import checksHandler_router
from api.router.host_router import host_router

app = FastAPI()

app.include_router(checksHandler_router)
app.include_router(elasticSearch_router)
app.include_router(vmOperations_router)
app.include_router(user_router)
app.include_router(esStatus_router)
app.include_router(host_router)
