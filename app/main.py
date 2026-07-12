from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.controllers.home_controller import router as home_router
from app.controllers.download_controller import router as download_router

app = FastAPI(
    title="Descargador Personal",
    version="1.0.0"
)

app.mount(
    "/static", StaticFiles(directory="app/static"), 
    name="static"
    )

app.include_router(home_router)
app.include_router(download_router)