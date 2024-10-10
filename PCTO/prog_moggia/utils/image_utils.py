import cv2
import numpy as np

def resize(image: np.ndarray, width: int = 224, heigth: int = 224) ->np.ndarray:
    return cv2.resize(image, (width, heigth), interpolation=cv2.INTER_AREA)

def grayscale(image: np.ndarray) ->np.ndarray:
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def crop(image: np.ndarray, rectangle: tuple[int, int, int, int]) -> np.ndarray:
    y = rectangle[0]
    y2 = rectangle[1]
    x = rectangle[2]
    x2 = rectangle[3]

    return image[y:y2, x:x2]

def process_image(image: np.ndarray) -> np.ndarray:
    # Resize the raw image into (224-height,224-width) pixels
    image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

    # Make the image a numpy array and reshape it to the models input shape.
    image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

    # Normalize the image array
    image = (image / 127.5) - 1

    return image