#lista = ["a", "b", "c"]

#for letra in lista: #El "letra" puede ir cualquier cosa, pero es importante que en el print
#aparezca la misma palabra.
    #print("Letra: " + letra)

#for letra in lista:
    #numero_letra = lista.index(letra) + 1
    #print(f"Letra {numero_letra}: {letra}")

#lista = ["Pablo", "Laura", "Fede", "Cristian", "Lionel"]
#for nombre in lista:
    #if nombre.startswith("L"): #StartWith sirve para ver si un elemento comienza con esa letra.
        #print(nombre)
    #else:
        #print("Nombre que no comienza con 'L'")

#numeros = [1,2,3,4,5]
#mi_valor = 0

#for numero in numeros:
    #mi_valor = mi_valor + numero
#print(mi_valor)

#palabra = "python"
#for letra in palabra:
    #print(letra)

#for letra in "python": #Tambien se puede hacer en el ciclo sin declarar variables
    #print(letra)

#for numero in [1,2,3]: #Lo mismo pasa con los numeros o con listas o con tuplas
    #print(numero)

#for a,b in [[1, 2], [3, 4], [5, 6]]: #'a' toma los primeros valores y 'b' los segundos
    #print(a)
    #print(b)

#dic = {"clave1": "a", "clave2": "b", "clave3": "c"}
#for a,b in dic.items():
    #print(a,b)

#Practica con Ciclo FOR 1:
#Utilizando loops For, saluda a todos los miembros de una clase, imprimiendo "Hola" + su nombre.
#Por ejemplo: "Hola María"
#alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]
alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]
for nombre in alumnos_clase:
    print("Hola " + nombre)

#Practica con Ciclo FOR 2:
#Dada la siguiente lista de números, realiza la suma de todos los números utilizando loops For y almacena el resultado de la suma en una variable llamada suma_numeros:
#lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros = 0
for numero in lista_numeros:
    suma_numeros = suma_numeros + numero
print(suma_numeros)

#Practica con Ciclo FOR 3:
#Dada la siguiente lista de números, realiza la suma de todos los números pares e impares* por separado en las variables suma_pares y suma_impares respectivamente:
#lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0
for numeros in lista_numeros:
    if numeros % 2 == 0:
        suma_pares = suma_pares + numeros
    else:
        suma_impares = suma_impares + numeros
print(suma_pares)
print(suma_impares)