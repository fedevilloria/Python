import os
from pathlib import *
from os import system

ruta_raiz = Path(Path.home(), "Recetas")

def contar_recetas(ruta):
    contador = 0
    for archivo in Path(ruta_raiz).glob("**/*.txt"):
        contador = contador + 1
    return contador

def inicio():
    system("cls")
    print("-" * 50)
    print(" " * 5 + " Bienvenido al administrador de recetas " + " " * 5)
    print("-" * 50)
    print("\n")
    print(f"Las recetas se encuentran en {ruta_raiz}")
    print(f"Total de recetas enconctradas: {contar_recetas(ruta_raiz)}")

    eleccion_menu = "x"
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1, 7):
        print("Elige una opcion:")
        print("""
        1) Leer receta
        2) Crear receta nueva
        3) Crear categoria nueva
        4) Eliminar receta
        5) Eliminar categoria
        6) Salir""")
        eleccion_menu = input()
    return eleccion_menu

def mostrar_categorias(ruta):
    print("Categorias:")
    ruta_categorias = Path(ruta)
    lista_categorias = []
    contador = 1
    for carpeta in ruta_categorias.iterdir():
        carpeta_str = str(carpeta.name)
        print(f"{contador}) {carpeta_str}")
        lista_categorias.append(carpeta)
        contador = contador + 1
    return lista_categorias

def elegir_categorias(lista):
    eleccion_correcta = "x"
    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1, len(lista) + 1):
        eleccion_correcta = input("\nElige una categoria: ")
    return lista[int(eleccion_correcta) - 1]

def mostrar_recetas(ruta):
    print("Recetas:")
    ruta_recetas = Path(ruta)
    lista_rectas = []
    contador = 1
    for receta in ruta_recetas.glob("*.txt"):
        receta_str = str(receta.name)
        print(f"{contador}) {receta_str}")
        lista_rectas.append(receta)
        contador = contador + 1
    return lista_rectas

def elegir_recetas(lista):
    eleccion_receta = "x"
    while not eleccion_receta.isnumeric() or int(eleccion_receta) not in range(1, len(lista) + 1):
        eleccion_receta = input("\nElige una receta: ")
    return lista[int(eleccion_receta) - 1]



#Mostrar menu inicio
menu = 0
if menu == 1:
    mis_categorias = mostrar_categorias(ruta_raiz)
    mi_categoria = elegir_categorias(mis_categorias)
    mis_recetas = mostrar_recetas(mi_categoria)
    mi_receta = elegir_recetas(mis_recetas)
    #Leer receta
    #Volver al inicio
    pass
elif menu == 2:
    mis_categorias = mostrar_categorias(ruta_raiz)
    mi_categoria = elegir_categorias(mis_categorias)
    #Crear una receta nueva
    #Volver al inicio
    pass
elif menu == 3:
    #Crear categoria
    #Volver al inicio
    pass
elif menu == 4:
    mis_categorias = mostrar_categorias(ruta_raiz)
    mi_categoria = elegir_categorias(mis_categorias)
    mis_recetas = mostrar_recetas(mi_categoria)
    mi_receta = elegir_recetas(mis_recetas)
    #Eliminar receta
    #Volver al inicio
    pass
elif menu == 5:
    mis_categorias = mostrar_categorias(ruta_raiz)
    mi_categoria = elegir_categorias(mis_categorias)
    #Elminar categoria
    #Volver al inicio
    pass
elif menu == 6:
    #Finalizar programa
    pass