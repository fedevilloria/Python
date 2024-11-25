#lista = ["a","b","c"]
#for item in enumerate(lista): #Enumerate sirve para indicar la posicion y el valor
#que tiene esa posicion
#    print(item)

#for indice, item in enumerate(lista): #Otra forma de representar las enumeraciones
#    print(indice, item)

#for indice, item in enumerate(range(50,56)): #Forma de representar dentro de un rango
#    print(indice, item)

#mis_tuples = list(enumerate(lista)) #Lo podemos guardar de manera en tuplas
#print(mis_tuples)

#Practica Enumerador 1:
#Imprime en pantalla frases como la siguiente:
#'{nombre} se encuentra en el índice {indice}'
#Donde nombre debe ser cada uno de los nombres de la lista a continuación, y el índice, obtenido mediante enumerate().
#lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indice, nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}')

#Practica Enumerador 2:
#Crea una lista formada por las tuplas (indice, elemento), formadas a partir de obtener mediante enumerate() los índices de cada caracter del string "Python".
#Llama a la lista obtenida con el nombre de variable lista_indices

lista_indices = list(enumerate("Python"))

#Practica Enumerador 3:
#Imprime en pantalla únicamente los índices de aquellos nombres de la lista a continuación, que empiecen con M:
#lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
#Puedes resolverlo de diferentes maneras, pero servirá que tengas presente todos o algunos de los siguientes elementos:
#Loops
#Condicionales if
#El método enumerate()
#Métodos de strings o indexado

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indice, nombre in enumerate(lista_nombres):
    if nombre.startswith("M"):
        print(indice)