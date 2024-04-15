from fastapi import FastAPI, Query

app = FastAPI()


@app.get('/items/')
async def read_items(q: str = Query(..., min_length=3, max_length=50)):
    results = {'items': [{'item_id': 'Spam'}, {'item_id': 'Eggs'}]}
    if q:
        results.update({'q': q})
    return results
