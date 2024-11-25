#Inmutabilidad: No se puede cambiar el orden ni el contenido del string.
#nombre = "Federico"
#nombre[0] = "T"
#print(nombre)

#Concatenacion: Se pueden concatenar los strings
#nombre = "Fede"
#nombre2= "rico"
#print (nombre + nombre2)

#Multiplicacion: Se repite la cadena las veces que quiera el usuario
#nombre = "Fede"
#print (nombre*8)

#Saltos de lineas: Se escribe con 3 comillas (Simples o Dobles)
#lo que hace es escribir el texto en distintas lineas
#nombre = """Federico
#Como estas?"""
#print(nombre)

#Preguntar si existe una palabra en la cadena
#Devuelve valores booleanos (True o False)
#nombre = "Federico Martin Villoria"
#print("Martin" in nombre)
#Preguntar si no existe una palabra en la cadena
#nombre = "Federico Martin Villoria"
#print("Martin" not in nombre)

#Largo de una cadena de texto
#nombre = "Federico Martin Villoria"
#print(len(nombre))

#Practica de Propiedades de String 1:
#Concatena 15 veces el texto "Repetición" y muestra el resultado en pantalla. Por suerte, conoces que los strings son multiplicables y puedes realizar esta actividad de forma simple y elegante.
texto = "Repetición"
print("Repetición"*15)

#Practica de Propiedades de String 2:
#Verifica si la palabra "agua" no se encuentra en el siguiente haiku. Debes imprimir el booleano.
frase = """Tierra mojada,
mis recuerdos de viaje
entre las lluvias"""
print("agua" not in frase)

#Practica de Propiedades de String 3:
#Muestra en pantalla el largo (en números de caracteres) de la palabra electroencefalografista.
palabra = "electroencefalografista"
print(len(palabra))