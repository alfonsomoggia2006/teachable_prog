import cv2
import numpy as np

# 1. Leggere l'immagine da un file
image = cv2.imread('C:\\Users\\Pcto Gel\\Desktop\\PCTO\\openCV\\ferrari.png')

# 2. Separare i canali BGR
b, g, r = cv2.split(image)

# 3. Visualizzare ogni canale in scala di grigi
# Creiamo immagini vuote per i canali
b_channel = np.zeros_like(image)
g_channel = np.zeros_like(image)
r_channel = np.zeros_like(image)

# Impostiamo solo il canale blu, verde e rosso rispettivamente
b_channel[:, :, 0] = b
g_channel[:, :, 1] = g
r_channel[:, :, 2] = r

# Visualizzare i canali in scala di grigi
cv2.imshow('Immagine Blu', b_channel)
cv2.imshow('Immagine Verde', g_channel)
cv2.imshow('Immagine Rosso', r_channel)

# 4. Attendere che l'utente prema un tasto qualsiasi
cv2.waitKey(0)

# 5. Chiudere tutte le finestre aperte da OpenCV
cv2.destroyAllWindows()





