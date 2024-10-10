import cv2

# 1. Leggere l'immagine da un file
image = cv2.imread('C:\\Users\\Pcto Gel\\Desktop\\PCTO\\openCV\\ferrari.png')

# 2. Visualizzare l'immagine in una finestra
cv2.imshow('Immagine originale', image)

# 3. Attendere che l'utente prema un tasto qualsiasi
cv2.waitKey(0)

# 4. Chiudere tutte le finestre aperte da OpenCV
cv2.destroyAllWindows()

