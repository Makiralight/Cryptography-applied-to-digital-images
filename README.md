# Cryptography-applied-to-digital-images

## Resumen
El presente proyecto consta del desarrollo de un algoritmo criptográfico en python capaz de almacenar el contenido de una imagen determinada de manera que su contenido no sea visible hasta asociarse con una clave definida en el algoritmo.
Este planteamiento surge de la necesidad de proteger la información contenida en las imágenes mediante una herramienta sencilla y accesible que, aplicando conceptos fundamentales de matemáticas discretas como aritmética modular y funciones biyectivas, permite cifrar una imagen y recuperarla únicamente cuando se ingrese la clave correcta.

## Instrucciones de uso
### Dependencias
Para ejecutar el código se debe instalar las librerías 
  - Pillow
  - Tkinter

Y contar con acceso a la librería Os, usualmente incluída en la instalación base de python.

Para instalar  la libreria Pillow:
```
pip install Pillow
```

Para verificar la instalación de Tkinter en Python
```
python -m tkinter
```

### Ejecución

El código del cifrado de imágenes corresponde al archivo "encrypt_image.py". Al ejecutar el código, en terminal aparecerá un mensaje que dice "Ingrese una clave: ". Se digitará una clave a elección del usuario que el usuario debe recordar. Una vez se envíe al programa dicha clave. Se abrirá una ventana del explorador de archivos donde se seleccionará la imagen a cifrar don un doble clic. Finalmente, el código mostrará la imagen codificada y ofrece la opción de reingresar la clave nuevamente para proceder con la recuperación de la imagen. De ser correcta, la imagen original se mostrará en pantalla.

<img width="1270" height="624" alt="imagen" src="https://github.com/user-attachments/assets/bbe862d3-1b3c-4030-92f0-aea85923c754" />


### Ejemplo de funcionamiento

Imagen sin codificar
<img width="887" height="496" alt="imagen" src="https://github.com/user-attachments/assets/26018650-706e-486a-a3a3-344162dd15ac" />

Imagen codificada
<img width="914" height="457" alt="imagen" src="https://github.com/user-attachments/assets/d720d746-7152-4a4d-a2ad-6ab4f85e1143" />

