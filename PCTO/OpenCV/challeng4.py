import cv2
import numpy as np

# 1. Leggere l'immagine da un file
image = cv2.imread('C:\\Users\\Pcto Gel\\Desktop\\PCTO\\openCV\\ferrari.png')

# 2. Normalizzazione Min-Max dell'immagine
normalized_image = cv2.normalize(image.astype('float32'), None, alpha=-1, beta=1, norm_type=cv2.NORM_MINMAX)

# 3. Visualizzare due immagini in due finestre
cv2.imshow('Immagine Originale', image)
cv2.imshow('Immagine Normalizzata (Min-Max)', normalized_image)

# Attendere che l'utente prema un tasto qualsiasi
cv2.waitKey(0)

# Chiudere tutte le finestre aperte da OpenCV
cv2.destroyAllWindows()


def z_score_normalization(image):
    # Separare i canali BGR
    b, g, r = cv2.split(image.astype('float32'))

    # Normalizzare ogni canale usando Z-Score
    r_normalized = (b - np.mean(r)) / np.std(b)
    g_normalized = (g - np.mean(g)) / np.std(g)
    b_normalized = (r - np.mean(b)) / np.std(r)

    # Ricomporre i canali normalizzati in un'unica immagine
    normalized_image_z = cv2.merge((b_normalized, g_normalized, r_normalized))

    return normalized_image_z

# Eseguire la normalizzazione Z-Score
normalized_z_image = z_score_normalization(image)

# Visualizzare l'immagine normalizzata Z-Score
cv2.imshow('Immagine Normalizzata ', normalized_z_image)

# Attendere che l'utente prema un tasto qualsiasi
cv2.waitKey(0)

# Chiudere tutte le finestre aperte da OpenCV
cv2.destroyAllWindows()













