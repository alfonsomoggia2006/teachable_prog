from fastapi import FastAPI, HTTPException, Request

app = FastAPI()

@app.post("/item/")
async def create_item(request: Request):
    data = await request.json()
    item_name = data.get("name")
    item_price = data.get("price")
    if not item_name or not isinstance(item_price, float):
        raise HTTPException(status_code=400, detail="Invalid item provided.")
    return {"name": item_name, "price": item_price}
