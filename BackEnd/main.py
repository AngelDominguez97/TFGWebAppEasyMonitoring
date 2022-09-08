from fastapi import FastAPI
from api.router.esOperations_router import esOperations_router
from api.router.vmOperations_router import vmOperations_router
from api.router.user_route import user_router
from api.router.esStatus_router import esStatus_router

app = FastAPI()

app.include_router(esOperations_router)
app.include_router(vmOperations_router)
app.include_router(user_router)
app.include_router(esStatus_router)