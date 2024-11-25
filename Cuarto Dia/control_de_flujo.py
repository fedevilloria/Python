#if 10 > 9:
    #print("es correcto")

#if 5 == 2:
    #print("es correcto")
#else:
    #print("no es correcto")

#mascota = "perro"
#if mascota == "gato":
    #print("tienes un gato")
#elif mascota == "perro":
    #print("tienes un perro")
#else:
    #print("no se que mascota tienes")

#edad = 16
#calificacion = 9
#if edad < 18:
    #print("Eres menor de edad")
    #if calificacion >= 7:
        #print("Aprobado")
    #else:
        #print("No aprobado")
#else:
    #print("Eres adulto")

#Practica Control de Flujo 1:
#Utilizando las variables num1 y num2, que se alimentan con el input del usuario (tal como en el código ya proporcionado):
#Crea una estructura de control de flujo que compare los valores de las variables, y arroje un resultado de acuerdo al caso:
#"num1 es mayor que num2"
#"num2 es mayor que num1"
#"num1 y num2 son iguales"

num1 = input("Ingresa un número:")
num2 = input("Ingresa otro número:")

if num1 > num2:
   print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"{num2} es mayor que {num1}")
else:
    print(f"{num1} y {num2} son iguales")

#Practica Control de Flujo 2:
#Las leyes de un país establecen que un adulto puede conducir si tiene licencia para hacerlo, y para optar por una licencia para conducir, debe de tener 18 años o más.
#Crea una estructura condicional para verificar si una persona de 16 años sin licencia puede conducir, y muestra el resultado que corresponda en pantalla:
#"Puedes conducir"
#"No puedes conducir aún. Debes tener 18 años y contar con una licencia"
#"No puedes conducir. Necesitas contar con una licencia"

edad = 16
tiene_licencia = False
if edad >= 18:
    print("Puedes conducir")
elif edad >= 18 or tiene_licencia:
    print("No puedes conducir. Necesitas contar con una licencia")
else:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")

#Practica Control de Flujo 3:
#Para acceder a un determinado puesto de trabajo, el candidato debe ser capaz de programar en Python y tener conocimientos de inglés.
#Crea una estructura condicional para evaluar a un candidato dadas estas condiciones, y muestra el mensaje correspondiente en pantalla:
#"Cumples con los requisitos para postularte"
#"Para postularte, necesitas saber programar en Python y tener conocimientos de inglés"
#"Para postularte, necesitas tener conocimientos de inglés"
#"Para postularte, necesitas saber programar en Python"
#Utiliza la base de código ya proporcionada para plantear la estructura de control de flujo apropiada y verificar dichas condiciones. Evalúa a un candidato que sabe inglés, pero no programa en Python.

habla_ingles = True
sabe_python = False

if habla_ingles and sabe_python:
    print("Cumples con los requisitos para postularte")
elif not habla_ingles:
    print("Para postularte, necesitas tener conocimientos de inglés")
elif not sabe_python:
    print("Para postularte, necesitas saber programar en Python")
else:
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")