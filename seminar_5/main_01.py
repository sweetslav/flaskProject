# Задание №1.
# Создать API для управления списком задач.
# Приложение должно иметь возможность создавать, обновлять, удалять и получать список задач.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс Task с полями id, title, description и status.
# Создайте список tasks для хранения задач.
# Создайте маршрут для получения списка задач (метод GET).
# Создайте маршрут для создания новой задачи (метод POST).
# Создайте маршрут для обновления задачи (метод PUT).
# Создайте маршрут для удаления задачи (метод DELETE).
# Реализуйте валидацию данных запроса и ответа.

import logging
from typing import Optional, List

from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    status: Optional[str] = None


task_1 = Task(id=1, title="title_1", description="description_1", status='completed')
task_2 = Task(id=2, title="title_2", description="description_2", status='in_progress')
task_3 = Task(id=3, title="title_3", description="description_3", status='in_progress')
task_4 = Task(id=4, title="title_4", description="description_4", status='completed')
task_5 = Task(id=5, title="title_5", description="description_5", status='in_progress')

tasks = [task_1, task_2, task_3, task_4, task_5]


@app.get('/')
def root():
    logger.info('Отработал GET запрос.')
    return {'message': 'Homepage'}


@app.get('/tasks/', response_model=List[Task])
def get_tasks():
    logger.info('Отработал GET запрос.')
    return tasks


@app.post('/tasks/', response_model=Task)
def create_task(task: Task = Depends()):
    tasks.append(task)
    logger.info('Отработал POST запрос.')
    return task


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task: Task):
    task_index = next((index for index, t in enumerate(tasks) if t.id == task_id), None)
    if task_index is None:
        raise HTTPException(status_code=404, detail="Task not found")
    tasks[task_index] = task
    logger.info(f'{task_id} was updated')
    return task


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    task_index = next((index for index, t in enumerate(tasks) if t.id == task_id), None)
    if task_index is None:
        raise HTTPException(status_code=404, detail="Task not found")
    del tasks[task_index]
    logger.info(f'{task_id} was deleted')
    return {"message": "Task deleted"}
