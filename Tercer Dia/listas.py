mi_lista = ["a", "b", "c"]
mi_lista2 = ["d","e","f"]
mi_lista3 = mi_lista+mi_lista2

#Pisar el valor de la posicion 0 por:
mi_lista3[0] = "alfa"

#Agrega valores a la lista:
mi_lista3.append("g")

#Eliminar valores de la lista:
eliminado = mi_lista3.pop(6)

#Ordena listas
lista = [3, 4, 6,2, 1, 0.5]
#El sort no puede ser almacenado en una variable
lista.sort()
print(lista)
#Ordena la lista al reves
lista.reverse()
print(lista)

#resultado = mi_lista[0:len(mi_lista)]
print(mi_lista3)
print(eliminado)
#print(len(mi_lista))
#print(type(mi_lista))

#Practica Listas 1:
#Crea una lista con 5 elementos, dentro de la variable mi_lista. Puedes incluir strings, booleanos, números, etc.
mi_lista = [1, 2, 3, 4, 5]

#Practica Listas 2:
#Agrega el elemento "motocicleta" a la siguiente lista de medios de transporte:
#medios_transporte = ["avión", "auto", "barco", "bicicleta"]
#No debes modificar la línea de código ya suministrada, sino que debes emplear el método apropiado de listas para añadir un nuevo elemento.
medios_transporte = ["avión", "auto", "barco", "bicicleta"]
medios_transporte.append("motocicleta")
print(medios_transporte)

#Practica Listas 3:
#Utiliza el método pop() para quitar el tercer elemento de la siguiente lista llamada frutas, y almacénalo en una variable llamada eliminado. Utiliza métodos de listas sin alterar la línea de código ya suministrada.
#manzana
#banana
#mango
#cereza
#sandía
frutas = ["manzana", "banana", "mango", "cereza", "sandía"]
eliminado = frutas.pop(2)
print(frutas, eliminado)