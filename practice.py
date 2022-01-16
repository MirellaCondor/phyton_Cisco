# coding=utf-8

# 1. Generar un excepcion forsoza y luego controlarlo para decir al usuario ("no pasho na!, tranquilo lo controlé")

try:
    print("dividiré 0 ÷ 0")
    print(0/0)
except:
    print("no pasho na!, tranquilo lo controlé")


# 2. Crear un excepcion personalizar que lleve el nombre ViejitaPanzocitaException y
# luego dispararla para controlarla con un mensaje que diga "tudu ben"
class miEViejitaPanzocitaException(Exception):
    pass

try:
    raise miEViejitaPanzocitaException
except miEViejitaPanzocitaException:
    print("Tudu bem")
