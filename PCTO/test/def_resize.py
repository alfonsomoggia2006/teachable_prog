import cv2
import numpy as np

def resize(img: np.ndarray, width: int = 224, height: int = 224) -> np.ndarray:
    #Ridimensiona l'immagine alle dimensioni specificate.
    return cv2.resize(img, (width, height))

def preprocess_image(image: np.ndarray) -> np.ndarray:
    #Esegue il preprocessing dell'immagine (ridimensionamento e normalizzazione).
    image = resize(image)
    image = image.astype(np.float32) / 127.5 - 1  # Normalizzazione nell'intervallo [-1, 1]
    return np.reshape(image, (1, 224, 224, 3))  # Aggiungi la dimensione del batch
