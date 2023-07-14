#! /usr/bin/env python3

#### EJERCICIO EMPRESA ACME ####
'''
id,nombre,horasTrabajadas,valorHora,salarioBruto,eps,pensión,subsidioTransporte,salarioNeto
'''

##### FUNCIONES ####
### Título ###
def titulo():
    nombreEmpresa = ('-' * 80 + '\n' + 'NOMINA ACME'.center(80,' ') + '\n' + '-' * 80)
    print(nombreEmpresa)

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
        print(f'==> Solo hay {e} opciones')
        print('x' * 80)
    
    elif cod == 3:
        print('x' * 80)
        print('==> Solo estan permitidas mínimo 1 hora, máximo 160 horas.')
        print('x' * 80)

    elif cod == 4:
        print('x' * 80)
        print('==> Solo está permitido mínimo 8000, máximo 150000 x hora.')
        print('x' * 80)

    elif cod == 5:
        print('x' * 80)
        print(f'==> El id {e} no se encuentra registrado.')
        print('x' * 80)

    elif cod == 6:
        print('x' * 80)
        print(f'==> No se encuentran datos registrados.')
        print('x' * 80)

### Calcular salario ###
def calcSalario(hrsTra,vlrHra):
    SMMLV = 1_160_000
    SUB_TRANS = 140_606
    EPS = 0.04
    PENSION = 0.04

### Crear registro usuario ###
def crearRegistro(data,dict):
    dict[data[0]] = {}
    dict[data[0]]['nombre'] = data[1]
    dict[data[0]]['hrsTra'] = data[2]
    dict[data[0]]['vlrHra'] = data[3]

### Buscar ###
def acciones(data,empleados,accion):
    if len(empleados) == 0 and accion != 1:
        return -1
    elif len(list(empleados.keys())) == 0 and accion == 1:
        id = 1
        data.insert(0,id)
        crearRegistro(data,empleados)
        return empleados
    else:
        for i in empleados.keys():
            print(i)
            if i == data[0]:
                pass
            if accion == 1:
                id = len(empleados) + 1
                data.insert(0,id)
                crearRegistro(data,empleados)
                return empleados


### INGRESO DATOS ###
def ingresoDatos(sel):
    while True:
        try:
            if sel == 1:
                nombre = input('\nNombre: ')
                hrsTra = int(input('\nHoras Trabajadas: '))
                if hrsTra < 1:
                    error(3)
                    continue

                vlrHra = int(input('\nValor x Hora: '))
                if vlrHra < 8_000 or vlrHra > 150_000:
                    error(4)
                    continue

                return list([nombre,hrsTra,vlrHra])

        except ValueError:
            error(1)
        except Exception as e:
            error(0,e)

### Menú ###
def menu():
    empleados = {}
    
    menu = ('-'*80) + '\n' + 'Menu'.center(80,' ') + '\n' + '-'*80 + '\n1- Agregar empleado\n2- Modificar empleado\n3- Buscar empleado\n4- Eliminar empleado\n5- Listar empleados\n6- Listar nómina de un empleado\n7- Listar nómina\n8- Salir'
    while True:
        try:
            print(menu)
            select = int(input('\n>> Escoja una opción (1-8): '))
            if select < 1 or select > 8:
                error(2,8)
                continue
            
            datos = ingresoDatos(select)
            res = acciones(datos,empleados,select)

            if res == -1:
                error(6)
                continue
            
            print(res)
            empleados = res
            

            input('>> Presione ENTER para volver al menú...')

        except ValueError:
            error(1)
        except Exception as e:
            error(0,e)
        
### Inicio ###
'------------------------------------------------------------------------------------'
titulo()
menu()