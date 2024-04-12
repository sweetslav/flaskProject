from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

app = FastAPI(openapi_url="/api/v1/openapi.json")


@app.get('/hello/{name}')
async def hello_name(name: str, age: int):
    return {"name": name, "age": age}


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Custom OpenAPI",
        version="1.0.0",
        description="This is very custom openapi schema",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
