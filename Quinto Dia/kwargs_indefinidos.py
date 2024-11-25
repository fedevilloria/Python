# def suma(**kwargs):
#    for clave,valor in kwargs.items():
#        print(f"{clave} = {valor}")
# suma(x=3,y=5,z=2)

# def suma(**kwargs):
#    total = 0
#    for clave,valor in kwargs.items():
#        print(f"{clave} = {valor}")
#        total = total + valor
#    return total

# print(suma(x=3,y=5,z=2))

# def prueba(num1, num2, *args, **kwargs):
#    print(f"El primer valor es {num1}")
#    print(f"El segundo valor es {num2}")
#    for arg in args:
#        print(f"arg = {arg}")
#    for clave,valor in kwargs.items():
#        print(f"{clave} = {valor}")
# args = [100,200,300,400]
# kwargs = {"x":"uno","y":"dos","z":"tres"}
# prueba(15,50,251,5125,523,52,123,x="uno",y="dos",z="tres")
# prueba(1,5,*args,**kwargs) #Asi se desglosa una lista o un diccionario con este metodo

# Pratica KWARGS 1:
# Crea una función llamada cantidad_atributos que cuente la cantidad de parémetros que se entregan, y devuelva esa cantidad como resultado.
def cantidad_atributos(**kwargs):
    parametros = 0
    for clave in kwargs.items():
        parametros = parametros + 1
    return parametros
print(cantidad_atributos(x=5,y=76,z=2456))

#Practica KWARGS 2:
#Crea una función llamada lista_atributos que devuelva en forma de lista los valores de los atributos entregados en forma de palabras clave (keywords). La función debe preveer recibir cualquier cantidad de argumentos de este tipo.
def lista_atributos(**kwargs):
    lista = []
    for valores in kwargs.values():
        lista.append(valores)
    return lista
print(lista_atributos(x="flaco",y="inteligente",z="subnormal"))

#Practica KWARGS 3:
#Crea una función llamada describir_persona, que tome como parámetros su nombre y luego una cantidad indetermida de argumentos. Esta función deberá mostrar en pantalla:
#Características de {nombre}:
#{nombre_argumento}: {valor_argumento}
#{nombre_argumento}: {valor_argumento}
#etc...

def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for clave,valor in kwargs.items():
        print(f"{clave}: {valor}")
    return

print(describir_persona("Federico",color_pelo="marron",edad="22"))