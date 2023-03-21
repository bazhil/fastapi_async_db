from fastapi import FastAPI
from db import metadata, database, engine


metadata.create_all(engine)

app = FastAPI()

@app.on_event('startup')
async def startup():
    await database.connect()


@app.on_event('shutdown')
async def startup():
    await database.disconnect()


@app.get('/articles')
async def get_article():
    return {'message': 'Hello World!'}
