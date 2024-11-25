from random import *

#aleatorio = randint(1,50) #Elige un numero aleatorio entre el rango declarado
#print(aleatorio)

#aleatorio = round(uniform(1,5),1) #Elige un numero aleatorio pero decimal.
#Con el ,1 le digo que me redondee en una decima
#print(aleatorio)

#aleatorio = random() #Elige un numero aleatorio entre el 0 y 1.
#print(aleatorio)

#colores = ["azul", "rojo", "verde", "amarillo"]
#aleatorio = choice(colores) #Choice elige aleatoriamente un elemento de una lista
#print(aleatorio)

#numeros = list(range(5,50,5))
#shuffle(numeros) #Desordena de forma aleatoria una lista en el lugar
#No se puede usar en los strings
#print(numeros)

#Practica Random 1:
#Implementa la función randint() de la librería random que te permita obtener un número entero del 1 al 10, y almacena dicho valor en una variable llamada aleatorio
aleatorio = randint(1,10)
print(aleatorio)

#Practica Random 2:
#Implementa la función random() de la librería random que te permita obtener un número decimal entre 0 y 1, y almacena dicho valor en una variable llamada aleatorio
aleatorio = random()
print(aleatorio)

#Practica Random 3:
#Utiliza el método choice() de la librería random para obtener un elemento al azar de la lista de nombres a continuación, y almacena el nombre escogido en una variable llamada sorteo.
nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]
sorteo = choice(nombres)
print(sorteo)