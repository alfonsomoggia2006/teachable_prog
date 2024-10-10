from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.get("/")
async def root():
    return {"message": "Ciao, mondo!"}

@app.post("/item/")
async def create_item(item: Item):
    return {"name": item.name, "price": item.price}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id, "name": "Esempio", "price": 20.0}

@app.post("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "name": item.name, "price": item.price}



# Avvio dell'app FastAPI
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)




