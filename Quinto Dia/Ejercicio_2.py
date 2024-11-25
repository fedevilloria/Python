def deletrear_sin_repetir(palabra):
    lista = []
    for letra in palabra:
        lista = list(set(palabra))
        lista.sort()
    return lista

print(deletrear_sin_repetir("entretenido"))