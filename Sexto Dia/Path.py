from pathlib import Path

#base = Path.home()
#guia = Path(base, "Europa", "Spain", Path("Barcelona", "Sagrada_Familia.txt"))
#guia2 = guia.with_name("La_Pedrera.txt")
#print(base)
#print(guia.parent) #Devuelve el ultimo archivo contenedor. En este caso devolveria hasta "Barcelona".
#print(guia2)

#guia = Path(Path.home(), "Europa")
#for txt in Path(guia).glob("*.txt"): #Para cada txt en Europa, devuelva todos los .txt
#    print(txt)

#for txt in Path(guia).glob("**/*.txt"): #Para cada txt en toda la carpeta Europa y en las subcarpetas, devuelva todos los .txt
#    print(txt)

#guia = Path("Europa", "Espana", "Barcelona", "Sagrada_Familia.txt")
#en_europa = guia.relative_to(Path("Europa"))
#en_espania = guia.relative_to(Path("Europa", "Espana"))

#Practica 1:
#Almacena en la variable ruta_base, un objeto Path que señale el directorio base del usuario.
#ruta_base = Path.home()

#Practica 2:
#Implementa y crea una ruta RELATIVA que nos permita llegar al archivo "practicas_path.py" a partir de la siguiente estructura de carpetas:
#ruta = Path("Curso Python", "Día 6", "practicas_path.py")

#Practica 3:
#Implementa y crea una ruta ABSOLUTA que nos permita llegar al archivo "practicas_path.py" a partir de la siguiente estructura de carpetas:
ruta = Path(Path.home(), "Curso Python", "Día 6", "practicas_path.py")