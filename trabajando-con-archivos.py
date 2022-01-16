
## Leer el archivo rana.txt y pintarlo en consola con el siguiente mensaje "lectura del archivo es : <contenido>"


conexion = open("/Users/bryan-alexander/bcd/education/software-development/proof-of-concept/python-test/rana.txt")
contenido = conexion.read()

print("el archivo es :", contenido)
conexion.close()