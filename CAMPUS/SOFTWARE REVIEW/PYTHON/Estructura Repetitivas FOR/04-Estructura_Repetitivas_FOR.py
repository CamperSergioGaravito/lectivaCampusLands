#! /usr/bin/env python3

'''4. Construya un programa que lea 10 números ingresados por el usuario y que al final, muestre el mayor
y el menor de todos estos números.'''

### Variables ###

mayor = 0
menor = True

### Validación ###
for x in range(0,10):
    num1 = int(input('Ingrese un número: '))
    if num1 > mayor:
        mayor = num1
    else:
        if num1 < menor or menor == True:
            menor = num1

print('el número mayor es: {} y el menor es: {}'.format(mayor,menor))

