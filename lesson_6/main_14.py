from fastapi import FastAPI, Path

app = FastAPI()


@app.get('/items/{item_id}')
async def read_item(item_id: int = Path(..., ge=1)):
    return {"item_id": item_id}
