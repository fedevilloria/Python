def contar_primos(numero):
    lista_primos = [2] #Se le agrega el dos por la convencion
    iteracion = 3
    if numero < 2:
        return 0
    while iteracion <= numero:
        for num in range(3,iteracion,2):
            if iteracion % num == 0:
                iteracion = iteracion + 2
                break
            else:
                lista_primos.append(iteracion)
                iteracion = iteracion + 2
    print(lista_primos)
    return len(lista_primos)
print(contar_primos(5))