# Librerías
import cv2
import numpy as np

# Leer la imagen a color
imagen = cv2.imread("ranita.png", cv2.IMREAD_COLOR)

# Convertir la clave textual en un valor numérico
clave = input("Ingrese una clave: ")

suma = 0

for letra in clave:
    suma += ord(letra)

k = suma

# Crear una imagen para guardar el resultado
imagen_cifrada = np.zeros_like(imagen)

# Obtener tamaño de la imagen, como es una imagen a color se le agrega los canales
filas, columnas, canales = imagen.shape

# Recorrer toda la imagen
for i in range(filas):
    for j in range(columnas):
        for c in range(canales):

            # Obtener el valor del canal
            x = int(imagen[i, j, c])

            # Capa 1: función biyectiva
            y = (13 * x + 57) % 256

            # Capa 2: suma modular con la clave
            z = (y + k) % 256

            # Guardar el nuevo valor
            imagen_cifrada[i, j, c] = z

# Guardar la imagen cifrada
cv2.imwrite("ranita_cifrada.png", imagen_cifrada)

print("Imagen cifrada correctamente.")

# Mostrar imágenes
cv2.imshow("Imagen Original", imagen)
cv2.imshow("Imagen Cifrada", imagen_cifrada)

cv2.waitKey(0)
cv2.destroyAllWindows()