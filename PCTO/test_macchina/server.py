from http.client import HTTPException
from keras.models import load_model
import os
import uvicorn
from fastapi import *
from pydantic import *
from starlette.responses import JSONResponse, FileResponse

from utils.image_utils import *
from utils.validation_utils import *

from utils.io_utils import save_image, load_image, save_file

model = load_model("model/keras_model.h5", compile=False)

class User(BaseModel):
    username: str
    password: str

app = FastAPI()

@app.get("/greet/{name}")
async def greet(name: str):
    return f"Hello, {name}!"

@app.get("/is_adult/")
async def is_adult(age: int):
    return age >= 18

@app.post("/submit_form/")
async def submit_form(user: User):
    return {"username": user.username, "password": user.password}

@app.post("/login/")
async def login(request: Request):
    data = await request.json()

    username = data.get("username")
    password = data.get("password")

    if username is not None and password is not None:
        login_result = "success"
    else:
        login_result = "failure"

    return {
        "username": username,
        "login": login_result
    }

@app.get("/profile/")
async def profile():
    # Dati di esempio che potrebbero provenire da un database o da un'altra fonte
    profile_data = {
        "name": "Giovanni",
        "age": 30,
        "country": "Italia"
    }
    return profile_data


@app.post("/item/")
async def create_item(request: Request):
    data = await request.json()
    item_name = data.get("name")
    item_price = data.get("price")

    if not item_name or not isinstance(item_price, float):
        raise HTTPException(status_code=400, detail="Invalid item provided.")

    # Qui potresti inserire i dati in un database o elaborarli ulteriormente
    return {"name": item_name, "price": item_price}

@app.post("/items/{item_id}")
async def update_item(item_id: int, request: Request):
    data = await request.json()
    update_data = {
        "item_id": item_id,
        "name": data.get("name"),
        "price": data.get("price")
    }
    # Qui potresti aggiornare i dati in un database
    return update_data

@app.post("/classify-image/")
async def classify_image(file: UploadFile):
    try:
        # Definisci il percorso dove salvare l'immagine
        save_path = f"uploaded_images/{file.filename}"

        # Crea la directory se non esiste
        os.makedirs(os.path.dirname(save_path), exist_ok=True)

        # Salva l'immagine
        save_file(file, save_path)

        #print("Saved image")
        img = load_image(save_path)
        #print("Read image")
        img = process_image(img)
        #print("Processed image")
        class_name, confidence = get_prediction(model, img)
        #print("Classified image")
        #print(class_name, confidence)

        message = "L'immagine è: " + class_name + " score: " + str(round(confidence*100))

        if os.path.isfile(save_path):
            os.remove(save_path)

        return JSONResponse(
            content={
                "filename": file.filename,
                "message": message,
            }
        )
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.post("/grayscale-image/")
async def grayscale_image(file: UploadFile):
    try:
        # Definisci il percorso dove salvare l'immagine
        save_path = f"uploaded_images/{file.filename}"

        # Crea la directory se non esiste
        os.makedirs(os.path.dirname(save_path), exist_ok=True)

        # Salva l'immagine
        save_file(file, save_path)

        img = load_image(save_path)
        img = grayscale(img)

        save_image(img, save_path)

        return FileResponse(save_path)

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.post("/crop-image/")
async def crop_image(file: UploadFile, start_y = Form(int), end_y = Form(int), start_x= Form(int), end_x= Form(int)):
    try:
        # Definisci il percorso dove salvare l'immagine
        save_path = f"uploaded_images/{file.filename}"

        # Crea la directory se non esiste
        os.makedirs(os.path.dirname(save_path), exist_ok=True)

        # Salva l'immagine
        save_file(file, save_path)

        img = load_image(save_path)
        if start_y != end_y:
            temp = int(start_y), int(end_y), int(start_x), int(end_x)
        else:
            return JSONResponse(content={"error": "Invalid values"}, status_code=400)

        img = crop(img, temp)

        save_image(img, save_path)

        return FileResponse(save_path)

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

def main():
    uvicorn.run(app, host="127.0.0.1", port=8000)

# Avvio dell'app FastAPI
if __name__ == "__main__":
    main()