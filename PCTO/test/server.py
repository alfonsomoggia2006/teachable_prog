from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_greeting():
    return {"message": "Ciao, mondo!"}

# Avvio dell'app FastAPI
