#! /usr/bin/env python3

''' 2. De una serie de números ingresados por el usuario, imprima cuales de estos son primos y cuáles no.
El ingreso de los números se termina cuando el usuario ingrese un numero negativo. '''

""" bandera = True
primo = True

while bandera:
    num = int(input('Ingrese un número: '))
    for x in range(1,num+1):
        if num % x == 0:
            if x == 1 or x == num:
                primo = True
            else:
                print('No es primo')
                primo = False """


num = 0

while num >= 0:
    num = int(input('Ingrese un número: '))
    contador = 0
    if num < 0:
        break

    for i in range(1,num+1):
        if num % i == 0:
            contador +=1
    
    if contador == 2:
        print(f"El numero {num} es primo")

    else:
        print(f"El numero {num} no es primo")