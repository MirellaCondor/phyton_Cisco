class Persona:
    def __init__(self, nombre, edad):
        self.cantidadOjos = 2
        self.nombre = nombre
        self.edad = edad
        print('Me crearon')

    def cambiarNombre(self, nuevoNombre):
        self.nombre = nuevoNombre


mirella = Persona('Mirella', 14)
bryan = Persona('Bryan', 26)

print(mirella.cantidadOjos)
print(mirella.edad)
mirella.cambiarNombre('Elizabeth')
print(bryan.nombre)
print(mirella.nombre)
print(mirella.nombre)

