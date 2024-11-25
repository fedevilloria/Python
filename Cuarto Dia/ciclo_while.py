#monedas = 5
#while monedas > 0:
#    print(f"Tengo {monedas} monedas")
#    #La resta se puede hacer de dos maneras:
#    monedas = monedas - 1 #1
#    monedas -= 1 #2
#else:
#    print("No tengo mas dinero")

#respuesta = "s"
#while respuesta == "s":
#    respuesta = input("Quieres seguir? (s/n)")
#else:
#    print("Gracias")

#respuesta = "s"
#while respuesta == "s"
#    pass #Sirve como ticket para guardar algo que nos sirva en un futuro rellenar
#print("Hola")

#nombre = input("Decime tu nombre: ")
#for letra in nombre:
#    if letra == "r":
#        break #Break sirve para que cuando encuentre un valor se corte el ciclo
#    print(letra)

#nombre = input("Decime tu nombre: ")
#for letra in nombre:
#    if letra == "r":
#        continue #Omite la letra o caracter especificado.
#    print(letra)

#Practica While 1:
#Crea un Loop While que se imprima en pantalla los números del 10 al 0, uno a la vez
numero = 10
while numero > 0:
    print(numero)
    numero = numero - 1
else:
    print(numero)

#Practica While 2:
#Crea un Loop While que reste de uno en uno los números desde el 50 al 0 (ambos números incluídos) con las siguientes condiciones adicionales:
#- Si el número es divisible por 5, mostrar dicho número en pantalla (¡recuerda que aquí puedes utilizar la operación módulo dividiendo por 5 y verificando el resto!)
#- Si el número no es divisible por 5, continuar ejecutando el loop sin mostrar el valor en pantalla (no te olvides de seguir restando para que el programa no corra infinitamente).
numero = 50
while numero >= 0:
    if numero % 5 == 0:
        print(numero)
    numero = numero - 1
    continue

#Practica While 3:
#Crea un loop For a lo largo de la siguiente lista de números, imprimiendo en pantalla cada uno de sus elementos, e interrumpe el flujo en el momento que encuentres un valor negativo:
#lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]
lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]
for numero in lista_numeros:
    if numero > 0:
        print(numero)
    else:
        break