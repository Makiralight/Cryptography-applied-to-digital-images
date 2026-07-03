
clave = input("Ingrese una clave: ")

suma = 0

for letra in clave:
    suma = suma + ord(letra)

k = suma % 256

print("Valor de k:", k)
