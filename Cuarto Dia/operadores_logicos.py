#Y - AND
#Si ambas se cumplen devuelve TRUE.
#Si al menos una no se cumple devuelve FALSE.
#operacion = 4 < 5 and 5 < 6
#print(operacion)

#operacion2 = 4 < 5 and 5 == 3 + 2 #Tambien lo podemos hacer con operaciones
#print(operacion2)

#operacion3 = (55 == 55) and ("perro" == "perro")
#print(operacion3)

#frase = "Esta frase es breve"
#mi_bool_and = ("frase" in frase) and ("python" in frase)
#print(mi_bool_and)

#O - OR
#Unicamente va ser FALSE cuando en ambos casos no se cumpla alguna operacion logica
#booleano = (1 == 10) or (30 == 30)
#print(booleano)

#booleano_falso = (1 == 10) or (3 == 30) #Sera falso ya que no se cumple ninguno de los dos casos
#print(booleano_falso)

#frase = "Esta frase es breve"
#mi_bool = ("frase" in frase) or ("python" in frase)
#print(mi_bool)

#NO - NOT
#Es la negacion a la frase
#mi_bool_not = not ("a" == "a") #Al ser iguales el NOT devuelve el valor contrario. En este caso sera FALSE.
#print(mi_bool_not)

#mi_bool_not2 = not ("a" != "a") #Al ser distintos, el NOT devuelve el valor contrario. En este caso sera TRUE.
#print(mi_bool_not2)

#Practica Operadores Logicos 1:
#Crea tres variables (num1 ,  num2 y num3):
#Dentro de num1, almacena el valor 36
#Dentro de num2, almacena el resultado de la operación 72/2
#Dentro de num3, almacena el valor 48
#Verifica si num1 es mayor que num2, y menor que num3. Almacena el resultado de dicha comparación en una variable llamada mi_bool.
num1 = 36
num2 = 72 / 2
num3 = 48
mi_bool = (num1 > num2) and (num1 < num3)
print(mi_bool)

#Practica Operadores Logicos 2:
#Verifica si num1 es mayor que num2, o menor que num3. Almacena el resultado de dicha comparación en una variable llamada mi_bool.
num1 = 36
num2 = 72 / 2
num3 = 48
mi_bool = (num1 > num2) or (num1 < num3)
print(mi_bool)

#Practica Operadores Logicos 3:
#Verifica si las palabras almacenadas en las siguientes variables:
#palabra1 = "éxito", y
#palabra2 = "tecnología"
#no se encuentran en la frase a continuación, y almacena el resultado de esta comprobación (un booleano) en una variable llamada mi_bool:
#"Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
#Elon Musk
frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
palabra1 = "éxito"
palabra2 = "tecnología"
mi_bool = not (palabra1 == frase) and not (palabra2 == frase)
print(mi_bool)