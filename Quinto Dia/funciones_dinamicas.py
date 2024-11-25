#lista = [1,52,6346,2345,12,523,5325,263]
#def chequear_3_cifras(lista):
#    for n in lista:
#        if n in range(100,1000):
#            return True
#        else:
#            pass
#resultado = chequear_3_cifras(lista)
#print(resultado)

#lista = [1,52,6346,2345,12,523,5325,263]
#def chequear_3_cifras(lista):
#    for n in lista:
#        if n in range(100,1000):
#            return True
#        else:
#            pass
#    return False #Devolvemos Falso en caso de que no haya ninguno
    #que cumpla con la condicion del if
#resultado = chequear_3_cifras(lista)
#print(resultado)


#lista = [1,52,646,2345,12,523,5325,263]
#def chequear_3_cifras(lista):
#    lista_3_cifras = []
#    for n in lista:
#        if n in range(100,1000):
#            lista_3_cifras.append(n) #Lo que hace es que a cada valor de 3
#            #cifras lo guarda en un vector vacio
#        else:
#            pass
#    return lista_3_cifras #Luego cuando termina el for devuelve esa lista con
            #los numeros guardados
#resultado = chequear_3_cifras(lista)
#print(resultado)

#Practica Funciones Dinamicas 1:
#Crea una función (todos_positivos) que reciba una
# #lista de números como parámetro, y
# devuelva True si todos los valores de una lista
# son positivos, y False si al menos uno de los
# valores es negativo. Crea una lista
# llamada lista_numeros con valores positivos y negativos.

lista_numeros = [-1, -125, 1, 457, 5290, -6348]
def todos_positivos(lista_numeros):
    for n in lista_numeros:
        if n < 0:
            return False
        else:
            pass
    return True
print(todos_positivos(lista_numeros))

#Practica Funciones Dinamicas 2:
#Crea una función (suma_menores) que sume los números de una lista (almacenada en la variable lista_numeros) siempre y cuando sean mayores a 0 y menores a 1000, y devuelva el resultado de dicha suma.

#lista_numeros = [124,-235,34603,743,6356,-1234]
#def suma_menores(lista_numeros):
#   suma = 0
#    for numero in lista_numeros:
#        if numero > 0 and numero < 1000:
#            suma = suma + numero
#        else:
#            pass
#    return suma
#print(suma_menores(lista_numeros))

#Practica Funcion Dinamicas 3:
#Crea una función (cantidad_pares) que cuente la cantidad de números pares que existen en una lista (lista_numeros), y devuelva el resultado de dicha cuenta.
lista_numeros = [2,5,677,42,734,645,457,776]
def cantidad_pares(lista_numeros):
    pares = 0
    for n in lista_numeros:
        if n % 2 == 0:
            pares = pares + 1
        else:
            pass
    return pares
print(cantidad_pares(lista_numeros))