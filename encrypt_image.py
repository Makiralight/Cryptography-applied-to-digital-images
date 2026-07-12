from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os

# Pedir clave
clave = input("Ingrese una clave: ")

# Convertir la clave textual en un valor numérico
k = 0
for letra in clave:
    k += ord(letra)

print("\nClave convertida correctamente.")
print(f"Valor numérico de la clave (k): {k}")

# Seleccionar imagen
root = Tk()
root.withdraw()

ruta = askopenfilename(
    title="Seleccionar imagen",
    filetypes=[("Archivos de imagen", "*.png *.jpg *.jpeg *.bmp")]
)

if not ruta:
    print("No se seleccionó ninguna imagen.")
    exit()

root.destroy()

# Abrir imagen
imagen = Image.open(ruta).convert("RGBA")

nombre = os.path.splitext(os.path.basename(ruta))[0]

# Carpeta de resultados
os.makedirs("resultados", exist_ok=True)

ruta_cifrada = os.path.join("resultados", f"{nombre}_cifrada.png")
ruta_descifrada = os.path.join("resultados", f"{nombre}_descifrada.png")

# Crear imágenes
imagen_cifrada = Image.new("RGBA", imagen.size)
imagen_descifrada = Image.new("RGBA", imagen.size)

print("\nImagen cargada correctamente")
print("Tamaño:", imagen.size)
print("Modo:", imagen.mode)

# =======================
# CAPAS 1 Y 2 (CIFRADO)
# =======================

for x in range(imagen.width):
    for y in range(imagen.height):

        r, g, b, a = imagen.getpixel((x, y))

        # Capa 1: Función biyectiva
        y_r = (13 * r + 57) % 256
        y_g = (13 * g + 57) % 256
        y_b = (13 * b + 57) % 256

        # Capa 2: Suma modular con clave y posición
        z_r = (y_r + k + x + y) % 256
        z_g = (y_g + k + x + y) % 256
        z_b = (y_b + k + x + y) % 256

        imagen_cifrada.putpixel((x, y), (z_r, z_g, z_b, a))

# Guardar imagen cifrada
imagen_cifrada.save(ruta_cifrada)

print("\nImagen cifrada correctamente.")
print(f"Imagen guardada en: {ruta_cifrada}")

# Mostrar original y cifrada
os.startfile(ruta)
os.startfile(ruta_cifrada)

# =======================
# VERIFICAR CLAVE
# =======================

clave_descifrado = input("\nIngrese la clave para descifrar la imagen: ")

m = 0
for letra in clave_descifrado:
    m += ord(letra)

if m != k:
    print("\nClave incorrecta. No es posible recuperar la imagen.")
    exit()

print("\nClave correcta.")
print("Iniciando proceso de descifrado...")

# =======================
# CAPA 3 (DESCIFRADO)
# =======================

for x in range(imagen_cifrada.width):
    for y in range(imagen_cifrada.height):

        z_r, z_g, z_b, a = imagen_cifrada.getpixel((x, y))

        y_r_rec = (z_r - k - x - y) % 256
        y_g_rec = (z_g - k - x - y) % 256
        y_b_rec = (z_b - k - x - y) % 256

        r_rec = (197 * (y_r_rec - 57)) % 256
        g_rec = (197 * (y_g_rec - 57)) % 256
        b_rec = (197 * (y_b_rec - 57)) % 256

        imagen_descifrada.putpixel((x, y), (r_rec, g_rec, b_rec, a))

# Guardar imagen recuperada
imagen_descifrada.save(ruta_descifrada)

print("\nImagen recuperada correctamente.")
print(f"Imagen guardada en: {ruta_descifrada}")

# Verificación
if list(imagen.getdata()) == list(imagen_descifrada.getdata()):
    print("Verificación exitosa: la imagen recuperada coincide con la original.")
else:
    print("Error: la imagen recuperada no coincide con la original.")

# Mostrar imagen recuperada
os.startfile(ruta_descifrada)