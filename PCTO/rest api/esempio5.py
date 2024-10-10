from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/login/")
async def login(request: Request):
    data = await request.json()
    username = data.get("username")
    password = data.get("password")
    login_result = "success" if username and password else "failure"
    return {"username": username, "login": login_result}
