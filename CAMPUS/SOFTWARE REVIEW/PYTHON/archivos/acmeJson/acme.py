#! /usr/bin/env python3

import json
#### EJERCICIO EMPRESA ACME ####
'''
id,nombre,horasTrabajadas,valorHora,salarioBruto,eps,pensión,subsidioTransporte,salarioNeto
'''
""" print('-' * 140)
print('ID t| NOMBRE tt| H. TRABAJADAS t| V. HORA t| S. BRUTO t| EPS t| PENSIÓN t| SUB. TRANSP. t| S. NETO')
print('-' * 140) """

##### FUNCIONES ####

### Update database ###
def updateDatabase(data,ruta):
    newJson = {}
    
    with open(ruta,'w') as db:
        if data:
            for i in data.keys():
                """ print(type(i)) """
                newJson[i] = []
                newJson[i].append({
                        "nombre": data[i]["nombre"],
                        "hrsTra": data[i]["hrsTra"],
                        "vlrHra": data[i]["vlrHra"]
                    })

        print(newJson)  

    
        json.dump(newJson,db,indent=4)
        

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

    elif cod == 7:
        print('x' * 80)
        print(f'==> El id {e} ya se encuentra registrado.')
        print('x' * 80)

### Calcular salario ###
def calcSalario(hrsTra,vlrHra):
    SMMLV = 1_160_000
    SUB_TRANS = 140_606
    EPS = 0.04
    PENSION = 0.04

    salarioBruto = int(hrsTra) * int(vlrHra)
    if salarioBruto > SMMLV:
        subTrans = 0
    else:
        subTrans = SUB_TRANS
    eps = salarioBruto * EPS
    pension = salarioBruto * PENSION
    descuento = eps + pension
    
    if subTrans > 0:
        subTrans -= eps + pension
        salarioNeto = salarioBruto + subTrans

    else:
        salarioNeto = salarioBruto - descuento

    
    return [eps,pension,descuento,subTrans,salarioBruto,salarioNeto]

### Crear registro usuario ###
def mostrar(dict,id):
    """ print(dict) """
    nombre = str(dict['nombre']).title()
    hrsTra = int(dict['hrsTra'])
    vlrHra = int(dict['vlrHra'])
    if len(dict["nombre"]) < 6:
        print('{}\t| {}\t\t\t| {}\t\t\t| ${:,}'.format(id,nombre,hrsTra,vlrHra))

    elif len(dict["nombre"]) < 19:
        print('{}\t| {}\t\t| {}\t\t\t| ${:,}'.format(id,nombre,hrsTra,vlrHra))
    else:
        print('{}\t| {} \t| {}\t\t\t| ${:,}'.format(id,nombre,hrsTra,vlrHra))
    
    print('-' * 80)

#### ids empleados ####
def idsEmpleados(dict):
    listIds = []
    for i in dict.keys():
        listIds.append(int(i))
    
    return listIds

##### nómina #####
def nomina(data,id,dict):
    """ print(type(data)) """
    if type(data) == list:
        nombre = dict[id]['nombre']
        hrsTra = int(dict[id]['hrsTra'])
        vlrHra = int(dict[id]['vlrHra'])
        eps = data[0]
        pension = data[1]
        descuento = data[2]
        subTrans = data[3]
        salarioBruto = data[4]
        salarioNeto = data[5]
    else:
        for i in dict.keys():
            nombre = dict[id]['nombre']
            hrsTra = dict[id]['hrsTra']
            vlrHra = dict[id]['vlrHra']
            dict[id]['eps'] = data[0]
            eps = dict[id]['eps']
            dict[id]['pension'] = data[1]
            pension = dict[id]['pension']
            dict[id]['descuento'] = data[2]
            descuento = dict[id]['descuento']
            dict[id]['subTrans'] = data[3]
            subTrans = dict[id]['subTrans']
            dict[id]['salarioBruto'] = data[4]
            salarioBruto = dict[id]['salarioBruto']
            dict[id]['salarioNeto'] = data[5]
            salarioNeto = dict[id]['salarioNeto']

    if len(nombre) < 6:
        print('{}\t| {}\t\t\t| {}\t\t| ${:,} | ${:,.0f} | ${:,.0f} | ${:,.0f} | ${:,} \t| ${:,} | ${:,.0f}'.format(id,nombre,hrsTra,vlrHra,eps,pension,descuento,subTrans,salarioBruto,salarioNeto))

    elif len(nombre) < 19:
        print('{}\t| {}\t\t| {}\t\t| ${:,} | ${:,.0f} | ${:,.0f} | ${:,.0f} | ${:,} \t| ${:,} | ${:,.0f}'.format(id,nombre,hrsTra,vlrHra,eps,pension,descuento,subTrans,salarioBruto,salarioNeto))
    else:
        print('{0}\t| {1} \t| {2}\t\t\t| ${3:,} | ${:,.0f} | ${:,.0f} | ${:,.0f} | ${:,} | ${:,} | ${:,.0f}'.format(id,nombre,hrsTra,vlrHra,eps,pension,descuento,subTrans,salarioBruto,salarioNeto))
    
    print('-' * 140)

### INGRESO DATOS ###
def ingresoDatos(sel,dict,ruta):
    MENU = '\n1) NOMBRE \t2) H. TRABAJADAS \t3) V. HORA'
    HEAD = '-' * 80 + '\n' + 'ID \t| NOMBRE \t\t| H. TRABAJADAS \t| V. HORA' + '\n' + '-' * 80 + '\n'
    while True:
        try:
            if sel == 1:
                ids = idsEmpleados(dict)
                if len(ids) > 0:
                    maxId = max(ids)
                    print(ids, ' == ', maxId)
                    resId = maxId + 1
                else:
                    resId = 1
                nombre = input('\nNombre: ')
                id = resId
                hrsTra = int(input('\nHoras Trabajadas: '))
                if hrsTra < 1 or hrsTra > 160:
                    error(3)
                    continuar = input('\nDesea volver a intentarlo? (S/N): ')
                    if continuar.lower() == 'n':
                        break   
                    continue

                vlrHra = int(input('\nValor x Hora: '))
                if vlrHra < 8_000 or vlrHra > 150_000:
                    error(4)
                    continuar = input('\nDesea volver a intentarlo? (S/N): ')
                    if continuar.lower() == 'n':
                        break   
                    continue
                
                user = dict.get(id)
                if user:
                    error(7,id)
                    continuar = input('\nDesea volver a intentarlo? (S/N): ')
                    if continuar.lower() == 'n':
                        break   
                    continue      
                
                dict.update({id:{'nombre':nombre,'hrsTra':hrsTra,'vlrHra':vlrHra}})
                updateDatabase(dict,ruta)
                print(HEAD)
                mostrar(dict[id],id)
                continuar = input('\nDesea agregar otro empleado? (S/N): ')
                if continuar.lower() == 'n':
                    break             

            if sel == 2:
                modId = int(input('\nId a modificar: '))

                user = dict.get(modId)
                if not user:
                    error(5,modId)
                    continuar = input('\nDesea realizar otro cambio? (S/N): ')
                    if continuar.lower() == 'n':
                        break
                    continue   
                
                print(HEAD)
                mostrar(dict[modId],modId)
                print(MENU)
                opcion = int(input('\n=> Item a modificar: '))    

                if opcion == 1:
                    nombre = input('\nNuevo nombre: ')
                    user.update({"nombre":nombre})
                    
                if opcion == 2:
                    hrsTra = int(input('\nHoras trabajadas: '))
                    if hrsTra < 1:
                        error(3)
                        continuar = input('\nDesea volver a intentarlo? (S/N): ')
                        if continuar.lower() == 'n':
                            break   
                        continue

                    user.update({"hrsTra":hrsTra})

                if opcion == 3:
                    vlrHra = int(input('\nValor x Hora: '))
                    if vlrHra < 8_000 or vlrHra > 150_000:
                        error(4)
                        continuar = input('\nDesea volver a intentarlo? (S/N): ')
                        if continuar.lower() == 'n':
                            break   
                        continue

                    user.update({"vlrHra":vlrHra})

                
                updateDatabase(dict,ruta)

                continuar = input('\nDesea realizar otro cambio? (S/N): ')
                if continuar.lower() == 'n':
                    break

            if sel == 3:
                id = int(input('\nId empleado: '))

                user = dict.get(id)
                if not user:
                    error(5,id)
                    continuar = input('\nDesea realizar otra busqueda? (S/N): ')
                    if continuar.lower() == 'n':
                        break
                    continue

                print(HEAD)
                mostrar(user,id)

                continuar = input('\nDesea realizar otra busqueda? (S/N): ')
                if continuar.lower() == 'n':
                    break
            
            if sel == 4:
                id = int(input('\nId empleado a eliminar: '))
                user = dict.get(id)
                print(user,' < user')
                if not user:
                    error(5,id)
                    continuar = input('\nDesea eliminar otro registro? (S/N): ')
                    if continuar.lower() == 'n':
                        break
                    continue

                print(HEAD)
                mostrar(user,id)

                confirmar = input(f'\n¿Está seguro de eliminar a {dict[id]["nombre"]}? (S/N): ')
                if confirmar.lower() == 's':
                    dict.pop(id)
                    updateDatabase(dict,ruta)
                    # eliminar empleado

                else:
                    print('\nOperación abortada...\n')
                
                continuar = input('\nDesea eliminar otro registro? (S/N): ')
                if continuar.lower() == 'n':
                    break

            if sel == 5:
                print(HEAD)
                for id in dict.keys():
                    mostrar(dict[id],id)

                break

            if sel == 6:
                id = int(input('\nId empleado: '))

                user = dict.get(id)
                if not user:
                    error(5,id)
                    continuar = input('\nDesea realizar otra busqueda? (S/N): ')
                    if continuar.lower() == 'n':
                        break
                    continue

                print('-' * 140)
                print('\nID \t| NOMBRE \t\t| H. TRABAJADAS | V. HORA | EPS      | PENSIÓN  | DESCUENTO | AUX. TRANS. | SALARIO BRUTO | SALARIO NETO')
                print('-' * 140, end='\n')
                data = calcSalario(dict[id]['hrsTra'],dict[id]['vlrHra'])
                nomina(data,id,dict)

                continuar = input('\nDesea realizar otra busqueda? (S/N): ')
                if continuar.lower() == 'n':
                    break

            if sel == 7:
                print('-' * 140)
                print('\nID \t| NOMBRE \t\t| H. TRABAJADAS | V. HORA | EPS      | PENSIÓN  | DESCUENTO | AUX. TRANS. | SALARIO BRUTO | SALARIO NETO')
                print('-' * 140)
                for id in dict.keys():
                    data = calcSalario(dict[id]['hrsTra'],dict[id]['vlrHra'])
                    nomina(data,id,dict)
                
                input('\nPresione Enter para volver al menú...')
                break

            if sel == 8:
                print('Gracias por usar nuetsro sistema, hasta pronto :D.')
                return 'salir'

        except ValueError:
            error(1)
        except Exception as e:
            error(0,e)
### CARGAR JSON ###
def cargarJson():
    try:
        """ empleados = {1: {'nombre': 'maria', 'hrsTra': 99, 'vlrHra': 89600}, 2: {'nombre': 'mateo', 'hrsTra': 78, 'vlrHra': 89600}, 3: {'nombre': 'rosio', 'hrsTra': 50, 'vlrHra': 60000}, 4: {'nombre': 'maria camila', 'hrsTra': 105, 'vlrHra': 140000}} """
        empleados = {}
        ruta = 'archivos/acmeJson/database/db.json'
        with open(ruta,'r') as fLDB:
            fJSON = json.load(fLDB)
            print(fJSON)
            if len(fJSON["data"]) > 0:
                for id in fJSON["data"][0].keys():
                    empleados[id] = fJSON["data"][0][id]

    except Exception as e:
        updateDatabase(None,ruta)
        return empleados,ruta

### Menú ###
def menu():
        cache,ruta = cargarJson()
        
        menu = ('-'*80) + '\n' + 'Menu'.center(80,' ') + '\n' + '-'*80 + '\n1- Agregar empleado\n2- Modificar empleado\n3- Buscar empleado\n4- Eliminar empleado\n5- Listar empleados\n6- Listar nómina de un empleado\n7- Listar nómina\n8- Salir'
        while True:
            try:
                print(cache)

                print(menu)
                select = int(input('\n>> Escoja una opción (1-8): '))
                if select < 1 or select > 8:
                    error(2,8)
                    continue
                
                res = ingresoDatos(select,cache,ruta)

                if res == 'salir':
                    break

                input('>> Presione ENTER para volver al menú...')

            except ValueError:
                error(1)
            except Exception as e:
                error(0,e)

### Inicio ###
'------------------------------------------------------------------------------------'
titulo()
menu()