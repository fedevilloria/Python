#Extraer una palabra y guardarla en otra variable
#texto = "ABCDEFGHIJKLM"
#fragmento = texto[2:5] #El 2 significa de donde comienza a leer
#El 5 es hasta que posicion va a extraer y guardar en la variable
#pero no lo incluye al caracter de esta posicion.
#print(fragmento)

#Extraer una palabra y guardarla en otra variable
#texto = "ABCDEFGHIJKLM"
#fragmento = texto[2:10:2] #El 2 significa de donde comienza a leer
#El 5 es hasta que posicion va a extraer y guardar en la variable
#pero no lo incluye al caracter de esta posicion.
#El ultimo 2 indica el paso. En este caso va de 2 en 2. Tampoco incluye
#el ultimo caracter (indice 10)
#print(fragmento)

#Si no se escribe nada, python va a tomar que es de donde se arranca la cadena
#o hasta que se termina. Ej: [:5] - [6:].

#Extraer una palabra y guardarla en otra variable
#texto = "ABCDEFGHIJKLM"
#fragmento = texto[::-1] #El -1 en esa posicion indica que va a recorrer
#el vector al reves y va guardando los caracteres en la variable.
#Desde el fin hasta el principio (al reves).
#print(fragmento)

#Practica Fragmentar 1:
#Extrae la primera palabra de la siguiente frase utilizando slicing, y muéstrala en pantalla:
#"Controlar la complejidad es la esencia de la programación"
#Pista: "Controlar" tiene un largo de 9 caracteres.
frase = "Controlar la complejidad es la esencia de la programación"
fragmento = frase[0:9]
print(fragmento)

#Practica Fragmentar 2:
#Toma cada tercer caracter empezando desde el noveno
#hasta el final de la frase, e imprime el resultado.
#"Nunca confíes en un ordenador que no puedas lanzar por una ventana"
frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
fragmento = frase[8::3]
print(fragmento)

#Practica Fragmentar 3:
#Invierte la posición de todos los caracteres de la
#siguiente frase y muestra el resultado en pantalla.
#"Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
fragmento = frase[::-1]
print(fragmento)





