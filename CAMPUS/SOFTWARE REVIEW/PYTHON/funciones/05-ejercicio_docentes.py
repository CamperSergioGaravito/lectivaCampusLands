#! /usr/bin/env python3

''' Situación problema: Liquidación de Honorarios Docente

Se tiene la siguiente información de los N docentes de una institución educativa:
• Documento de identidad
• Nombre
• Categoría docente (A, B o C)
• Horas laboradas en el mes 

También suministran el valor de la hora que la institución paga a los docentes, dependiendo
de su categoría, así:(Categoría - Valor hora):(A-$25.000,B-$35.000,C-$50.000)
Con base en la información suministrada se pide:
• Valor a pagar por honorarios para cada docente
• Valor total apagar(Todos los docentes)
• Cantidad de docentes de cada una de las categorías.'''

# Dictionary #
''' fees: honorarios
    pay: pagar '''

#### ERRORES ####
def error(cod,e=None):
    if cod == 0 and e:
        print('x' * 50)
        print(f':( Error inesperado. Error: {e}.')
        print('x' * 50)

    elif cod == 1:
        print('x' * 50)
        print(f'==> Error en tipo de valores de ingreso.')
        print('x' * 50)

    elif cod == 2:
        print('x' * 50)
        print('==> Solo hay 3 opciones')
        print('x' * 50)

###### FUNCIONES ######
### Calcular pago ###
def calcular(category,workHours):
    global contA
    global contB
    global contC

    A = 25000
    B = 35000
    C = 50000

    if category.lower() == 'a':
        pay = workHours * A
        cat = A
        contA += 1
    elif category.lower() == 'b':
        pay = workHours * B
        cat = B
        contB += 1
    elif category.lower() == 'c':
        pay = workHours * C
        cat = C
        contC += 1

    return cat,pay

###### START ######
### Variables ###
valuePayFees = 0
valuePayTeachs = 0
contA = 0
contB = 0
contC = 0


while True:
    try:
        document = int(input('Documento de identidad: '))
        name = input('Nombre: ')
        category = input('Categoría docente (A, B o C): ')

        if category.lower() != 'a' and category.lower() != 'b' and category.lower() != 'c':
            error(2)
            continue

        workHours = int(input('Horas laboradas en el mes: '))
        cat,valuePayFees = calcular(category,workHours)

        valuePayTeachs += valuePayFees

        print('\n','-' * 80)
        print(f'Recibo de pago'.center(80,' '))
        print('-' * 80)
        print(f'Valor nómina: ${valuePayTeachs:,.0f}'.center(80,' '),end='\n')
        print(f'\nValor honorarios {name}: ${valuePayFees:,.0f}')
        print('-' * 80)
        print(f'Cant. docentes categoria A: {contA}')
        print(f'Cant. docentes categoria B: {contB}')
        print(f'Cant. docentes categoria C: {contC}')
        print('-' * 80,end='\n\n')

    except ValueError:
        error(1)
    except Exception as e:
        error(0,e)