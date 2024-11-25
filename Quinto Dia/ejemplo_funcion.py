#Ejemplo de la vida cotidiana
precios_cafe = [("capucino", 2.2),("Expresso",1.2),("Moka",1.9)]

def cafe_mas_caro(lista_precios):
    precio_mayor = 0
    cafe_mas_caro = " "
    for cafe,precio in precios_cafe:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
        else:
            pass
    return (cafe_mas_caro,precio_mayor)

#print(cafe_mas_caro(precios_cafe))
#Si no se puede hacer guardando los valores en variables
#Ejemplo
cafe, precio = cafe_mas_caro(precios_cafe)
print(f"El cafe mas caro es {cafe} y su precio al publico es ${precio}.")