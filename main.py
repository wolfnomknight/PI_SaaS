import os
import json
import uvicorn
from dotenv import load_dotenv
from jinja2.utils import markupsafe
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware


load_dotenv()
debug = os.getenv('DEBUG', False)


def render_bundle():
    manifest = json.load(open('static/manifest.json'))
    imports = [
        f'<script type="module" src="/static/{manifest[file]["file"]}"></script>' if 'js' in file
        else f'<link rel="stylesheet" type="text/css" href="/static/{manifest[file]["file"]}"/>' if 'css' in file
        else '' for file in manifest
    ]
    return markupsafe.Markup('\n'.join(filter(None, imports)))


app = FastAPI()
app.mount('/static', StaticFiles(directory='static'), name='static')
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.get("/", response_class=HTMLResponse)
def homepage(request: Request):
    return (
        Jinja2Templates(directory='back/templates', auto_reload=debug)
        .TemplateResponse('index.html', {'request': request, 'debug': debug, 'render_bundle': render_bundle})
    )


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=debug)
