from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


# @app.get("/", response_class=HTMLResponse)
# def main(request: Request):
#     return Jinja2Templates(directory="src/templates").TemplateResponse(
#         "index.html", {"request": request}
#     )
@app.get("/")
def main():
    html = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>PI</title>
</head>
<body>
  <div>hello world</div>
</body>
</html>"""
    return HTMLResponse(html)
