from urllib.request import Request
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from api.router.elasticSearch_router import elasticSearch_router
from api.router.user_route import user_router
from api.router.esStatus_router import esStatus_router
from api.router.checks_handler_router import checksHandler_router
from api.router.host_router import host_router
from api.utils.exception_handler_util import HandlerGeneralException

app = FastAPI()

app.include_router(checksHandler_router)
app.include_router(elasticSearch_router)
app.include_router(user_router)
app.include_router(esStatus_router)
app.include_router(host_router)

async def exception_handler_general(request: Request, ex: HandlerGeneralException):
    return JSONResponse(
        status_code=500,
        content={"message": f"{ex.detail}"}
    )

app.add_exception_handler(HandlerGeneralException, exception_handler_general)