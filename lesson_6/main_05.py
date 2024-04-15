import databases
import sqlalchemy
from fastapi import FastAPI

DATABASE_URL = 'sqlite:///main_05.db'
# DATABASE_URL = 'postgresql://user:password@localhost/dbname'

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

...

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
