from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()

# @app.get("/", response_class=HTMLResponse)
# def main(request: Request):
#     return Jinja2Templates(directory="src/templates").TemplateResponse(
#         "index.html", {"request": request}
#     )
@app.get("/")
def main():
    return ("""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>PI</title>
</head>
<body>
  <div>hello world</div>
</body>
</html>""")

# if __name__ == "__main__":
#     uvicorn.run("main:app", host="127.0.0.1", port=8000)