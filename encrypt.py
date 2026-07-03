
# Convertir la clave textual en un valor numérico
clave = input("Ingrese una clave: ")

suma = 0

for letra in clave:
    suma = suma + ord(letra)

k = suma

# Píxel de prueba
x = 120

# Capa 1: función biyectiva
y = (13 * x + 57) % 256

# Capa 2: suma modular usando la clave
z = (y + k) % 256

#capa 3 Descifrado
# quitar la clave
y_recuperado = (z - k) % 256

# aplicar la función inversa
x_recuperado = (197 * (y_recuperado - 57)) % 256  # 197 es el inverso modular de 13 módulo 256 (13⁻¹ mod 256 = 197)

print("Valor de k:", k)
print("Valor original:", x)
print("Después de la función biyectiva:", y)
print("Valor cifrado:", z)
print("y recuperado:", y_recuperado)
print("x recuperado:", x_recuperado)