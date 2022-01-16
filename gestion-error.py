# coding=utf-8

contador = 0

while contador <= 1000:
    print('ciclo ' + str(contador))

    try:
        if contador == 500:
            resultado = 1+1
    except NameError:
        print('Error Controlado!')
    except ZeroDivisionError as errorsito:
        print(errorsito)
        print('Error Controlado!')

    contador += 1
