#! /usr/bin/env python3

''' 1. Construya un programa que verifique si un número dado es perfecto. Un número perfecto es un
número entero positivo que es igual a la suma de sus divisores propios positivos (excluyendo el
número mismo). En otras palabras, si sumas todos los divisores propios de un número perfecto, el
resultado será igual al número original.
Por ejemplo, el número 6 es considerado un número perfecto. Sus divisores propios son 1, 2 y 3. Si
sumamos estos números: 1 + 2 + 3 = 6, obtenemos el mismo número original. '''

from os import system

bandera = True

while bandera:
    system('clear')
    print('#' * 70)
    print('Los números digitados deben ser enteros para validar si son perfectos.')
    print('#' * 70)

    ### Solicitud del número ###
    num = int(input('Ingrese un número: '))

    print('-' * 30)

    listaNums = []
    result = 0

    if num > 0:
        for x in range(1,num):
            if num % x == 0:
                listaNums.append(x)
                result += x
    
    if result == num:
        print('{} es un número perfecto, sus divisores son: {}\n'.format(num,listaNums))
    else:
        print('Resultado suma: ', result)
        print('{} no es un número perfecto\n'.format(num))

    salir = input('Desea realizar otra validación? S/N: ')
    if salir.lower() == 'n':
        bandera = False