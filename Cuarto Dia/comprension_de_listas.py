#palabra = "python"
#lista = [letra for letra in palabra] #Una letra por cada letra que hay en palabra

#Otra manera de hacerlo es:
#lista = [letra for letra in "python"] #Queda todo en una sola linea
#print(lista)

#lista = [numero for numero in range(0,21,2)]
#print(lista)

#lista = [numero / 2 for numero in range(0,21,2)] #Se puede alterar el numero antes
#de incluirlo en la lista
#print(lista)

#lista = [numero for numero in range(0,21,2) if numero*2 > 10] #Es con el if
#print(lista)

#lista = [numero if numero*2 > 10 else "No" for numero in range(0,21,2)] #Con el else
#si o si se pone antes de que comience el "for"
#print(lista)

#pies = [10,20,30,40,50]
#metros = [pie * 3.281 for pie in pies]
#print(metros)

#Practica Comprension de lista 1:
#Para realizar el ejercicio a continuación, puedes optar por diferentes caminos. Si bien en programación el camino correcto es el que devuelve el resultado correcto, te animo a que intentes aplicar los conceptos de comprensión de listas para comenzar a afianzarlos para el futuro. ¡Pueden resultarte muy útiles en tu práctica profesional!
#Crea una lista valores_cuadrado formada por los números de la lista valores, elevados al cuadrado.

valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_cuadrado = [valor ** 2 for valor in valores]
print(valores_cuadrado)

#Practica Comprension de lista 2:
#Crea una lista valores_pares formada por los números de la lista valores que (¡adivinaste!) sean pares.
valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_pares = [numero for numero in valores if numero % 2 == 0 ]
print(valores_pares)

#Practica Comprension de lista 3:
#Para la siguiente lista de temperaturas en grados Fahrenheit, expresa estos mismos valores en una nueva lista de valores de temperatura en grados Celsius. La conversión entre tipo de unidades es la siguiente:
#°C = (°F - 32) * (5/9)
#o expresado de otro modo:
#(grados_fahrenheit-32)*(5/9)

temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [(fahrenheit - 32) * (5 / 9) for fahrenheit in temperatura_fahrenheit]
print(grados_celsius)