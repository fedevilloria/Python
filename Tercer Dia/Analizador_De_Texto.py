#Proyecto de ANALIZADOR DE TEXTO:
texto = input("Ingrese un texto, por favor: ") #Pedimos texto al usuario para analizar
texto = texto.lower() #Convierto el texto todo a minuscula.
letra1 = str(input("Ingrese la primera letra en minuscula: "))
letra2 = str(input("Ingrese la segunda letra en minuscula: "))
letra3 = str(input("Ingrese la tercera letra en minuscula: "))
print(" ")
#Primera parte: Contar las letras ingresadas que pertenecen
#al texto
print("Cantidad de letras:")
print(f"La letra '{letra1}' aparece {texto.count(letra1)} veces.")
print(f"La letra '{letra2}' aparece {texto.count(letra2)} veces.")
print(f"La letra '{letra3}' aparece {texto.count(letra3)} veces.")
print(" ")
#Segunda parte: Contar las palabras
print("Cantidad de palabras del texto:")
palabras = texto.split() #La funcion split sirve para separar el texto por cada espacio y guardarlo como lista.
longitud_texto = len(palabras) #Con longitud del texto ya transformado a lista, le pido la longitud de la lista para obtener la cantidad de palabras.
print(f"Su texto contiene {longitud_texto} palabras.")
print(" ")
#Tercer parte: Primer y ultima letra del texto ingresado
print("Primer y ultima letra del texto:")
primer_letra = texto[0] #Utilizando los indices del string busco el primer caracter y el ultimo del texto.
ultima_letra = texto[-1]
print(f"La primer letra del texto es '{primer_letra}' y la ultima letra es '{ultima_letra}'.")
print(" ")
#Cuarta parte: Invertir el texto
print("Texto invertido:")
texto_invertido = texto[::-1] #Recorro el texto al reves y lo guardo en la variable.
print(f"El texto de manera inversa queda asi: '{texto_invertido}'")
print(" ")
#Quinta parte: Indicar si "Python" se encuentra en el texto
print("Python aparece dentro del texto?:")
control = "python" in texto #Si la palabra "Python" aparece en el texto o si no aparece e indicar la respuesta.
diccionario = {True: "si", False: "no"}
print(f"La palabra 'Python' {diccionario[control]} esta en el texto.")