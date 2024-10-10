from fastapi import FastAPI

app = FastAPI()

@app.get("/is_adult/")
async def is_adult(age: int):
    return age >= 18
