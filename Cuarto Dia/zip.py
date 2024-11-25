#nombres = ["Ana", "Hugo", "Valeria"]
#edades = [65, 29, 42]

#combinados = list(zip(nombres,edades))
#print(combinados)

#for nombres, edades in combinados:
#    print(f"{nombres} tiene {edades} anios")

#Practica Zip 1:
#Muestra en pantalla frases como la del siguiente ejemplo:
#La capital de Alemania es Berlín
#Utiliza la función zip, loops, y las siguientes listas de países y capitales para resolverlo rápida y eficientemente.
capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

frase = list(zip(paises, capitales))
for paises, capitales in frase:
    print(f"La capital de {paises} es {capitales}")

#Practica Zip 2:
#Crea un objeto zip formado a partir de listas, de un conjunto de marcas y productos que tú prefieras, dentro de la variable mi_zip.
marcas = ["Nike", "Adidas", 'Puma']
productos = ["Zapatillas", "Remeras", "Camperas"]
mi_zip = zip(marcas, productos)

#Producto Zip 3:
#Crea el zip con las traducciones los números del 1 al 5 en español, portugués e inglés (en el mismo orden), y convierte el objeto generado en una lista almacenada en la variable numeros:
#1: uno / um / one
#2: dos / dois / two
#3: tres / três / three
#4: cuatro / quatro / four
#5: cinco / cinco / five

espaniol = ["uno", "dos", "tres", "cuatro", "cinco"]
portugues = ["um", "dois", "três", "quatro", "cinco"]
ingles = ["one", "two", "three", "four", "five"]

numeros = list(zip(espaniol, portugues, ingles))