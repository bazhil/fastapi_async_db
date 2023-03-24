from typing import List
from fastapi import FastAPI, status, HTTPException
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

    return {**article.dict(), 'id':last_record_id}

@app.get('/articles/', response_model=List[ArticleSchema])
async def get_articles():
    query = Article.select()
    return await database.fetch_all(query=query)


@app.get('/articles/{id}', response_model=ArticleSchema)
async def get_details(id: int):
    query = Article.select().where(id==Article.c.id)
    myarticle = await database.fetch_one(query=query)

    if not myarticle:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, details='Article does not found')

    return {**myarticle}


@app.put('/articles/{id}', response_model=ArticleSchema)
async def update_article(id: int, article: ArticleSchemaIn):
    query = Article.update().where(Article.c.id==id).values(title=article.title, description=article.description)
    await database.execute(query)

    return {**article.dict(), 'id': id}


@app.delete('/articles/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_article(id: int):
    query = Article.delete().where(Article.c.id==id)
    await database.execute(query)

    return {'Message': 'Article deleted'}