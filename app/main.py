from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
app = FastAPI(
    title="Descargador Personal",
    version="1.0.0"
)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")

@app.get("/")
def inicio(request: Request):
    return templates.TemplateResponse(
        request=request,
        name='index.html',
        context={}
    )