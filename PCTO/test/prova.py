import os
import cv2
import numpy as np
from tensorflow.keras.models import load_model

np.set_printoptions(suppress=True)

def load_labels(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file.readlines()]

def preprocess_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print(f"Errore nel caricamento dell'immagine: {image_path}")
        return None
    image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)
    image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)
    image = image / 255.0  # Normalizzazione nell'intervallo [0, 1]
    return image

def make_prediction(model, image):
    prediction = model.predict(image)
    index = np.argmax(prediction)
    return index, prediction[0][index]

def main(cartella_immagini, model_path, labels_path):
    model = load_model(model_path, compile=False)
    class_names = load_labels(labels_path)

    previsioni_corrette = 0
    totale_immagini = 0

    for filename in os.listdir(cartella_immagini):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            totale_immagini += 1
            etichetta_reale = filename.split('_')[0]
            print(f"Etichetta reale: {etichetta_reale}")

            image_path = os.path.join(cartella_immagini, filename)
            image = preprocess_image(image_path)

            if image is None:
                continue

            index, confidence_score = make_prediction(model, image)
            etichetta_previsione = class_names[index]

            print(f"Immagine: {filename}")
            print(f"Classe prevista: {etichetta_previsione}, Percentuale: {np.round(confidence_score * 100, 2)}%")
            print(f"Predizioni: {prediction}")

            if etichetta_reale == etichetta_previsione:
                previsioni_corrette += 1

    print(f"Previsioni corrette: {previsioni_corrette}, Totale immagini: {totale_immagini}")
    if totale_immagini > 0:
        accuratezza = (previsioni_corrette / totale_immagini) * 100
        print(f"Accuratezza: {accuratezza:.2f}%")
    else:
        print("Errore: il totale delle immagini è zero.")

if __name__ == "__main__":
    main("./prova macchina", "keras_Model.h5", "labels.txt")

