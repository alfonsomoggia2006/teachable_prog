import os
import numpy as np
import cv2
from tensorflow.keras.models import load_model

def load_labels(labels_path):
    # Carica le etichette dal file
    with open(labels_path, 'r') as f:
        return f.read().splitlines()

def preprocess_image(image_path):
    # Funzione per caricare e preprocessare l'immagine
    image = cv2.imread(image_path)
    image = cv2.resize(image, (224, 224))  # Modifica le dimensioni se necessario
    image = image.astype('float32') / 255.0  # Normalizza l'immagine
    image = np.expand_dims(image, axis=0)  # Aggiunge la dimensione del batch
    return image

def make_prediction(model, image):
    # Funzione per fare una previsione sull'immagine
    predictions = model.predict(image)
    index = np.argmax(predictions, axis=1)[0]
    confidence_score = predictions[0][index]
    return index, confidence_score

def main(cartella_immagini, model_path, labels_path):
    model = load_model(model_path, compile=False)
    class_names = load_labels(labels_path)

    previsioni_corrette = 0
    totale_immagini = 0

    for filename in os.listdir(cartella_immagini):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            totale_immagini += 1
            etichetta_reale = filename.split('_')[0]  # Modifica se necessario

            image_path = os.path.join(cartella_immagini, filename)
            image = preprocess_image(image_path)

            index, confidence_score = make_prediction(model, image)
            etichetta_previsione = class_names[index][2:]  # Modifica se necessario

            print(f"Immagine: {filename}, Classe: {etichetta_previsione}, Percentuale: {np.round(confidence_score * 100, 2)}%")

            if etichetta_reale == etichetta_previsione:
                previsioni_corrette += 1

    print(f"Previsioni corrette: {previsioni_corrette}, Totale immagini: {totale_immagini}")
    if totale_immagini > 0:
        accuratezza = (previsioni_corrette / totale_immagini) * 100
        print(f"Accuratezza: {accuratezza:.2f}%")
    else:
        print("Errore: il totale delle immagini è zero.")

    cv2.destroyAllWindows()

# Specifica i percorsi del modello e delle etichette
model_path = 'path/to/your/model.h5'  # Sostituisci con il percorso reale del tuo modello
labels_path = 'path/to/your/labels.txt'  # Sostituisci con il percorso reale del tuo file di etichette
cartella_immagini = r'C:\Users\Pcto Gel\Desktop\PCTO\test\prova macchina'

# Esegui la funzione main
main(cartella_immagini, model_path, labels_path)

