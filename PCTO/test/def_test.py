from io_utils import load_image
from predictor import predict
from image_utils import preprocess_image

def test_image(model, image: np.ndarray, true_label: str) -> bool:
    #Testa la predizione del modello rispetto all'etichetta vera.
    predicted_index, _ = predict(model, image)
    return predicted_index == true_label

def test_all_images(model, image_paths_with_labels: list) -> int:
    #Testa tutte le immagini e restituisce il numero di predizioni corrette.
    num_correct_predictions = 0
    for image_path, true_label in image_paths_with_labels:
        img = load_image(image_path)
        img_preprocessed = preprocess_image(img)
        if test_image(model, img_preprocessed, true_label):
            num_correct_predictions += 1
    return num_correct_predictions
