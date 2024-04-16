# Задание №2.
# Создать веб-приложение на FastAPI, которое будет предоставлять API для работы с базой данных пользователей.
# Пользователь должен иметь следующие поля:
# ○ ID (автоматически генерируется при создании пользователя)
# ○ Имя (строка, не менее 2 символов)
# ○ Фамилия (строка, не менее 2 символов)
# ○ Дата рождения (строка в формате "YYYY-MM-DD")
# ○ Email (строка, валидный email)
# ○ Адрес (строка, не менее 5 символов)
# API должен поддерживать следующие операции:
# ○ Добавление пользователя в базу данных
# ○ Получение списка всех пользователей в базе данных
# ○ Получение пользователя по ID
# ○ Обновление пользователя по ID
# ○ Удаление пользователя по ID
# Приложение должно использовать базу данных SQLite3 для хранения пользователей.

from typing import List

import databases
import sqlalchemy
from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr, PastDate
from faker import Faker
from datetime import date

DATABASE_URL = 'sqlite:///seminar_6_1.db'

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

app = FastAPI()
fake = Faker()

users = sqlalchemy.Table(
    'users',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('firstname', sqlalchemy.String(50)),
    sqlalchemy.Column('lastname', sqlalchemy.String(50)),
    sqlalchemy.Column('birthday', sqlalchemy.Date()),
    sqlalchemy.Column('email', sqlalchemy.String(50)),
    sqlalchemy.Column('address', sqlalchemy.String(80)),
)


class UserIn(BaseModel):
    firstname: str = Field(..., title="Name", description="Define name", min_length=2, max_length=50)
    lastname: str = Field(..., title="Last Name", description="Define last name", min_length=2, max_length=50)
    birthday: PastDate = Field(..., title="Birthday", description="Define birthday")
    email: EmailStr = Field(..., title="Email", description="Define email", min_length=8, max_length=32)
    address: str = Field(..., title="Address", description="Define address", min_length=5, max_length=80)


class User(UserIn):
    id: int


@app.on_event('startup')
async def startup():
    await database.connect()


@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()


engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)


@app.get('/fake_users/{count}')
async def create_fake_users(count: int):
    for i in range(count):
        query = users.insert().values(
            firstname=fake.first_name(),
            lastname=fake.last_name(),
            email=fake.email(),
            address=fake.address(),
            birthday=fake.date_between_dates(
                date_start=date(1970, 1, 1),
                date_end=date(1995, 1, 1)))
        await database.execute(query)
    return {'message': f'{count} Users created successfully'}


@app.get('/users/', response_model=List[User])
async def get_users():
    query = users.select()
    return await database.fetch_all(query)


@app.get('/users/{user_id}', response_model=User)
async def get_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query)


@app.post('/users/', response_model=User)
async def create_user(user: UserIn):
    query = users.insert().values(**user.dict())
    user_id = await database.execute(query)
    return {**user.dict(), 'id': user_id}


@app.put('/users/{user_id}', response_model=User)
async def update_user(user_id: int, user: User):
    query = users.update().where(users.c.id == user_id).values(**user.dict())
    await database.execute(query)
    updated_user = await get_user(user_id)
    return updated_user, {'message': f'{user_id} was updated successfully'}


@app.delete('/users/{user_id}')
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {'message': f'User {user_id} was deleted'}
