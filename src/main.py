from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def homepage(request: Request):
    return Jinja2Templates(directory="templates").TemplateResponse(
        "index.html", {"request": request}
    )
