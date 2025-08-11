from fastapi import FastAPI
from models.api.api_responses import (
    StandardMessageResponse,
    MessageTypeEnum,
    )
from routers.auth_router import auth_router
from routers.talent_router import talent_router
from routers.user_router import user_router
from routers.campaign_router import campaign_router


def register_routes(app: FastAPI):
    @app.get("/alive", response_model=StandardMessageResponse[None] )
    def alive():
        respnse =  StandardMessageResponse(
            message_type= MessageTypeEnum.SUCCESS,
            text ="the server is  running",
            data=None,
        )
        return respnse
    app.include_router(router=auth_router)
    app.include_router(router=user_router)
    app.include_router(router=talent_router)
    app.include_router(router=campaign_router)
