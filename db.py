from sqlalchemy import Column, Integer, MetaData, String, Table, create_engine
from databases import Database

DATABASE_URL = 'postgresql://home:123456@localhost/articles_db'

engine = create_engine(DATABASE_URL)
metadata = MetaData()

Article = Table(
    'article',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String(100)),
    Column('description', String(500))
)

database = Database(DATABASE_URL)