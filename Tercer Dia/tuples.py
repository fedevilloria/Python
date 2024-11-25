#INMUTABLES
#mi_tuple = (1,2,3,4)
#print(mi_tuple[0])

#t = (5,6.5,"F")
#print(t)

#Siempre que coincida la cantidad de valores se puede asignar a otra variable
#t = (1,2,3)
#x,y,z = t
#print(x,y,z)

#Cuantas veces aparece el 1 en una tupla
#t = (1,2,3,1)
#print(t.count(1))
#Consulto el indice de un valor
#print(t.index(3))

#Practica Tuples 1:
#Utiliza un método de tuplas para contar la cantidad de veces que aparece el valor 2 en la siguiente tupla, y muestra el resultado (integer) en pantalla:
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
print(mi_tupla.count(2))

#Practica Tuplas 2:
#Convierte a lista la siguiente tupla, y almacénala en una variable llamada mi_lista.
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)
mi_lista = list(mi_tupla)

#Practica Tuplas 3:
#Extrae los elementos de la siguiente tupla en cuatro variables: a, b, c, d
mi_tupla = (1, 2, 3, 4)
a,b,c,d = mi_tupla