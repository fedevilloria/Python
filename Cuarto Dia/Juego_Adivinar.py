from random import *
print("Bienvenido al juego de adivinanza")
nombre = input("Ingrese su nombre: ")
numero_secreto = int(randint(1, 100))
numero_jugador = 0
intentos = 8
print(f"Hola {nombre} he pensado un numero del 1 al 100. Tienes 8 intentos para adivinar cual es el numero.")


while intentos > 0:
    numero_jugador = int(input("Ingrese su numero: "))
    print(" ")
    if numero_jugador < 1 or numero_jugador > 100:
        print("Por favor elije un numero del 1 al 100.")
        continue
    elif numero_jugador < numero_secreto:
        print("Respuesta incorrecta. Tu numero esta por debajo del que pense.")
        intentos = intentos - 1
        print("Te quedan ", intentos, " intentos.")
        print(" ")
    elif numero_jugador > numero_secreto:
        print("Respuesta incorrecta. Tu numero esta por encima del que pense.")
        intentos = intentos - 1
        print("Te quedan ", intentos, " intentos.")
        print(" ")
    else:
        print("FELICITACIONES!!\nAdivinaste el numero!!!!")
        intentos = intentos - 1
        print(f"Te sobraron {intentos} intentos.")
        break
if numero_jugador != numero_secreto:
    print(f"Lo siento, se han acabado los intentos. El numero secreto era {numero_secreto}.")