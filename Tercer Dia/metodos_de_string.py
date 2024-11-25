texto = "Este es el texto de Federico"
#Devuelve la cadena todo en MAYUSCULA
#resultado = texto.upper()
#Devuelve el caracter del indice en mayuscula
#resultado = texto[2].upper()

#Devuelve la cadena todo en MINUSCULA
#resultado = texto.lower()
#Devuelve el caracter del indice en minuscula
#resultado = texto[2].lower()

#Devuelve la cadena separada en palabras
#resultado = texto.split()
#Devuelve la cadena separada segun el criterio de las ""
#resultado = texto.split("t")
#print(resultado)

#Join va a tomar todos los elementos que incluyamos en el parentesis
#y los separa con el caracter de la variable "e". En este caso es un espacio.
#a = "aprender"
#b = "Python"
#c = "es"
#d = "genial"
#e = " ".join([a,b,c,d])
#print(e)

#Find sirve para buscar los caracteres en una cadena de texto
#resultado = texto.find("s")
#Replace sirve para reemplazar una palabra o caracter por otra
#resultado = texto.replace("Federico", "Juan")
#print(resultado)

#Practica Metodos Strings 1:
#Imprime el siguiente texto en mayúsculas, empleando el método específico de strings:
frase = "Especialmente en las comunicaciones electrónicas, la escritura enteramente en mayúsculas equivale a gritar."
print(frase.upper())

#Practica Metodos Strings 2:
#Une la siguiente lista en un string, separando cada elemento con un espacio.
#Utiliza el método apropiado de listas/strings, y muestra en pantalla el resultado.
lista_palabras = ["La","legibilidad","cuenta."]
palabras = "La legibilidad cuenta."
resultado = " ".join([palabras])
print(resultado)

#Practica Metodos Strings 3:
#Reemplaza en la siguiente frase:
#"Si la implementación es difícil de explicar, puede que sea una mala idea."
#los siguientes pares de palabras:
#"difícil" --> "fácil"
#"mala" --> "buena"
#y muestra en pantalla la frase con ambas palabras modificadas.
frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
resultado = frase.replace("difícil", "fácil").replace("mala", "buena")
print(resultado)