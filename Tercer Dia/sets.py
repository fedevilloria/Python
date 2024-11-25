#mi_set = set([1,2,3,4,5])
#print(type(mi_set))
#print(len(mi_set))
#print(mi_set)

#otro_set = {1,2,3}
#print(type(otro_set))
#print(otro_set)

#s1 = {1,2,3}
#s2 = {3,4,5}
#s3 = s1.union(s2)

#Agregar elementos al set
#s1.add(4)
#print(s1)
#Eliminar un elemento del set
#s1.remove(3)
#print(s1)
#Descartar elementos (Es parecido al remove pero si el elemento no se encuentra en la
#lista, no tira error)
#s1.discard(5)
#print(s1)
#Eliminar un elemento aleatorio
#sorteo = s1.pop()
#print(sorteo)
#Limpiar el set
#s1.clear()
#print(s1)

#Practica Sets 1:
#Une los siguientes sets en uno solo, llamado mi_set_3:
mi_set_1 = {1, 2, "tres", "cuatro"}
mi_set_2 = {"tres", 4, 5}
mi_set_1 = tuple(mi_set_1)
mi_set_2 = tuple(mi_set_2)
mi_set_3 = mi_set_1 + mi_set_2
mi_set_3 = set(mi_set_3)
print(mi_set_3)
print(type(mi_set_3))

#Practica Sets 2:
#Elimina un elemento al azar del siguiente set, utilizando métodos de sets.
sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo.pop()
print(sorteo)

#Practica Sets 3:
#Agrega el nombre Damián al siguiente set, utilizando métodos de sets:
sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo.add("Damián")
print(sorteo)