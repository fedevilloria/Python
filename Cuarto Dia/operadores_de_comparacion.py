#COMPARACION "=="
#mi_variable = "Hola mundo" #El = solo es para asignar un valor a algo
#comparacion = 10 == 25 #El doble = es para comparar si son iguales o equivalentes
#print(comparacion)

#comparacion2 = 5+5 == 18-8 #Se puede hacer con operaciones tambien. Compara los resultados.
#print(comparacion2)

#comparacion3 = "blanco" == "negro" #Se puede hacer con strings.
#Las mayusculas se tienen en cuenta.
#print(comparacion3)

#comparacion4 = 100.0 == 100 #Se puede hacer comparando enteros con floats
#print(comparacion4)

#DIFERENCIA "!="
#diferencia = 100.0 != 100 #Pregunto si son DISTINTOS los valores
#En este caso son iguales por lo que arrojaria valor Falso.
#print(diferencia)

#MAYOR ">"
#mayor = 24 > 25 #Pregunto si un numero es mayor que otro
#print(mayor)

#MAYOR O IGUAL ">="
#mayor_igual = 25 >= 25 #Pregunto si un numero es mayor o igual que el otro
#print(mayor_igual)

#MENOR "<"
#menor = 24 < 25 #Pregunto si un numero es menor que otro
#print(menor)

#MENOR O IGUAL "<="
#menor_igual = 24 <= 24 #Pregunto si un numero es menor o igual que otro
#print(menor_igual)

#Practica Operadores de Comparacion 1:
#Crea dos variables (num1 y  num2) con los valores 36 y 17 respectivamente. Verifica si num1 es mayor o igual que num2 y almacena el resultado de dicha comparación en una variable llamada mi_bool

num1 = 36
num2 = 17
mi_bool = num1 >= num2
print(mi_bool)

#Practica Operadores de Comparacion 2:
#Crea dos variables (num1 y  num2):
#Dentro de num1, almacena el resultado de la operación raíz cuadrada de 25
#Dentro de num2, almacena el número 5.
#Verifica si num1 es igual a num2 y almacena el resultado de dicha comparación en una variable llamada mi_bool.

num1 = 25 ** 0.5 #Calculo de raiz cuadrada
num2 = 5
mi_bool = num1 == num2
print(mi_bool)

#Practica Operadores de Comparacion 3:
#Crea dos variables (num1 y  num2):
#Dentro de num1, almacena el resultado de la operación 64 x 3
#Dentro de num2, almacena el resultado de la operación 24 x 8
#Verifica si num1 es diferente a num2 y almacena el resultado de dicha comparación en una variable llamada mi_bool.

num1 = 64 * 3
num2 = 24 * 8
mi_bool = num1 != num2
print(mi_bool)