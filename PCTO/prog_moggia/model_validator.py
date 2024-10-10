from keras.models import load_model
from utils.io_utils import get_image_paths, create_file, write_file
from utils.validation_utils import test_all_image

path_to_model = "model/keras_model.h5"

model = load_model(path_to_model, compile=False)

def validate():
    image_paths_with_label = get_image_paths("immagini/macchina", "macchina")
    image_paths_with_label += get_image_paths("immagini/moto", "moto")

    num_correct_predictions = test_all_image(model, image_paths_with_label)
    total_images = len(image_paths_with_label)
    accuracy = num_correct_predictions / total_images

    #converto accuracy in %
    accuracy = round(accuracy*100)

    # Scrive il valore di accuracy in un file
    create_file()
    write_file('Score: '+str(accuracy))

if __name__ == "__main__":
    validate()