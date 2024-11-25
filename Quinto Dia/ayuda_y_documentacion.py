dic = {"clave1": 100, "clave2": 500}
a = dic.popitem() #Elimina e imprime el valor suprimido
#En este caso es de tipo LIFO (Last in, first out)
#Osea que devolveria: "clave2": 500
print(a)
print(dic)
#Con control apretado podes ver de que se trata el objeto

#Si mantengo el cursor en el operador tira una ayuda en ingles
#Aparece un link debajo, el cual me lleva a la pagina de python
#Donde ahi se encuentra toda la documentacion

#Practica Ayuda 1:
#Remueve los caracteres a la izquierda de nuestro texto principal:
#,
#:
#%
#_
##
#Utiliza el método lstrip(). Imprime el resultado en pantalla:
texto = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#".lstrip(",:%_#")

#lstrip() Elimina todos los objetos de izquierda a derecha que
#se especifiquen dentro del parentesis
print(texto)

#Practica Ayuda 2:
#Añade el elemento "naranja" como el cuarto elemento de la siguiente lista "frutas", utilizando
#el método insert():

# insert(i,x) Inserta un nuevo elemento con valor x en el
# arreglo antes de la posición i.
# Si hay valores negativos son tratados como
# relativos a la posición final del arreglo.
frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
frutas.insert(3,"naranja")
print(frutas)

#Practica Ayuda 3:
#Verifica si los sets a continuación forman conjuntos
# aislados (es decir, que no tienen
# elementos en común), utilizando el
# método isdisjoint(). Almacena dicho resultado en la
# variable conjuntos_aislados:

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}
conjuntos_aislados = marcas_tv.isdisjoint(marcas_smartphones)
#isdisjoint() Retorna True si el conjunto no
# tienen ningún elemento en común con other.
# Dos conjuntos son disjuntos si y solo si su
# intersección es el conjunto vacío.
print(conjuntos_aislados)
