#! /usr/bin/env python3

'''3. Construya un programa tal que encuentre y muestre todos los enteros positivos, comenzando desde el
cero, que satisfacen la siguiente expresión: P³ + Q⁴ - 2 * P² < 680'''

### Variables ###
p = int(input('Ingrese un número entero: '))
listaIntPos = []

### Validación y guardado de resultados que cumplen la expresión ###
for q in range(0,p+1):
    ### Expresión ###
    resultExpresion = ((p**3) + (q**4) - (2 * (p**2)))
    print(resultExpresion)
    ### Validación ###
    if 0 < resultExpresion < 680:
        listaIntPos.append(resultExpresion)

print('-' * 30)
print('Números enteros positivos que cumplen con la\n\
expresión: P³ + Q⁴ - 2 * P² < 680 cuando P es {}'.format(p))
print('-' * 30)

### Impresión de resultados ###
for posicion in range(0,len(listaIntPos)):
    if (posicion % 2 == 0 and posicion != 0):
        print('{}'.format(listaIntPos[posicion]),end='\n')
    else:
        print('{}\t'.format(listaIntPos[posicion]),end='')
print('-' * 30)