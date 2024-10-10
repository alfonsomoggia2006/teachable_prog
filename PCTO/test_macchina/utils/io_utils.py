from typing import BinaryIO
from venv import logger

import cv2
import os
import logging
import numpy as np
import shutil

from fastapi import UploadFile

logger = logging.getLogger(__name__)

def load_image(path: str) ->np.ndarray:
    return cv2.imread(path)

def save_image(image: np.ndarray, path: str) -> None:
    cv2.imwrite(path, image)

def get_image_paths(image_folder: str, correct_tag: str) -> list:
    # Ottiene i percorsi delle immagini di test in una cartella specificata.
    # image_folder: percorso alla cartella che contiene le immagini
    # correct_tag: è l'etichetta che indica il tipo di immagine (cane o gatto) che stiamo caricando ed è legata alla cartella

    image_paths = []
    # Cicla attraverso tutti i file nella cartella specificata
    for filename in os.listdir(image_folder):
        # Combina il percorso della cartella con il nome del file per ottenere il percorso completo
        full_path = os.path.join(image_folder, filename)
        image_paths.append((full_path, correct_tag))

    return image_paths

def create_file() ->None:
    file = open('score.txt', 'w')
    file.close()

def write_file(text: str) -> None:
    file = open('score.txt', 'a')
    file.write(text)
    file.close()

def clean_up(base_path: str) -> None:
    # Funzione che pulisce la directory di salvataggio immagini
    file_list = os.listdir(base_path)
    for file_name in file_list:
        file_path = base_path + file_name
        os.remove(file_path)
        logger.debug(f"removed file: {file_path}")


def create_save_location(save_location: str) -> None:
    # Funzione che crea la directory di salvataggio immagini
    # se non esiste già
    os.makedirs(save_location, exist_ok=True)
    logger.info("creazione cartella completata")


def save_file(file: UploadFile, save_path: str) -> None:
    # Funzione che salva un file binario
    with open(save_path, "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)