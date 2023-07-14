#! /usr/bin/env python3

''' Situación problema 2: Comisión Vendedores 

Se tiene una lista de vendedores de una empresa, sobre las ventas realizadas en el mes. La información que se conoce de cada vendedor es la siguiente:

• Cédula de ciudadanía
• Nombre
• Tipo de vendedor,que puede ser 
    1: Puerta a Puerta 
    2: Telemercadeo 
    3: Ejecutivo de ventas 

Valor ventas realizadas en el mes NOTA: La lista termina cuando la cédula de ciudadanía es -1.

También nos suministran el porcentaje de comisión que se le aplica a las ventas realizadas en el mes, para el cálculo de la comisión, de acuerdo al tipo de vendedor así:
    • Si el vendedor es puerta a puerta, el porcentaje de comisiónes del 20% sobre el valor de las ventas realizadas en el mes.
    • Si el vendedor es telemercadeo, el porcentaje de comisiónes del 15% sobre el valor de las ventasrealizadasenelmes.
    • Si el vendedor es ejecutivo de ventas, el porcentaje de comisiónes del 25% sobre el valor de las ventas realizadas en el mes.

Se pide calcular el valor a pagar por comisión  de cada vendedor, el valor total de la ventas del mes, el valor total a pagarpor comisiones '''

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

#### Comprobar y calcular ####
def comprobar(cc,tVendedor,nombre):
    ventasVendedor = int(input('Ingrese sus ventas del mes: '))

    if tVendedor == 1:
        bono = 0.2
        comision = ventasVendedor * bono
    elif tVendedor == 2:
        bono = 0.15
        comision = ventasVendedor * bono
    elif tVendedor == 3:
        bono = 0.25
        comision = ventasVendedor * bono

    print('-'*80)
    print(f'\nNombre:\t{nombre.upper()}\nCédula:\t{cc}\nVentas del mes: ${ventasVendedor:,}\nBono:\t{bono*100:.0f}%\nComisión: ${comision:,.0f}',end='\n')


### Menu ###
def menu():
    try:
        print('-' * 50)
        print(' Datos '.center(50,' '))
        cedula = int(input('\nIngrese número cedula: '))

        if cedula == -1:
            print('-'*80,end='\n')
            return 'salir'
        
        nombre = input('Ingrese su nombre: ')
        print('\n• ¿Tipo de vendedor?:\n\t1: Puerta a Puerta\n\t2: Telemercadeo\n\t3: Ejecutivo de ventas\n')
        tipoVendedor = int(input('? Selección: '))
        print('-' * 50)

        if 0 < tipoVendedor < 4:
            comprobar(cedula,tipoVendedor,nombre)
        else:
            error(2)
            return

    except ValueError:
        error(1)
    except Exception as e:
        error(0,e)

#### Variables ####
while True:
    try:
        iniciar = menu()
        if iniciar == 'salir':
            print('\nGracias por preferirnos.')
            break
        continue

    except ValueError:
        error(1)
