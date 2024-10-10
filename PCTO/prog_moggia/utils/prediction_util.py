import numpy as np

classes = ["Ferrari", "Porsche", "Jeep", "quad", "Panda"]

def get_prediction(model, image_preprocessed: np.ndarray) -> tuple[str, float]:
    # Ottenere la predizione proposta dal modello
    prediction = model.predict(image_preprocessed)
    index = np.argmax(prediction)  # Trova la predizione più probabile
    predicted_class = classes[index]
    prediction_confidence = prediction[0][index]
    return predicted_class, prediction_confidence