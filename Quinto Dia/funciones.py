#def saludar_persona ():
    #"""
    #Esta funcion sirve para saludar a las personas
    #"""
    #print("Hola")

#saludar_persona() #Llamamos a la funcion

#def saludar_persona (nombre):
    #"""
    #Esta funcion sirve para saludar a las personas
    #"""
    #Ahora le damos un parametro a la funcion
    #en este caso el paramtro es nombre
    #print("Hola " + nombre)

#saludar_persona("Carlos")

#Practica Funciones 1:
#Declara una función llamada saludar, que cada vez que sea llamada imprima en pantalla "¡Hola mundo!"
def saludar():
    """
    Funcion que saluda a Mundo
    """
    print("¡Hola mundo!")
saludar()

#Practica Funciones 2:
#Declara una función llamada bienvenida, que tome como argumento el nombre de una persona, y que cada vez que sea llamada imprima en pantalla "¡Bienvenido {nombre_persona}!"
#Crea la variable nombre_persona, y almacena dentro de la misma el nombre que prefieras.
def bienvenida(nombre_persona):
    """
    Funcion que saluda a una persona
    """
    print(f"¡Bienvenido {nombre_persona}!")

nombre_persona = "Federico"
bienvenida(nombre_persona)

#Practica Funciones 3:
#Declara una función llamada cuadrado, que tome como argumento un número cualquiera, y que cada vez que sea llamada, imprima en pantalla el cuadrado de dicho número (es decir, la potencia 2 del valor).
#El nombre del argumento que debe tomar dicha función es un_numero. Crea dicha variable y asígnale un número cualquiera.
def cuadrado(un_numero):
    """
    Funcion que imprime el cuadrado de un numero
    """
    print(un_numero**2)
un_numero = 2
cuadrado(un_numero)




