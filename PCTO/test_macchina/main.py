import cv2
from keras.models import load_model
from utils.image_utils import process_image
from utils.io_utils import load_image
from utils.prediction_util import get_prediction

model = load_model('model/keras_model.h5', compile=False)

def main():
    path_to_img = "immagini/macchina/autoprova.jpg"

    image = load_image(path_to_img)
    cv2.imshow('Image', image)
    image = process_image(image)

    label, score = get_prediction(model, image)

    print("L'immagine è: ", label, " al ", round(score*100),"%")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()