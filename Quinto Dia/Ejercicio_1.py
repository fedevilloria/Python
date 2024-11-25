def devolver_distintos(num1,num2,num3):
    lista = [num1,num2,num3]
    suma = num1 + num2 + num3
    if suma > 15:
        maximo = max(lista)
        return maximo
    elif suma < 10:
        minimo = min(lista)
        return minimo
    elif suma > 10 and suma < 15:
        lista.sort()
        return lista[1]

print(devolver_distintos(4,5,0))