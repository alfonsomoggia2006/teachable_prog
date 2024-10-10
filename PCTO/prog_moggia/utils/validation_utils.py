import numpy as np

from utils.io_utils import load_image
from utils.prediction_util import get_prediction
from utils.image_utils import process_image

def test_image(model, image: np.ndarray, true_label: str) -> bool:
    image_processed = process_image(image)
    predicted_class, confidence_score = get_prediction(model, image_processed)

    return predicted_class.lower() == true_label.lower()

def test_all_image(model, image_paths_with_label: list) -> int:
    num_correct_prediction = 0
    for image_path, true_label in image_paths_with_label:
        image = load_image(image_path)

        if test_image(model, image, true_label):
            num_correct_prediction += 1

    return num_correct_prediction

