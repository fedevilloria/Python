from random import *
palabras = ["ahorcado", "futbol", "argentina", "computadora", "juego"]

def elegir_palabra():
    palabra_programa = choice(palabras)
    return palabra_programa

def palabra_oculta():
    for letras in palabra_programa:
        palabra_ahorcado  = print("-")
        lista = list(palabra_ahorcado)
        return palabra_ahorcado

def pedir_letra():
    letra_usuario = input("Ingrese una letra: ")
    return

palabra_elegida = elegir_palabra()
vida = 6
while vida != 0:
    letra = print(pedir_letra())
    if str(letra) in palabra_elegida:
        palabra_oculta()
        lista.replace()
    else:
        print("La letra no esta en la palabra")
        vida = vida - 1
        print (f"Te quedan {vida} vidas.")