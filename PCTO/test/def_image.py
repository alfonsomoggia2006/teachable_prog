import os
import numpy as np
from tensorflow.keras.models import load_model
import cv2

def load_model(path: str):
    #Carica il modello dal percorso specificato.
    return load_model(path)

def load_image(path: str) -> np.ndarray:
    #Carica un'immagine e la restituisce come array numpy.
    image = cv2.imread(path)
    if image is None:
        raise ValueError(f"Immagine non trovata in {path}")
    return image

def save_image(image: np.ndarray, path: str) -> None:
    #Salva l'immagine nel percorso specificato.
    cv2.imwrite(path, image)

def get_image_paths(image_folder: str, correct_tag: str) -> list:
    #Recupera i percorsi delle immagini nella cartella specificata.
    return [(os.path.join(image_folder, filename), correct_tag)
            for filename in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, filename))]
