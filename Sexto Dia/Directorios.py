import os
from pathlib import Path

#ruta = os.getcwd() #Sirve para ver en que ruta se ubica el archivo actual
#print(ruta)

#ruta = os.chdir("D:\\asd") #Sirve para cambiar el directorio del archivo
#archivo = open("texto_busqueda.txt")
#print(archivo.read())

#ruta = os.makedirs("D:\\asd\\Otra") #Sirve para crear una carpeta en una ruta

#print(archivo.read())

#ruta = "D:\\asd\\Otra"
#elemento = os.path.basename(ruta) #Nombre de base de toda la ruta (el ultimo elemento)
#print(elemento)

#elemento = os.path.dirname(ruta) #Direccion de la ruta sin el ultimo elemento
#print(elemento)

#elemento = os.path.split(ruta) #Crea una tupla con los 2 elementos por separado
#en el principio aparece el "dirname" y al final el "basename"
#print(elemento)

#os.rmdir("D:\\asd\\Otra") #Sirve para remover la base de la direccion (el ultimo elemento)

#otro_archivo = open("D:\\asd\\texto_busqueda.txt") #Abrir un archivo especifico dentro de la computadora
#buscandolo a traves de una ruta sin el metodo os
#print(otro_archivo.read())

#carpeta = Path("D:/asd") #Esto sirve para poder abrir los directorios en cualquier sistema operativo
#Tambien se puede eliminar el "D:" y serviria igual
#archivo = carpeta / "texto_busqueda.txt" #Concatenamos el archivo el cual necesitamos abrir
#mi_archivo = open(archivo)
#print(mi_archivo.read())