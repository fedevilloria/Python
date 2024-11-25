#for numero in range(5): #Imprimo todos los numeros que van hasta el 5 sin incluirlo
#Del 0 al 4. (Cinco posiciones)
    #print(numero)

#for numero in range(1,5): #El primer parametro indica el inicio y el ultimo el final (Sin incluirlo).
    #print(numero)

#for numero in range (1,5,2): #El ultimo parametro indica el paso.
#En este caso lee de 2 en 2. Porque el paso es 2.
#Si no se pone nada seria paso 1. De uno en uno.
    #print(numero)

#lista = list(range(1,101)) #Crea una lista del 1 al 100
#print(lista)

#Practica Rango 1:
#Crea una lista formada por todos los números desde el 2500 al 2585 (inclusive). Almacena dicha lista en la variable mi_lista.
#mi_lista = list(range(2500,2586))

#Practica Rango 2:
#Utilizando la función range(), crea en una única linea de código una lista formada por todos los números múltiplos de 3 desde el 3 al 300 (inclusive). Almacena dicha lista en la variable mi_lista.
#mi_lista = list(range(3,301,3))

#Practica Rango 3:
#Utiliza la función range() y un loop para sumar los cuadrados de todos los números del 1 al 15 (inclusive). Almacena el resultado en una variable llamada suma_cuadrados.
#Para ello:
#Crea un rango de valores que puedas recorrer en un loop
#Para cada uno de estos valores, calcula su valor al cuadrado (potencia de 2). Puede que necesites crear variables intermedias (de manera opcional).
#Suma todos los valores al cuadrado obtenidos. Acumula la suma en la variable suma_cuadrados.

#MI SOLUCION
suma_cuadrado = 0
for numero in range(1,16):
        cuadrado = numero * numero
        suma_cuadrado = suma_cuadrado + cuadrado
        numero = numero + 1
print(suma_cuadrado)

#SOLUCION DE UDEMY
suma_cuadrados = 0
for numero in range(1,16):
    suma_cuadrados = suma_cuadrados + numero ** 2 #O suma_cuadrados += numero ** 2
print(suma_cuadrados)