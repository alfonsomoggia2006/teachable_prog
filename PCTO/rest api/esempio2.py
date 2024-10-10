from fastapi import FastAPI

app = FastAPI()

@app.get("/greet/{name}")
async def greet(name: str):
    return f"Hello, {name}!"
# Avvio dell'app FastAPI
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)