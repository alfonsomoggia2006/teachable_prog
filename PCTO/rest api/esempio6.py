from fastapi import FastAPI

app = FastAPI()

@app.get("/profile/")
async def profile():
    return {"name": "Alfonso", "age": 17, "country": "Italia"}
