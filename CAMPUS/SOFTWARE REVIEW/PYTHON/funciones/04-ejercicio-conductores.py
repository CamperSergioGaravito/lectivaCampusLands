#! /usr/bin/env python3

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
        print('==> Solo hay 2 opciones')
        print('x' * 50)

##### FUNCIONES #####
def calcular(clase,ventasMesPas,ventasMesEnc):
    global totalPagarConds
    global cantExp
    global cantNov
    if clase == 1:
        bonoPas = 0.3
        bonoEnc = 0.2
        comisionPas = ventasMesPas * bonoPas
        comisionEnc = ventasMesEnc * bonoEnc
        totalPagar = comisionEnc + comisionPas
        cantExp += 1

    elif clase == 2:
        bonoPas = 0.2
        bonoEnc = 0.15
        comisionPas = ventasMesPas * bonoPas
        comisionEnc = ventasMesEnc * bonoEnc
        totalPagar = comisionEnc + comisionPas
        cantNov += 1

    totalPagarConds += totalPagar
    return bonoPas,bonoEnc,comisionPas,comisionEnc,totalPagar

##### INICIO #####
cantNov = 0
cantExp = 0
totalPagarConds = 0

while True:
    try:
        print('-' * 80)
        print('TRASRAPIDO'.center(80,' '))
        print('-' * 80)

        print('-' * 80)
        print('DATOS CONDUCTOR'.center(80,' '),end='\n')
        cedula = int(input('\nCédula: '))
        nombre = input('Nombre: ')

        print('Clase conductor:\n\t1: Experto\n\t2: Novato')
        clase = int(input('? Selección: '))
        if 0 > clase > 2:
            error(2)
            continue

        ventasMesPas = int(input('Valor total pasajes del mes: '))
        ventasMesEnc = int(input('Valor total encomiendas del mes: '))

        bonoPas,bonoEnc,comisionPas,comisionEnc,totalPagar = calcular(clase,ventasMesPas,ventasMesEnc)
        print('-' * 80)
        print('PAGO CONDUCTOR'.center(80,' '),end='\n')
        print('-' * 80)
        print(f'Cédula: {cedula}  \t  Conductor: {nombre.upper()}\n'.center(80,' '))
        print(f'\nVentas pasajes mes:\t\t${ventasMesPas:,.0f}')
        print(f'Ventas encomiendas mes:\t\t${ventasMesEnc:,.0f}')
        print(f'Bono por venta pasajes:\t\t{bonoPas*100:.0f}%')
        print(f'Bono por venta encomiendas:\t{bonoEnc*100:.0f}%')
        print(f'Comisión por venta pasajes:\t${comisionPas:,.0f}')
        print(f'Comisión por venta pasajes:\t${comisionEnc:,.0f}')
        print('-' * 80)
        print(f'Total a pagar:\t\t\t${totalPagar:,.0f}')
        print('-' * 80,end='\n')

        print('\n','+' * 80)
        print(f'Cantidad novatos: {cantNov}\nCantidad expertos: {cantExp}')
        print(f'Total nómina: ${totalPagarConds:,.0f}')
        print('+' * 80,end='\n\n')

    except ValueError:
        error(1)
    except Exception as e:
        error(0,e)