#! /usr/bin/env python3

######### Variables #######

a = float(input('Ingrese un número: '))
b = float(input('Ingrese un número: '))
c = float(input('Ingrese un número: '))

##### p para comprobar si es triángulo ######

p = (a+b+c)/2

######### Validación ########

if p > a and p > b and p > c:
    print('es un triángulo')
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    ####### Resultado ########
    print('El triangulo con sus lados a: {}, b: {}, c: {}, tiene un área de: {:.2f}'.format(a,b,c,area))
else:
    print('no es un triángulo')