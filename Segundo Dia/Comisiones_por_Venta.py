nombre_empleado = input("Ingrese su nombre: ")
cantidad_de_ventas = input("Ingrese la cantidad de ventas que obtuvo este mes: ")
cantidad_de_ventas = int(cantidad_de_ventas)
comision_por_ventas = round(cantidad_de_ventas*13/100,2)
print(f"Hola {nombre_empleado}, este mes has vendido {cantidad_de_ventas} productos y de comision te corresponde ${comision_por_ventas} por las ventas.\nMuchas gracias!")