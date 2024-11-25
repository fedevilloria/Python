def abrir_leer(archivo):
    archivo = open(archivo)
    return archivo.read()

def sobrescribir(archivo):
    archivo = open(archivo,"w")
    archivo.write("contenido eliminado")
    return

def registro_error(archivo):
    archivo = open(archivo, "a")
    archivo.write("se ha registrado un error de ejecución")
    archivo.close()
    return
