#! /usr/bin/env python3

#### Errores ####
def error(cod,e=None):
    if cod == 0 and e:
        print('x' * 80)
        print(f':( Error inesperado. Error: {e}.')
        print('x' * 80)

    elif cod == 1:
        print('x' * 80)
        print(f'==> Error en tipo de valores de ingreso.')
        print('x' * 80)

    elif cod == 2:
        print('x' * 80)
        print(f'==> Las notas van desde 0 hasta {e}.')
        print('x' * 80)
    
    elif cod == 3:
        print('x' * 80)
        print('==> Solo estan permitidas mínimo 1 hora, máximo 160 horas.')
        print('x' * 80)

    elif cod == 4:
        print('x' * 80)
        print('==> Solo está permitido mínimo 8000, máximo 150000 x hora.')
        print('x' * 80)

def validarAprobacion(v1,v2,v3,estudianteCl):
    res = v1 + v2 + v3
    estudianteCl['notaFinal'] = res
    if res >= 3.0:
        estudianteCl['aprobacion'] = 'Aprobado'
    else:
        estudianteCl['aprobacion'] = 'Reprobado'
    return estudianteCl

estudiantes = {}

while True:
    try:
        print('CALIFICACIONES'.center(80,' '))

        codigo = int(input('\nCod. estudiante: '))

        if codigo == 999:
            print('\nAdios!.')        
            break

        nombre = input('\nNombre estudiante: ')
        notaA = float(input('\nNota 1: '))
        notaB = float(input('\nNota 2: '))
        notaC = float(input('\nNota 3: '))

        if notaA < 0 or notaA > 5 or notaB < 0 or notaB > 5 or notaC < 0 or notaC > 5:
            error(2,5)
            continue

        estudiantes[codigo] = {}
        estudiantes[codigo]['nombre'] = nombre
        estudiantes[codigo]['notaA'] = notaA
        estudiantes[codigo]['notaB'] = notaB
        estudiantes[codigo]['notaC'] = notaC
    
    except ValueError:
        error(1)

for clave in estudiantes.keys():
    nA = estudiantes[clave]['notaA'] * 0.3
    nB = estudiantes[clave]['notaB'] * 0.3
    nC = estudiantes[clave]['notaC'] * 0.4

    res = validarAprobacion(nA,nB,nC,estudiantes[clave])
    print('-' * 100)
    print(f'El estudiante {estudiantes[clave]["nombre"]} de código {clave} fue {estudiantes[clave]["aprobacion"]} con una nota de {estudiantes[clave]["notaFinal"]:.2f}')
    print('-' * 100)