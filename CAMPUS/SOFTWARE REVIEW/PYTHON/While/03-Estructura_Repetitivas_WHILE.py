#! /usr/bin/env python3

''' 3. De una serie de números ingresados por el usuario, indique cual es el menor y el mayor de estos.
El ingreso de los números se termina cuando el usuario ingrese un numero negativo.'''

bandera = True
menorN = True
mayorN = 0

while bandera:
    print('-' * 30)
    num = float(input('Ingrese un número: '))
    if num < 0:
        print('-' * 30)
        print('El número ingresado debe ser positivo.')
        break
    if num > mayorN:
        mayorN = num
    if menorN == True or num < menorN:
        menorN = num
    
    print('El número mayor hasta ahora es: {:.2f}\nEl número menor hasta ahora es: {:.2f}'.format(
        mayorN,menorN
    ))

print('El número mayor es: {:.2f}\nEl número menor es: {:.2f}'.format(mayorN,menorN))
print('-' * 30)