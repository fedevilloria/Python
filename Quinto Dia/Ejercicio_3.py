def repetido(*args):
    contador = 0
    for numero in args:
        if contador + 1 == len(args): #Si no encuentra nada, se soluciona para que no se vaya de rango
            return False
        elif args[contador] == 0 and args[contador + 1] == 0: #en los argumentos en la posicion del contador (valor)
            return True
        else:
            contador = contador + 1
    return False

print(repetido(0,1,1,0,0,2))