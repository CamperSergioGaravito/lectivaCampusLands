#! /usr/bin/env python3

'''2. Construya un programa tal que lea un número entero N, muestre la cantidad de términos y el resultado
de la siguiente serie: 1 - 1/2 + 1/3 - 1/4 + ... +- 1/N'''

#### Variables e ingreso de data #####
listFactorial = []
N = int(input('Ingrese un numero entero: '))
resultFactorial = 1
sumarRestar = False

for factorial in range(2,N+1):
    listFactorial.append(factorial)
    if sumarRestar == True:
        resultFactorial += (1 / factorial)
        sumarRestar = False
        print(resultFactorial,' - ')
    else:
        resultFactorial -= (1 / factorial)
        sumarRestar = True
        print(resultFactorial,' + ')

print('-' * 48)
print('{} ===> Resultado total'.format(resultFactorial),'\n')

print('-' * 48)
print('Resultado de 1 - ',end='')
interruptor = True

for posicion in range(0,len(listFactorial)):
    if posicion == len(listFactorial)-1:
        print('1/{} = {:.2f}'.format(N,resultFactorial))
        break
    if interruptor:
        print('1/{} + '.format(listFactorial[posicion]),end='')
        interruptor = False
    else:
        print('1/{} - '.format(listFactorial[posicion]),end='')
        interruptor = True

print('-' * 48)