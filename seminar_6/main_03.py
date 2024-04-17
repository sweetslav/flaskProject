# Задание №3.
# Создать API для управления списком задач.
# Каждая задача должна содержать поля "название", "описание" и "статус" (выполнена/не выполнена).
# API должен позволять выполнять CRUD операции с задачами.

from random import choice
from typing import List

import databases
import sqlalchemy
from faker import Faker
from fastapi import FastAPI
from pydantic import BaseModel, Field

DATABASE_URL = 'sqlite:///homework_6.db'

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

app = FastAPI()
fake = Faker()

tasks = sqlalchemy.Table(
    'tasks',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer(), primary_key=True),
    sqlalchemy.Column('task_name', sqlalchemy.String(80)),
    sqlalchemy.Column('description', sqlalchemy.String(100)),
    sqlalchemy.Column('status', sqlalchemy.String(32))
)

statuses = ['Complete', 'Incomplete', 'In process']


class TaskIn(BaseModel):
    task_name: str = Field(..., title='Task Name', description='Description of task name', min_length=3, max_length=80)
    description: str = Field(None, title='Description', description='Description of task', max_length=100)
    status: str = Field(default='Incomplete', description='Status of task')


class Task(TaskIn):
    id: int


@app.on_event('startup')
async def startup():
    await database.connect()


@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()


engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)


@app.get('/fake_tasks/{count}', tags=['Fill database'])
async def create_fake_tasks(count: int):
    for i in range(count):
        query = tasks.insert().values(
            task_name=fake.sentence(),
            description=fake.text(max_nb_chars=100),
            status=choice(statuses))
        await database.execute(query)
    return {'message': f'{count} Tasks created successfully'}


@app.get('/tasks/', response_model=List[Task], tags=['tasks'])
async def get_tasks():
    query = tasks.select()
    return await database.fetch_all(query)


@app.get('/tasks/{task_id}', response_model=Task, tags=['tasks'])
async def get_task(task_id: int):
    query = tasks.select().where(tasks.c.id == task_id)
    return await database.fetch_one(query)


@app.post('/tasks/', response_model=Task, tags=['tasks'])
async def create_task(task: TaskIn):
    query = tasks.insert().values(**task.dict())
    task_id = await database.execute(query)
    return {**task.dict(), 'id': task_id}


@app.put('/tasks/{task_id}', response_model=Task, tags=['tasks'])
async def update_task(task_id: int, task: TaskIn):
    query = tasks.update().where(tasks.c.id == task_id).values(**task.dict())
    await database.execute(query)
    updated_task = await get_task(task_id)
    return updated_task


@app.delete('/tasks/{task_id}', tags=['tasks'])
async def delete_task(task_id: int):
    query = tasks.delete().where(tasks.c.id == task_id)
    await database.execute(query)
    return {'message': f'Task {task_id} was deleted'}
