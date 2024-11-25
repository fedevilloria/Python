import os
from pathlib import *


nombre = input("Ingrese su nombre: ")
ruta = Path(Path.home(), "Recetas")

#Opcion 1:
def leer_receta():
    print("Que categoria desea elegir?")
    contenido = os.listdir()
    print(f"Elija una de las opciones: {contenido}")
    opcion = int(input(" "))


#Opcion 2:
def crear_receta():
    print("En que categoria desea crear su receta?")
    contenido = os.listdir(ruta)
    print(contenido)

#Opcion 3:
def crear_categoria():
    print("Que nombre desea para su nueva categoria?")
    nombre = input("Nombre de la categoria: ")
    categoria_nueva = os.makedirs()

print(f"Bienvenido {nombre} al recetario en linea. La carpeta de recetas se ubica en {ruta}.")
print(" ")
print("Seleccione una opcion, por favor:\n1- Elegir receta.\n2- Crear receta.\n3- Crear categoria.\n4- Eliminar receta.\n5- Eliminar categoria.\n6- Fin del programa.")
opcion = int(input("Opcion: "))
while opcion != 6:
    if opcion == 1:
        print("Que categoria desea elegir?")
        contenido = os.listdir(ruta)
        print(contenido)
        opcion_categoria = int(input(" "))
        if opcion_categoria == 1:
            carpeta_carnes = Path(Path.home(), "Carnes")
            for txt in Path(carpeta_carnes).glob("*.txt"):
                print(txt)

        break

    if opcion == 2:
        crear_receta()

    if opcion == 3:
        crear_categoria()
