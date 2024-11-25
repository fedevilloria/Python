#def suma(*args): #*args sirve para recibir una cantidad indefinida de argumentos
#    total = 0
#    for arg in args:
#        total = total + arg
#    return total
#print(suma(5,6,5,6,23))

#Practica Argumentos Indefinidos 1:
#Crea una función llamada suma_cuadrados que tome una cantidad indeterminada de argumentos numéricos, y que retorne la suma de sus valores al cuadrado.
#Por ejemplo para los argumentos suma_cuadrados(1,2,3) deberá retornar 14 (1+4+9).

def suma_cuadrados(*args):
    total = 0
    for n in args:
        total = total + n**2
    return total
print(suma_cuadrados(1,2,3))

#Practica Argumentos Indefinidos 2:
#Crea una función llamada suma_absolutos, que tome un conjunto de argumentos de cualquier extensión, y retorne la suma de sus valores absolutos (es decir, que tome los valores sin signo y los sume, o lo que es lo mismo, los considere a todos -negativos y positivos- como positivos).
def suma_absolutos(*args):
    total = 0
    for n in args:
        total = total + abs(n)
    return total
print(suma_absolutos(-2,-5,4))

#Practica Argumentos Indefinidos 3:
#Crea una función llamada numeros_persona que reciba, como primer argumento, un nombre, y a continuación, una cantidad indefinida de números.
#La función debe devolver el siguiente mensaje:
#"{nombre}, la suma de tus números es {suma_numeros}"

def numeros_persona(nombre,*numeros):
    suma_numeros = 0
    for num in numeros:
        suma_numeros = suma_numeros + num
    return f"{nombre}, la suma de tus números es {suma_numeros}"
print(numeros_persona("Federico",1,2,4,54,4))