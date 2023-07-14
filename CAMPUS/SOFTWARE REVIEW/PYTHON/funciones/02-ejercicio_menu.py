#! /usr/bin/env python

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
        

########### FUNCIONES ###########
### Menu ###
def menu(men):
    if men == 1:
        print('-' * 50)
        print(' Programa académico al que pertenece '.center(50,' '))
        print('\n1: Técnico en Sistemas\n2: Técnico en Desarrollo de video juegos\n3: Técnico en Animación Digital')
        print('-' * 50)

    if men == 2:
        print('-' * 80)
        print(' Beca obtenida '.center(80,' '))
        print('\n1: Beca por rendimiento académico. Descuento del 50% sobre el valor matricula.\n2: Beca Cultural–Deportes. Descuento del 40% sobre el valor matrícula.\n3: Sin Beca.')
        print('-' * 80)

    sel = int(input('? Selección (1 - 3): '))
    return sel,men

### Calcular porcentaje ###
def calcularPorce(porcentaje):
    if programAcad.lower().find('sistemas') != -1:
        vlrMtc = 800_000
        res = vlrMtc - (vlrMtc * porcentaje)
        return res,vlrMtc
    
    elif programAcad.lower().find('juegos') != -1:
        vlrMtc = 1_000_000
        res = vlrMtc - (vlrMtc * porcentaje)
        return res,vlrMtc
    
    elif programAcad.lower().find('animación') != -1:
        vlrMtc = 1_200_000
        res = vlrMtc - (vlrMtc * porcentaje)
        return res,vlrMtc

########## Logica inicial #########
pasa = True
while True:
    try:
        if pasa:
            print('-' * 50)
            codigo = int(input('Cod. estudiante: '))
            nombre = input('Nombre de estudiante: ')
            print('-' * 50)
            seccion = True

        if seccion:
            try:
                select,mnu = menu(1)
                if 0 < select < 4 and mnu == 1:
                    if select == 1:
                        programAcad = 'Técnico en Sistemas'
                    if select == 2:
                        programAcad = 'Técnico en Desarrollo de video juegos'
                    if select == 3:
                        programAcad = 'Técnico en Animación Digital'
                    
                    pasa = True
                    print(programAcad)
                    seccion = False

                else:
                    error(2)
                    pasa = False
                    continue

            except ValueError:
                error(1)
                pasa = False
                continue
        
        if not seccion:
            try:
                select,mnu = menu(2)

                if 0 < select < 4 and mnu == 2:
                    if select == 1:
                        descuento = 0.5
                        valorMatri,vlrMtc = calcularPorce(descuento)

                    if select == 2:
                        descuento = 0.4
                        valorMatri,vlrMtc = calcularPorce(descuento)

                    if select == 3:
                        descuento = 0
                        valorMatri,vlrMtc = calcularPorce(descuento)

                    pasa = True

                else:
                    error(2)
                    pasa = False
                    seccion = False
                    continue

            except ValueError:
                error(1)
                pasa = False
                seccion = False
                continue

        pasa = False
        if valorMatri:
            pasa = True
            print('\n','#' * 50)
            print('# Valor neto #'.center(50,' '))
            print('-' * 50)

            print(f"Código {'-'*15}> {codigo}")
            print(f"Nombre {'-'*15}> {nombre.upper()}")
            print(f"Carrera {'-'*15}> {programAcad}")

            print('-'*50,end='\n')

            print(f"Valor Matricula {'-'*15}> ${vlrMtc:,.0f}")
            print(f"Descuento {'-'*20}> {descuento*100:.0f}%")

            print(f'{"-"*50}'.center(50,' '))
            
            print(f"Valor neto {'-'*15}> ${valorMatri:,.0f}")
            
            print('#' * 50,end='\n')
            input('\nPresione una tecla para regresar al menú.')
            print('-'*50,end='\n')
            continue

    except ValueError:
        error(1)

    except Exception as a:
        error(0,a)

