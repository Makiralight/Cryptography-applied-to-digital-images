#Librerias, cv2 es para imagenes y numpy 
import cv2
import numpy as np

# Se lee la imagen pero por momento en colores a blanco y negro
imagen = cv2.imread("ranita.png", cv2.IMREAD_GRAYSCALE)

# Convertir la clave textual en un valor numérico
clave = input("Ingrese una clave: ")

suma = 0

for letra in clave:
    suma += ord(letra)

k = suma

# se crea un imagen para guardar el resultado de la ranita cifrada
imagen_cifrada = np.zeros_like(imagen)

filas, columnas = imagen.shape

for i in range(filas):
    for j in range(columnas):

        x = int(imagen[i, j])

        # Capa 1
        y = (13 * x + 57) % 256

        # Capa 2
        z = (y + k) % 256

        imagen_cifrada[i, j] = z

# Guardar la imagen cifrada
cv2.imwrite("ranita_cifrada.png", imagen_cifrada)

print("Imagen cifrada correctamente.")

cv2.imshow("Imagen Original", imagen)
cv2.imshow("Imagen Cifrada", imagen_cifrada)

cv2.waitKey(0)
cv2.destroyAllWindows()