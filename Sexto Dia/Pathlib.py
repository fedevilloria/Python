from pathlib import Path, PureWindowsPath
carpeta = Path("D:/PythonCurse/Sexto Dia/prueba1.txt")
ruta_windows = PureWindowsPath(carpeta) #Cambia la ruta al formato Windows
#print(ruta_windows)
#print(carpeta.read_text()) #Devuelve el contenido del archivo
#print(carpeta.name) #Nombre completo y tipo de archivo
#print(carpeta.suffix) #Devuelve tipo de archivo
#print(carpeta.stem) #Devuelve unicamente el nombre

#if not carpeta.exists():
#    print("Este archivo no existe")
#else:
#    print("Genial, existe")