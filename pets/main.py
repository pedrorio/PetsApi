import fastapi
import uvicorn
from pets import controller, views, config, models

api = fastapi.FastAPI()


@api.on_event("startup")
async def startup():
    await config.Database.connect()


@api.on_event("shutdown")
async def shutdown():
    await config.Database.disconnect()


def configure():
    models.Common.create_all(config.Engine)
    api.include_router(views.home.router)
    api.include_router(controller.animal.router)
    api.include_router(controller.weather.router)


def start():
    uvicorn.run(api)


configure()
if __name__ == "__main__":
    start()
