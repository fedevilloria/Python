#x = 10
#y = 5
#print("Mis numeros son {} y {}".format(x,y))
#print("La suma de {} y {} da como resultado {}".format(y,x,y+x))

#color = "Rojo"
#patente = 42456
#print(f"El auto es {color} y la patente es {patente}")

#Practica de FORMATEAR CADENAS 1:
#Necesitamos imprimir el nombre y número de asociado dentro de la siguiente frase:
#Estimado/a (nombre_asociado), su número de asociado es: (numero_asociado)
#Recuerda que la precisión de tu respuesta (espacios, ortografía y puntuación), es muy importante para llegar al resultado correcto.
nombre_asociado = "Jesse Pinkman"
numero_asociado = 399058
print(f"Estimado/a {nombre_asociado}, su número de asociado es: {numero_asociado}")

#Practica de FORMATEAR CADENAS 2:
#Muestra al usuario la cantidad de puntos acumulados dentro de la siguiente frase:
#Has ganado (puntos_nuevos) puntos! En total, acumulas (puntos_totales) puntos
#Recuerda que la precisión de tu respuesta (espacios, ortografía y puntuación), es muy importante para llegar al resultado correcto.
puntos_nuevos = 350
puntos_totales = 1225
print(f"Has ganado {puntos_nuevos} puntos! En total, acumumlas {puntos_totales} puntos")
print("Has ganado {} puntos! En total, acumulas {} puntos".format(puntos_nuevos,puntos_totales))

#Practica de FORMATEAR CADENAS 3:
#Muestra al usuario la cantidad de puntos acumulados dentro de la siguiente frase:
#Has ganado (puntos_nuevos) puntos! En total, acumulas (puntos_totales) puntos
#En esta ocasión, la cantidad de puntos acumulados (totales) será igual a los puntos_anteriores más los puntos_nuevos.
#Recuerda que la precisión de tu respuesta (espacios, ortografía y puntuación), es muy importante para llegar al resultado correcto.
puntos_anteriores = 875
puntos_nuevos = 350
print("Has ganado {} puntos! En total, acumulas {} puntos".format(puntos_nuevos,puntos_nuevos+puntos_anteriores))
print(f"Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_anteriores+puntos_nuevos} puntos")