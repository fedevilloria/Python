#Abrir un archivo ya existente
#mi_archivo = open("prueba.txt")

#Leer un archivo
#print(mi_archivo.read()) #Con read lo que hacemos es leer el archivo
                        #una vez que lo imprimimos nos aparece el contenido del archivo

#READLINE
#print(mi_archivo.readline()) #Lee una sola linea

#una_linea = mi_archivo.readline()
#print(una_linea) #Primera linea

#una_linea = mi_archivo.readline()
#print(una_linea) #Segunda linea
#una_linea = mi_archivo.readline()
#print(una_linea.rstrip()) #rstrip lo que hace es borrar el salto de linea automatico generado por el archivo txt

#una_linea = mi_archivo.readline()
#print(una_linea) #Tercera linea

#Se puede iterar en las lineas
#for linea in mi_archivo:
#    print("Aqui dice: " + linea)


#READLINES
#todas = mi_archivo.readlines() #Transforma el archivo a una lista
                                #Se le puede aplicar todos los metodos de listas
#print(todas)

#Se debe cerrar para tener prudencia
#mi_archivo.close()

#Practica Archivos 1:
#Abre el archivo texto.txt e imprime su contenido.

mi_archivo = open("texto.txt")
print(mi_archivo.read()) #Sirve para imprimir el contenido del archivo

#Practica Archivos 2:
#Imprime la primera línea del archivo texto.txt
#No olvides abrir el archivo y cerrarlo luego de ejecutar tu código.

mi_archivo = open("texto.txt")
print(mi_archivo.readline())
mi_archivo.close()

#Practica Archivos 3:
#Abre el archivo texto.txt e imprime únicamente la segunda línea.
archivo = open("texto.txt")
una_linea = archivo.readline() #Leo la primera linea
una_linea = archivo.readline() #Leo la segunda y sobreescribo la variable
print(una_linea) #Imprimo la segunda ya que es la ultima que se guardo en la variable