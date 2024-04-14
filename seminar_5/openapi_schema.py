from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.models import APIKey, APIKeyInHeader
from fastapi.openapi.utils import get_openapi


app = FastAPI()

# Определяем API ключ для Swagger UI
API_KEY = "fake-api-key"
API_KEY_NAME = "access_token"


# Генерируем документацию OpenAPI
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Task Manager API",
        version="1.0.0",
        description="This is a very fancy project, with auto-generated API documentation from FastAPI.",
        routes=app.routes,
    )
    # Добавляем API ключ для авторизации в документацию
    openapi_schema["components"]["securitySchemes"] = {
        API_KEY_NAME: {
            "type": "apiKey",
            "in": "header",
            "name": API_KEY_NAME
        }
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


# Маршрут для получения документации Swagger UI
@app.get("/docs", include_in_schema=False)
def get_documentation():
    return get_swagger_ui_html(openapi_url="/openapi.json", title="docs")


# Маршрут для отображения схемы OpenAPI
@app.get("/openapi.json", include_in_schema=False)
def get_open_api_endpoint():
    return custom_openapi()


# Проверка на уникальность ID при создании новой задачи
def is_unique_id(task_id: int):
    return task_id not in [task.id for task in tasks]


# Добавление обработчика исключений для проверки уникальности ID
def validate_unique_id(task_id: int):
    if not is_unique_id(task_id):
        raise HTTPException(status_code=400, detail="ID already exists")


# Измененная функция создания задачи с проверкой уникальности ID
@app.post('/tasks/', response_model=Task)
def create_task(task: Task = Depends(validate_unique_id)):
    tasks.append(task)
    logger.info('Отработал POST запрос.')
    return task
