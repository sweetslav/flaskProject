# Задание №1.
# Разработать API для управления списком пользователей с использованием базы данных SQLite.
# Для этого создайте модель User со следующими полями:
# ○ id: int (идентификатор пользователя, генерируется автоматически)
# ○ username: str (имя пользователя)
# ○ email: str (электронная почта пользователя)
# ○ password: str (пароль пользователя)
# API должно поддерживать следующие операции:
# ○ Получение списка всех пользователей: GET /users/
# ○ Получение информации о конкретном пользователе: GET /users/{user_id}/
# ○ Создание нового пользователя: POST /users/
# ○ Обновление информации о пользователе: PUT /users/{user_id}/
# ○ Удаление пользователя: DELETE /users/{user_id}/
# Для валидации данных используйте параметры Field модели User.
# Для работы с базой данных используйте SQLAlchemy и модуль databases.

import databases
import sqlalchemy
from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr
from typing import List

DATABASE_URL = 'sqlite:///seminar_6.db'

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

app = FastAPI()

users = sqlalchemy.Table(
    'users',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('username', sqlalchemy.String(30)),
    sqlalchemy.Column('email', sqlalchemy.String(50)),
    sqlalchemy.Column('password', sqlalchemy.String(20)),
)


class UserIn(BaseModel):
    username: str = Field(..., title="Username", description="Define username", min_length=3, max_length=50)
    email: EmailStr = Field(..., title="Email", description="Define email", min_length=8, max_length=32)
    password: str = Field(..., title="Password", description="Define password", min_length=8, max_length=32)


class User(UserIn):
    id: int


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

metadata.create_all(engine)


@app.get('/fake_users/{count}')
async def create_note(count: int):
    for i in range(count):
        query = users.insert().values(username=f'user{i}', email=f'mail{i}@mail.ru', password=11111188 * i)
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
