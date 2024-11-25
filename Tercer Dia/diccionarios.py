#diccionario = {"c1":"valor1", "c2":"valor1"}
#print(diccionario)

#Buscar el valor indicado por la clave
#resultado = diccionario["c1"]
#print(resultado)

#cliente = {"nombre":"Juan", "apellido":"Fuentes","peso":65, "talla":1.67}
#consulta = cliente["apellido"]
#print(consulta)

#dic = {"c1":55, "c2":[10, 20, 30], "c3":{"s1":100, "s2":200}}
#print(dic["c3"]["s2"])

#De este diccionario agarra la letra e y convertirla en mayuscula
#en una linea de codigo
#dic = {"c1":["a", "b", "c"], "c2":["d", "e", "f"]}
#print(dic["c2"][1].upper())

#Agregar valores a los diccionarios
dic = {1:"a", 2:"b"}
print(dic)
dic[3] = "c"
print(dic)
##Pisar los valores del diccionario y modificarlos
dic[2] = "b".upper()
print(dic)
#Imprime unicamente las llaves
print(dic.keys())
#Imprime unicamente los valores
print(dic.values())
#Imprime todos los elementos del diccionario
print(dic.items())

#Practica Diccionarios 1:
#Crea un diccionario llamado mi_dic que almacene la siguiente información de una persona:
#nombre: Karen
#apellido: Jurgens
#edad: 35
#ocupacion: Periodista
#Los nombres de las claves y valores deben ser iguales a la consigna.
mi_dic = {"nombre":"Karen","apellido":"Jurgens","edad":35,"ocupacion":"Periodista"}
print(mi_dic)

#Practica Diccionarios 2:
#Crea una función print que devuelva del segundo item de la lista llamada points2, dentro del siguiente diccionario.
#Si el valor 300 cambiara en el futuro, el código debería funcionar igual para devolver el valor que se encuentre en esa misma posición. Para ello, deberás hacer referencia a los nombres de las claves y/o índices según corresponda.
mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(mi_dict["puntos"]["points2"][1])

#Practica Diccionarios 3:
#Actualiza la información de nuestro diccionario llamado mi_dic  (reasignando nuevos valores a las claves según corresponda), y agrega una nueva clave llamada "pais" (sin tilde). Los nuevos datos son:
#nombre: Karen
#apellido: Jurgens
#edad: 36
#ocupacion: Editora
#pais: Colombia
#para ello, no debes cambiar la línea de código ya escrita, sino actualizar los valores mediante métodos de diccionarios.
mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}
mi_dic["edad"]= 36
mi_dic["ocupacion"] = "Editora"
mi_dic["pais"]= "Colombia"
print(mi_dic)












