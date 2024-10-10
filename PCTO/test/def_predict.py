def predict(model, image: np.ndarray) -> tuple[int, float]:
    #Esegue la predizione sull'immagine utilizzando il modello.
    predictions = model.predict(image)
    index = np.argmax(predictions)
    return index, predictions[0][index]
