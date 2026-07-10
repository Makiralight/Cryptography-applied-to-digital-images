# Librerías
import cv2
import numpy as np

# Leer la imagen original
imagen = cv2.imread("ranita.png", cv2.IMREAD_COLOR)

# Ingresar la clave
clave = input("Ingrese una clave: ")

# Convertir la clave a un valor numérico
suma = 0
for letra in clave:
    suma += ord(letra)

k = suma

# Obtener dimensiones de la imagen
filas, columnas, canales = imagen.shape

# CIFRADO

# Crear imagen cifrada
imagen_cifrada = np.zeros_like(imagen)

# Recorrer todos los píxeles
for i in range(filas):
    for j in range(columnas):
        for c in range(canales):

            # Valor del píxel
            x = int(imagen[i, j, c])

            # Capa 1: función biyectiva
            y = (13 * x + 57) % 256

            # Capa 2: suma modular con la clave
            z = (y + k) % 256

            # Guardar el resultado
            imagen_cifrada[i, j, c] = z

# Guardar la imagen cifrada
cv2.imwrite("ranita_cifrada.png", imagen_cifrada)

print("Imagen cifrada correctamente.")

# DESCIFRADO

# Leer la imagen cifrada
imagen_cifrada = cv2.imread("ranita_cifrada.png", cv2.IMREAD_COLOR)

# Crear imagen para el resultado
imagen_descifrada = np.zeros_like(imagen_cifrada)

# Inverso modular de 13 módulo 256
inv13 = 197

# Recorrer la imagen cifrada
for i in range(filas):
    for j in range(columnas):
        for c in range(canales):

            # Valor cifrado
            z = int(imagen_cifrada[i, j, c])

            # Deshacer la suma con la clave
            y = (z - k) % 256

            # Deshacer la función biyectiva
            x = (inv13 * (y - 57)) % 256

            # Guardar el píxel recuperado
            imagen_descifrada[i, j, c] = x

# Guardar la imagen descifrada
cv2.imwrite("ranita_descifrada.png", imagen_descifrada)

print("Imagen descifrada correctamente.")

# Mostrar imágenes
#cv2.imshow("Imagen Original", imagen)
cv2.imshow("Imagen Cifrada", imagen_cifrada)
cv2.imshow("Imagen Descifrada", imagen_descifrada)

cv2.waitKey(0)
cv2.destroyAllWindows()