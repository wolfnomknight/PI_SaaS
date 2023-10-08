from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from uvicorn import run

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def homepage(request: Request):
    return Jinja2Templates(directory="src/templates").TemplateResponse(
        "index.html", {"request": request}
    )

if __name__ == "__main__":
    run("main:app", host="127.0.0.1", port=8000, reload=True)
