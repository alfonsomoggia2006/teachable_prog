from fastapi import FastAPI, Form

app = FastAPI()

class User(BaseModel):
    username: str
    password: str

@app.post("/submit_form/")
async def submit_form(user: User):
    return {"username": user.username, "password": user.password}
