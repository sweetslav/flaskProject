# Задание №3-7.
# Создать API для добавления нового пользователя в базу данных.
# Приложение должно иметь возможность принимать POST запросы с данными нового пользователя и сохранять их в базу данных.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс User с полями id, name, email и password.
# Создайте список users для хранения пользователей.
# Создайте маршрут для добавления нового пользователя (метод POST).
# Создайте маршрут для обновления информации о пользователе (метод PUT).
# Создайте маршрут для удаления информации о пользователе (метод DELETE).
# Реализуйте валидацию данных запроса и ответа.
# Создать веб-страницу для отображения списка пользователей.
# Приложение должно использовать шаблонизатор Jinja для динамического формирования HTML страницы.
# Создайте HTML шаблон для отображения списка пользователей.
# Он должен содержать заголовок страницы, таблицу со списком пользователей и кнопку для добавления нового пользователя.
# Создайте маршрут для отображения списка пользователей (метод GET).
# Реализуйте вывод списка пользователей через шаблонизатор Jinja.

import logging
from typing import List

from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, EmailStr

app = FastAPI()
templates = Jinja2Templates(directory='seminar_5/templates')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    password: str


user1 = User(id=1, name='name1', email='email1@example.com', password='password1')
user2 = User(id=2, name='name2', email='email2@example.com', password='password2')
user3 = User(id=3, name='name3', email='email3@example.com', password='password3')
user4 = User(id=4, name='name4', email='email4@example.com', password='password4')
user5 = User(id=5, name='name5', email='email5@example.com', password='password5')
users = [user1, user2, user3, user4, user5]


# Маршрут для отображения главной страницы
@app.get('/', response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


# Маршрут для добавления нового пользователя
@app.post('/users/', response_model=User, tags=['users'])
def create_user(user: User):
    users.append(user)
    return user


# Маршрут для отображения всех пользователей
@app.get('/users/', response_model=List[User], tags=['users'])
def read_all_users():
    return users


# Маршрут для отображения информации о пользователе по его ID
@app.get('/users/{user_id}', response_model=User, tags=['users'])
def get_user_by_id(user_id: int):
    filtered_user = next((user for user in users if user.id == user_id), None)
    if filtered_user is None:
        raise HTTPException(status_code=404, detail=f'User {user_id} not found')
    return filtered_user


# Маршрут для обновления информации о пользователе по его ID
@app.put('/users/{user_id}', response_model=User, tags=['users'])
def update_user_by_id(user_id: int, user_data: User):
    for user in users:
        if user.id == user_id:
            user.name = user_data.name
            user.email = user_data.email
            user.password = user_data.password
            return user
    raise HTTPException(status_code=404, detail=f'User {user_id} not found')


# Маршрут для удаления пользователя по его ID
@app.delete('/users/{user_id}', tags=['users'])
def delete_user_by_id(user_id: int):
    user_to_delete = next((user for user in users if user.id == user_id), None)
    if user_to_delete:
        users.remove(user_to_delete)
        return {'message': f'User {user_id} has been deleted successfully.'}
    else:
        raise HTTPException(status_code=404, detail=f'User {user_id} not found')


# Маршрут для отображения списка пользователей через шаблонизатор Jinja
@app.get('/user_list/', response_class=HTMLResponse)
def user_list(request: Request):
    return templates.TemplateResponse('users.html', {'request': request, 'users': users})
