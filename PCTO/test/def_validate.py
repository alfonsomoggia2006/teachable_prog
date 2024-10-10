from io_utils import load_model, get_image_paths
from validation_utils import test_all_images

model = load_model("path_to_your_model")

def validate():
    image_paths_with_label = get_image_paths("./test_set/dogs", "class 1")
    image_paths_with_label += get_image_paths("./test_set/cats", "class 2")

    num_correct_predictions = test_all_images(model, image_paths_with_label)
    total_images = len(image_paths_with_label)
    accuracy = num_correct_predictions / total_images if total_images > 0 else 0

    with open("accuracy.txt", "w") as f:
        f.write(f"Accuratezza: {accuracy:.2f}\n")

if __name__ == "__main__":
    validate()
