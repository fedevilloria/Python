#archivo = open("prueba.txt", "w") #Hace que el archivo se regenere completamente. Si existe, su texto sera reemplazado por el nuevo
#Si no existe, se creara un archivo nuevo

#archivo.write("Soy el nuevo texto") #No agrega el salto de linea automatico

#Para agregar distintas lineas se debe hacer asi:
#1RA Forma:
#archivo.write("Hola\n")
#archivo.write("Mundo")

#2DA Forma:
#archivo.write("""Hola
#mundo
#soy
#Federico""")

#Otra forma de escribir en el archivo
#Escribe toda en una misma linea y concatena todas juntas
#archivo.writelines(["Hola","mundo","soy","Federico"])

#Si queremos agregarle los saltos de linea desde una lista
#lista = ["Hola","mundo","soy","Federico"]
#for palabra in lista:
#    archivo.writelines(palabra + "\n")


#archivo = open("prueba.txt", "a") #Se posiciona en el ultimo caracter y agrega el texto
#archivo.write("bienvenido")

#archivo.close()

#Practica Archivos 1:
#Abre el archivo llamado "mi_archivo.txt", y cambia su contenido por el texto "Nuevo texto".
#Imprime el contenido completo de "mi_archivo.txt" al finalizar.
#Pista: deberás cerrarlo en modo escritura y volverlo a abrir en modo lectura.
archivo = open("mi_archivo.txt","w")
archivo.write("Nuevo texto")
archivo.close()
archivo = open("mi_archivo.txt")
print(archivo.read())
archivo.close()

#Practica Archivos 2:
#Abre el archivo llamado "mi_archivo.txt", y añade una línea al final del mismo que diga: "Nuevo inicio de sesión".
#Imprime el contenido completo de "mi_archivo.txt" al finalizar.
#Pista: deberás cerrarlo en modo escritura y volverlo a abrir en modo lectura.
archivo = open("mi_archivo.txt", "a")
archivo.write("Nuevo inicio de sesión")
archivo.close()
archivo = open("mi_archivo.txt")
print(archivo.read())
archivo.close()

#Practica Archivos 3:
#Utiliza el método writelines para escribir los valores de la siguiente lista al final del archivo "registro.txt" . Inserta un tabulador entre cada elemento de la lista para separarlos.
#Imprime el contenido completo de "registro.txt" al finalizar.
#Pista: recuerda que el símbolo para concatenar un tabulador en un string es \t. También, deberás cerrar el archivo en modo escritura y volverlo a abrir en modo lectura para poder imprimir su contenido.
registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

registro = open("registros.txt", "a")
for item in registro_ultima_sesion:
    registro.writelines(item + "\t")

registro.close()
registro = open("registros.txt")
print(registro.read())
registro.close()



