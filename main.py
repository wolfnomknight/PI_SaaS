from os import listdir
from os.path import join, dirname, abspath
from contextlib import asynccontextmanager

import pandas as pd
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

plants = {'excaulebur': None, 'totosa': None}

# def get_plant_data(plant):
#     df = pd.concat([get_file_data(file, plant) for file in listdir(join(dirname(abspath(__file__)), 'data'))])
#     return df.sort_values(by=['Data', 'Hora']).to_json(orient='records')

# def get_file_data(file, plant):
#     if file.split('_')[0] == plant.title():
#         with open(join(dirname(abspath(__file__)), 'data', file), 'r') as f:
#             df = pd.read_csv(f, encoding='unicode_escape', engine='python')
#             df['Data'] = file.split('.')[0][-10:]
#             return df[['Valor do sinal', 'Temperatura', 'Umidade', 'Data', 'Hora']]

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     for plant in plants.keys():
#         plants[plant] = get_plant_data(plant)
#     yield

# app = FastAPI(lifespan=lifespan)

app = FastAPI()

@app.on_event("startup")
def startup_event():
    for plant in plants.keys():
        plants[plant] = pd.read_csv(join(dirname(abspath(__file__))), 'data', f'{plant.title()}.csv', encoding='unicode_escape', engine='python').sort_values(by=['Data', 'Hora']).to_json(orient='records')

templates = Jinja2Templates(directory='templates')

@app.get('/', response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(request=request, name='index.html')

@app.get('/test')
def test():
    return {
        'hello': 'world', 'dir': listdir(join(dirname(abspath(__file__)), 'data')), 
        # 'excaulebur': get_file_data('Excaulebur_2024-04-04.csv', 'excaulebur')
    }

@app.get('/plants/{plant}')
def get_plant(plant):
    return pd.read_csv(join(dirname(abspath(__file__))), 'data', f'{plant.title()}.csv', encoding='unicode_escape', engine='python').sort_values(by=['Data', 'Hora']).to_json(orient='records')

# plants.get(plant)

# @app.get('/plants/{plant}/data')
# def get_data(plant):
#     return get_plant_data(plant)

# @app.get('/plants/{plant}/{file}')
# def get_data(plant, file):
#     return get_file_data(file, plant)