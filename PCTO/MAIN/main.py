import cv2
import numpy as np

# 1. Leggere l'immagine da un file
image = cv2.imread('C:\\Users\\Pcto Gel\\Desktop\\PCTO\\veicoli\\ferrari.png')

# 2. Sottrarre un valore ai pixel dell'immagine
value_to_subtract = np.array([14, 0, 53], dtype=np.uint8)  # Valori diversi per i diversi canali
dark_image = cv2.subtract(image, np.full(image.shape, value_to_subtract, dtype=np.uint8))

# 3. Visualizzare due immagini in due finestre
cv2.imshow('Immagine Originale', image)
cv2.imshow('Immagine dopo la sottrazione', dark_image)

# 6. Attendere che l'utente prema un tasto qualsiasi
cv2.waitKey(0)

# 7. Chiudere tutte le finestre aperte da OpenCV
cv2.destroyAllWindows()
