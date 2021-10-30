# coding=utf-8

print("::: CALCULAR EL NÚMERO MAYOR :::\n")

number1 = int(input("Ingrese el primer número: "))
number2 = int(input("Ingrese el segundo número: "))

def calcular_numero_mayor(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2

elMayor = calcular_numero_mayor(number1, number2)

print("El número mayor es .....")
print("re dobles re dobles tan tan tan !!!")
print("esssss " + str(elMayor))
