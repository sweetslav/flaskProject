from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def read_root():
    return {'message': 'Hello World'}


# @app.get('/items/{item_id}')
# async def read_item(item_id: int):
#     return {'item_id': item_id}


@app.get('/items/{item_id}')
async def read_item(item_id: int, q: str = None):
    if q:
        return {'item_id': item_id, 'q': q}
    return {'item_id': item_id}


@app.get('/users/{user_id}/orders/{order_id}')
async def read_order(user_id: int, order_id: int):
    # Обработка данных
    return {'user_id': user_id, 'order_id': order_id}


@app.get('/items/')
async def skip_limit(skip: int = 0, limit: int = 10):
    return {'skip': skip, 'limit': limit}
