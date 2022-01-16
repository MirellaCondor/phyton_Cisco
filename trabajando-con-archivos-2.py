
## Leer el archivo rana.txt y pintarlo en consola con el siguiente mensaje "lectura del archivo es : <contenido>" 
## y si no lo encuentra pintar, "No hay pe causa!!"


try:
    conexion = open("/Users/bryan-alexander/bcd/education/software-development/proof-of-concept/python-test/recursos/rana2.txt")

    contenido = conexion.read()
    print("el archivo es :", contenido)
    conexion.close()
except:
    print("No hay pe causa!!")





