from urllib.request import Request
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from api.router.elasticSearch_router import elasticSearch_router
from api.router.user_route import user_router
from api.router.esStatus_router import esStatus_router
from api.router.checks_handler_router import checksHandler_router
from api.router.host_router import host_router
from api.utils.scheduler_util import app as app_rocketry
from api.utils.exception_handler_util import HandlerGeneralException
from fastapi.middleware.cors import CORSMiddleware
import asyncio
import uvicorn

app = FastAPI()

app.include_router(checksHandler_router)
app.include_router(elasticSearch_router)
app.include_router(user_router)
app.include_router(esStatus_router)
app.include_router(host_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Server(uvicorn.Server):
    """Customized uvicorn.Server

    Uvicorn server overrides signals and we need to include
    Rocketry to the signals."""
    def handle_exit(self, sig: int, frame) -> None:
        app_rocketry.session.shut_down()
        return super().handle_exit(sig, frame)


async def main():
    "Run scheduler and the API"
    server = Server(config=uvicorn.Config(app, workers=1, loop="asyncio"))

    api = asyncio.create_task(server.serve())
    sched = asyncio.create_task(app_rocketry.serve())

    await asyncio.wait([sched, api])

if __name__ == "__main__":
    asyncio.run(main())



async def exception_handler_general(request: Request, ex: HandlerGeneralException):
    return JSONResponse(
        status_code=500,
        content={"message": f"{ex.detail}"}
    )

app.add_exception_handler(HandlerGeneralException, exception_handler_general)