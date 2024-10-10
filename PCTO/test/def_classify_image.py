from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import os
import shutil
import io_utils as I  # Assicurati di importare correttamente io_utils.py

app = FastAPI()

@app.post("/classify-image/")
async def classify_image(file: UploadFile = File(...)):
    try:
        save_path = os.path.join("uploaded_images", file.filename)
        os.makedirs(os.path.dirname(save_path), exist_ok=True)

        # Salva l'immagine caricata
        with open(save_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        img = I.read_img(save_path)
        img = I.process_img(img)
        class_name, confidence = I.predict_class(img, MODEL)

        # Opzionalmente elimina l'immagine dopo l'elaborazione
        if os.path.isfile(save_path):
            os.remove(save_path)

        return JSONResponse(
            content={
                "filename": file.filename,
                "message": I.print_prediction(class_name, confidence),
            }
        )
    except Exception as e:
        logger.error(f"Errore durante la classificazione dell'immagine: {str(e)}")
        return JSONResponse(content={"error": str(e)}, status_code=500)
