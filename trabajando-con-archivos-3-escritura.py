
# Leer el archivo rana.txt y pintarlo en consola con el siguiente mensaje "lectura del archivo es : <contenido>"
# y si no lo encuentra pintar, "No hay pe causa!!"


try:
    puenteTransmicion = open("recursos/mire-rana.txt", 'wt')

    contenido = puenteTransmicion.write("Mirella esta gordita!!!")

    puenteTransmicion.close()
except Exception as error:
    print(error)
    print("Error no se pudo escribir")
