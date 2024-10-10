import os
import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Disabilita la notazione scientifica per maggiore chiarezza
np.set_printoptions(suppress=True)


def load_labels(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file.readlines()]


def preprocess_image(image_path):
    image = cv2.imread(image_path)
    image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)
    image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)
    image = (image / 127.5) - 1  # Normalizza l'immagine
    return image


def make_prediction(model, image):
    prediction = model.predict(image)
    index = np.argmax(prediction)
    return index, prediction[0][index]


def main(cartella_immagini, model_path, labels_path):
    # Carica il modello
    model = load_model(model_path, compile=False)

    # Carica le etichette
    class_names = load_labels(labels_path)

    previsioni_corrette = 0
    totale_immagini = 0

    # Elabora ogni immagine nella directory
    for filename in os.listdir(cartella_immagini):
        if filename.endswith(('.jpg', '.jpeg', '.png')):  # Regola per i tuoi formati di immagine
            totale_immagini += 1

            # Ottieni l'etichetta corretta dal nome del file (assumendo sia formattato come "etichetta_immagine.jpg")
            etichetta_reale = filename.split('_')[0]  # Modifica secondo la tua convenzione di denominazione

            # Preprocessa l'immagine
            image_path = os.path.join(cartella_immagini, filename)
            image = preprocess_image(image_path)

            # Fai una previsione
            index, confidence_score = make_prediction(model, image)

            etichetta_previsione = class_names[index][2:]  # Regola come necessario
            print(f"Immagine: {filename}")
            print(f"Classe : {etichetta_previsione}, percentuale: {np.round(confidence_score * 100, 2)}%")

            # Controlla se la previsione è corretta
            if etichetta_reale == etichetta_previsione:
                previsioni_corrette +=1

    # Stampa i risultati
    print(f"Previsioni corrette: {previsioni_corrette}, Totale immagini: {totale_immagini}")
    if totale_immagini > 0:
        accuratezza = ((previsioni_corrette / totale_immagini) * 100)
        print(f"Accuratezza: {accuratezza:.2f}%")
    else:
        print("Errore: il totale delle immagini è zero.")

    cv2.destroyAllWindows()

# Esempio di utilizzo
if __name__ == "__main__":
    main("./prova macchina", "keras_Model.h5", "labels.txt")
