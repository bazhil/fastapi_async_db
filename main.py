from fastapi import FastAPI, status
from db import metadata, database, engine, Article
from schemas import ArticleSchemaIn, ArticleSchema


metadata.create_all(engine)

app = FastAPI()

@app.on_event('startup')
async def startup():
    await database.connect()


@app.on_event('shutdown')
async def startup():
    await database.disconnect()


@app.post('/articles/', status_code=status.HTTP_201_CREATED, response_model=ArticleSchema)
async def add_article(article: ArticleSchemaIn):
    query = Article.insert().values(title=article.title, description=article.description)
    last_record_id = await database.execute(query)

    return {**article.dict, 'id': last_record_id}

@app.get('/articles/')
async def get_article():
    return {'message': 'Hello World!'}
