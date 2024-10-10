import os
import numpy as np
import cv2
from keras.models import load_model

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)


def load_labels(file_path):

    with open(file_path, "r") as file:
        return [line.strip() for line in file.readlines()]


def preprocess_image(image_path):

    image = cv2.imread(image_path)
    image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)
    image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)
    image = (image / 127.5) - 1  # Normalize the image
    return image


def make_prediction(model, image):

    prediction = model.predict(image)
    index = np.argmax(prediction)
    return index, prediction[0][index]


def get_image_paths(image_folder, correct_tag):

    image_paths = []
    for filename in os.listdir(image_folder):
        full_path = os.path.join(image_folder, filename)
        image_paths.append((full_path, correct_tag))
    return image_paths


def test_all_images(model, image_paths_with_label):

    num_correct_predictions = 0
    for image_path, true_label in image_paths_with_label:
        img_preprocessed = preprocess_image(image_path)
        predicted_class, _ = make_prediction(model, img_preprocessed)

        # Convert predicted class index to label
        predicted_label = class_names[predicted_class]
        if predicted_label == true_label:
            num_correct_predictions += 1

    return num_correct_predictions


def main(model_path, labels_path, test_set_folder):

    # Load the model
    model = load_model(model_path, compile=False)

    # Load labels
    global class_names
    class_names = load_labels(labels_path)

    # Prepare test data
    image_paths_with_label = get_image_paths(os.path.join(test_set_folder, "macchina"), "macchina")
    image_paths_with_label += get_image_paths(os.path.join(test_set_folder, "moto"), "moto")

    # Test images and calculate accuracy
    num_correct_predictions = test_all_images(model, image_paths_with_label)
    total_images = len(image_paths_with_label)
    accuracy = num_correct_predictions / total_images

    # Print results
    print(f"Accuracy: {round(accuracy * 100)}%")


# Example usage
if __name__ == "__main__":
    main("./prova macchina/macchinaprova.jpg", "keras_Model.h5", "labels.txt")


