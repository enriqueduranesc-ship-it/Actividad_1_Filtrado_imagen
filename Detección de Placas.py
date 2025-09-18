import matplotlib.pyplot as mpl
import pytesseract
pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"
import numpy as np
import cv2 as cv
import os

os.system("clear")
os.chdir('/Users/enriqueduran/Desktop/General/Archivos/Escolar/Python/Resources')

# Cargar imagen
img = cv.imread('placa_1.jpg', cv.IMREAD_COLOR)
assert img is not None, "file could not be read, check with os.path.exists()"

# Convertir a RGB
img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

# Filtrar solo texto negro
lower_black = np.array([0, 0, 0])
upper_black = np.array([40, 40, 40])
mask = cv.inRange(img_rgb, lower_black, upper_black)

# Limpiar ruido y recuperar texto
kernel = np.ones((2, 2), np.uint8)
mask_eroded = cv.erode(mask, kernel, iterations=2)
mask_dilated = cv.dilate(mask_eroded, kernel, iterations=6)
mask_final = cv.GaussianBlur(mask_dilated, (3, 3), 1)

# Aplicar máscara y preparar para OCR
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
result = cv.bitwise_and(img_gray, img_gray, mask=mask_final)
_, thresh_final = cv.threshold(result, 1, 255, cv.THRESH_BINARY)

# Mostrar procesamiento
mpl.figure(figsize=(12, 4))

mpl.subplot(1, 3, 1)
mpl.title("Original")
mpl.imshow(img_rgb)
mpl.axis("off")

mpl.subplot(1, 3, 2)
mpl.title("Texto Filtrado")
mpl.imshow(result, cmap='gray')
mpl.axis("off")

mpl.subplot(1, 3, 3)
mpl.title("Para OCR")
mpl.imshow(thresh_final, cmap='gray')
mpl.axis("off")

mpl.show()

# OCR con PSM 8 (una palabra)
text = pytesseract.image_to_string(thresh_final, config=r'--oem 3 --psm 8 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ')

print(f"\nTexto detectado: '{text.strip()}'")
