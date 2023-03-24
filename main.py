from fastapi import FastAPI
from db import metadata, database, engine
from articles import router


metadata.create_all(engine)

app = FastAPI()

@app.on_event('startup')
async def startup():
    await database.connect()


@app.on_event('shutdown')
async def startup():
    await database.disconnect()


app.include_router(router)