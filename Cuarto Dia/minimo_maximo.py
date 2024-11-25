#menor = min(1,23,4,5,745,74,-123)
#print(menor)

#mayor = max(1,24,5,213,45,12,56,643)
#print(mayor)

#lista = [0,421,5124,512,5,32,5,-123,-52]
#print(f"El menor de su lista es {min(lista)} y el mayor es {max(lista)}")

#nombres = ["Juan", "Pablo", "Alicia", "Carlos"]
#print(f"El primero en la lista es {min(nombres)} y el ultimo sera {max(nombres)}")

#nombre = "Carlos"
#print(min(nombre.lower()))

#dic = {"C1":45, "C2":11}
#print(min(dic.values()))

#Practica Minimo y Maximo 1:
#Obtén el valor máximo entre los valores de la siguiente lista, y almacénalo en una variable llamada valor_maximo:
lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5]
valor_maximo = max(lista_numeros)

#Practica Minimo y Maximo 2:
#Calcula la diferencia entre el valor máximo y el mínimo en la siguiente lista de números, y almacénalo en una variable llamada rango:
lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]
rango = max(lista_numeros) - min(lista_numeros)

#Practica Minimo y Maximo 3:
#Utilizando max(), min() y métodos de diccionarios, obtén el mínimo valor a partir del siguiente diccionario:
#diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}
#Almacena dicho valor en una variable llamada edad_minima.
#También, obtén el nombre que se ubica último en orden alfabético, y almacénalo en una variable llamada ultimo_nombre.

diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}
edad_minima = min(diccionario_edades.values())
ultimo_nombre = max(diccionario_edades)