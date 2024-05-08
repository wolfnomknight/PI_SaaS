from os.path import join
from os import listdir, getcwd
from contextlib import asynccontextmanager

import pandas as pd
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

plants = {'excaulebur': None, 'totosa': None}

def get_plant_data(plant):
    df = pd.concat([get_file_data(file, plant) for file in listdir(f'{getcwd()}\\data')])
    return df.sort_values(by=['Data', 'Hora']).to_json(orient='records')

def get_file_data(file, plant):
    if file.split('_')[0] == plant.title():
        with open(join('data', file)) as f:
            df = pd.read_csv(f, encoding='unicode_escape', engine='python')
            df['Data'] = file.split('.')[0][-10:]
            return df[['Valor do sinal', 'Temperatura', 'Umidade', 'Data', 'Hora']]

@asynccontextmanager
async def lifespan(app: FastAPI):
    for plant in plants.keys():
        plants[plant] = get_plant_data(plant)
    yield

app = FastAPI(lifespan=lifespan)

templates = Jinja2Templates(directory='templates')

@app.get('/', response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(request=request, name='index.html')

@app.get('/test')
def test():
    return {'hello': 'world'}

@app.get('/plants/{plant}')
def get_plant(plant):
    return plants.get(plant)