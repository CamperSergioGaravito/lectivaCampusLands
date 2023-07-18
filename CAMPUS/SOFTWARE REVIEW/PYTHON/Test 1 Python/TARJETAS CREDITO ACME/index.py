#! /usr/bin/env python3

import json
from datetime import datetime
from os import system
from time import sleep

##### CONSTANTES #####
def constantes(var):
    if var == 'continuar':
        CONTINUAR = '\n> ENTER < para continuar...'
        return CONTINUAR

    if var == 'ruta':
        RUTA = 'database/bdTarjetas.json'
        return RUTA

###### FUNCIONES ######

###### ERRORES ######
def error(cod,e=None,u=None,i=None):
    if cod == 0:
        print('x' * 80)
        print(f'Error inesperado. Error: {e}'.center(80,' '))
        print('x' * 80)

    elif cod == 1:
        print('x' * 80)
        print(f'Error de tipo de valores, Error: {e}'.center(80,' '))
        print('x' * 80)

    elif cod == 2:
        print('x' * 80)
        print(f'El id {e} no está en base de datos.'.center(80,' '))
        print('x' * 80)

    elif cod == 3:
        print('x' * 80)
        print(f'El id {e} solo tiene {u} unidades en base de datos.'.center(80,' '))
        print('x' * 80)

    elif cod == 4:
        print('x' * 80)
        print(f'El {e} {u} debe de tener el formato indicado {i}.'.center(80,' '))
        print('x' * 80)

    elif cod == 5:
        print('x' * 80)
        print(f'El número de validación debe estar entre 100 a 999, {e} no es valido.'.center(80,' '))
        print('x' * 80)
    
    elif cod == 6:
        print('x' * 80)
        print('El número de teléfono debe contener mínimo 7 y máximo 10 digitos,'.center(80,' '))
        print(f'{e} tiene {len(str(e))} digitos y por ello no es valido.'.center(80,' '))
        print('x' * 80)
    
    elif cod == 7:
        print('x' * 80)
        print('Debe seleccionar un sexo, (M) masculino, (F) femenino.'.center(80,' '))
        print('x' * 80)

    elif cod == 8:
        print('x' * 80)
        print(f'Solo hay {e} opciones, la opción {u} es invalida.'.center(80,' '))
        print('x' * 80)

    elif cod == 9:
        print('x' * 80)
        print(f'El {e} debe de {u} {i}'.center(80,' '))
        print('x' * 80)

    elif cod == 10:
        print('x' * 80)
        print(f'El número {e} no está en base de datos.'.center(80,' '))
        print('x' * 80)

##### Templates #####
def template(sel,e=None):
    if sel == 1:
        print('-' * 80)
        print('Bienvenido...'.center(80,' '))
        print('-' * 80)

    elif sel == 2:
        print('-' * 80)
        print('Gestión de tarjetas'.center(80,' '))
        print('ACME'.center(80,' '))
        print('-' * 80)

    elif sel == 3:
        print('-' * 80)
        print('\tMENÚ')
        print('-' * 80)
        print('\n1) Crear nuevo registro\n2) Modificar registro\n3) Eliminar registro\n4) Reportes tarjetas registradas\n5) Salir')
        print('-' * 80)

    elif sel == 4:
        print('-' * 80)
        print('Añadir registro de tarjeta'.center(80,' '))
        print('de crédito'.center(80,' '))
        print('-' * 80)

    elif sel == 5:
        print('-' * 80)
        print('Modificar registro'.center(80,' '))
        print('-' * 80)

    elif sel == 6:
        print('-' * 80)
        print('Historial de tarjetas'.center(80,' '))
        print('registradas'.center(80,' '))
        print('-' * 80)

    elif sel == 7:
        print('-' * 80)
        print('Datos a modificar'.center(80,' '))
        print('-' * 80)
        print('1) Nombre\n2) Teléfono\n3) Sexo\n4) Tipo Card\n5) Num. Card\n6) Fecha de vencimiento\n7) Cod. verificación\n8) Salir')
    
    elif sel == 8:
        print('-' * 80)
        print('Datos modificados exitosamente.'.center(80,' '))
        print('-' * 80)
    
    elif sel == 9:
        print('-' * 80)
        print('Eliminar registro'.center(80,' '))
        print('-' * 80)

    elif sel == 10:
        print('-' * 80)
        print('Menú Reportes trajetas'.center(80,' '))
        print('de crédito'.center(80,' '))
        print('-' * 80)
        print('1) Por id cliente\n2) Por número de tarjeta\n3) Todas las tarjetas\n4) Todos los clientes\n5) Por tipo (todas)\n6) Salir')
    
    elif sel == 11:
        print('-' * 120)
        print(f'Informe de {e}'.center(120,' '))
        print('-' * 120)
        print('| ID\t\t| NOMBRE\t\t| TIPO CARD\t| NÚMERO CARD\t\t| Fecha de vencimiento\t| Cod. verificación')
        print('-' * 120)

### Leer Json registro ###
def leerJsonRegis():
    try:
        with open(constantes('ruta'),'r',encoding='utf-8') as cajaDia:
            dataCaja = json.load(cajaDia)

    except Exception as e:
        dataCaja = {}
    
    return dataCaja

### Validar fechas de vencimiento de la tarjeta ###
def validarFechasVenc(mes,year):
    if mes > 0 and mes < 10:
        pass
    
    else:
        if len(str(mes)) < 2 or len(str(mes)) > 2:
            error(4,'mes',mes,'MM')
            return 'Error'
        elif mes < 1 or mes > 12:
            error(9,'mes','estar entre','1 a 12')
            return 'Error'

    if len(str(year)) < 4 or len(str(year)) > 4:
        error(4,'año',year,'AAAA')
        return 'Error'
    elif year < 2023:
        error(9,'año','ser mayor a',2023)
        return 'Error'

    else:
        return 'ok'

### guardar registro ###
def guardarRegistro(id,registro):
    dbCards = leerJsonRegis()
    user = dbCards.get(id,False)
    """ print(dbCards)
    print('user: ',user) """
    
    if user:
        dbCards[id] = registro
    else:
        dbCards[id] = {}
        dbCards[id] = registro

    with open(constantes('ruta'),'w+',encoding='utf-8') as db:
        json.dump(dbCards,db,indent=4)

### Designar tipo de tarjeta ###
def designarTipocard(sel):
    if sel == 1:
        return 'Master Card'
    if sel == 2:
        return 'Visa'
    if sel == 3:
        return 'American Express'

### Imprimir info ###
def imprimirInfo(data):
    print('-' * 140)
    print('  Registro  '.center(140,' '))
    print('-' * 140)
    print('| DOC. CLIENTE\t| NOMBRE\t| TELÉFONO\t| SEXO')
    print('-' * 140)
    print(f'| {data["CC"]}\t| {data["nombre"]}\t| {data["telefono"]}\t| {data["sexo"]}')
    print('-' * 140,end='\n')
    print('-' * 140)
    print('| TIPO CARD\t| NUM. CARD\t| F. VENCIMIENTO\t| COD. VERIFICACIÓN')
    print('-' * 140)
    print(f'| {data["tipo_card"]}\t\t| {data["numero_card"]}\t| {data["fecha_vencimiento"]}\t\t| {data["cod_verificacion"]}')
    print('-' * 140,end='\n')

### Actualizar Información ###
def actualizarInfo(sel,id,user):
    print('user: ',user)
    if sel == 1:
        data = input('\nNuevo nombre: ').title()
        user['nombre'] = data
        template(8)

    if sel == 2:
        data = int(input('\nNuevo teléfono: '))
        if len(str(data)) < 7 or len(str(data)) > 10:
            error(6,data)
            return
        
        user['telefono'] = data
        template(8)

    if sel == 3:
        data = input('\nNuevo sexo (M/F): ').upper()
        if data != 'M' and data != 'F':
            error(7)
            return
        user['sexo'] = data
        template(8)

    if sel == 4:
        print('\nTipo de tarjeta:\n\n1) Master Card\n2) Visa\n3) Américan Express')
        data = int(input('\nNuevo tipo de card: '))
        if data < 1 or data > 3:
            error(8,3,data)
            return
        user['tipo_card'] = designarTipocard(data)
        template(8)

    if sel == 5:
        data = int(input('\nNuevo num. card: '))
        user['numero_card'] = data
        template(8)

    if sel == 6:
        mesVen = int(input('\nNuevo mes de vencimiento (MM): '))
        yearVen = int(input('\nNuevo año de vencimiento (AAAA): '))
        resValFecha = validarFechasVenc(mesVen,yearVen)

        if mesVen > 0 and mesVen < 10:
            mesVen = f'0{mesVen}'

        if resValFecha == 'Error':
            return
        
        user['fecha_vencimiento'] = str(mesVen)+'/'+str(yearVen)
        template(8)

    if sel == 7:
        data = int(input('\nNuevo cod. verificación (max 999 y min 100): '))
        if data < 100 or data > 999:
            error(5,data)
            return
        user['cod_verificacion'] = data
        template(8)

    if sel == 8:
        return 'salir'

    print('user: ',user)
    guardarRegistro(id,user)

### OPCIONES DEL MENÚ ###

### Modificar registro ###
def modificarRegistro():
    mod = True
    while True:
        try:
            system('clear')
            dataJson = leerJsonRegis()
            template(5)
            
            if mod:
                id = input('\n=> Documento a buscar: ')

            idEncont = dataJson.get(id,False)

            if not idEncont:
                error(2,id)
                continuar = input('\n¿Desea buscar otro registro? (S/N): ').lower()
                if continuar == 'n':
                    break
            
            """ print(idEncont) """
            imprimirInfo(idEncont)
            template(7)

            sel = int(input('\n=> Selección: '))
            if sel < 1 or sel > 8:
                error(8,8,sel)
                input(constantes('continuar'))
                continue

            res = actualizarInfo(sel,id,idEncont)

            if res == 'salir':
                break

            continuar = input('\n¿Desea buscar otro registro? (S/N): ').lower()
            if continuar == 's':
                mod = True
                continue
            
            mod = False

        except ValueError as e:
            error(1,e)
            input(constantes('continuar'))
            
        except Exception as u:
            error(0,u)
            input(constantes('continuar'))        

### Nuevo registro ###
def nuevoRegistro():
    err = False
    registro = {}
    while True:
        try:
            if err:
                selCont = input('\nDesea crear un registro nuevo? (S/N): ').lower()
                if selCont == 'n':
                    break

                err = False

            template(4)
            print('  INFORMACIÓN CLIENTE  '.center(80,'-'))

            documento = int(input('\nNúmero cédula cliente (CC): '))
            nombre = input('\nNombre cliente: ')
            tel = int(input('\nNúmero de teléfono: '))

            if len(str(tel)) < 7 or len(str(tel)) > 10:
                error(6,tel)
                continue

            sexo = input('\nSexo (M/F): ').lower()
            if sexo != 'm' and sexo != 'f':
                error(7)
                continue

            print('  INFORMACIÓN TARJETA DE CRÉDITO  '.center(80,'-'))
            print('  DEL CLIENTE  '.center(80,'-'))

            print('\nTipo de tarjeta:\n\n1) Master Card\n2) Visa\n3) Américan Express')

            tipoTrajeta = int(input('\n=> Selección: '))
            if tipoTrajeta < 1 or tipoTrajeta > 3:
                error(8,3,tipoTrajeta)
                continue

            tipoTrajeta = designarTipocard(tipoTrajeta)
            numTrajeta = int(input('\nNúmero tarjeta de crédito: '))

            mesVen = int(input('\nMes de vencimiento (MM): '))
            yearVen = int(input('\nAño de vencimiento (AAAA): '))
            resValFecha = validarFechasVenc(mesVen,yearVen)

            if mesVen > 0 and mesVen < 10:
                mesVen = f'0{mesVen}'

            if resValFecha == 'Error':
                err = True
                continue
            
            codVerif = int(input('\nCod. de verificación (max 999 y min 100): '))
            if codVerif < 100 or codVerif > 999:
                error(5,codVerif)
                continue
            
            registro['CC'] = documento
            registro['nombre'] = nombre.title()
            registro['telefono'] = tel
            registro['sexo'] = sexo.upper()
            registro['tipo_card'] = tipoTrajeta
            registro['numero_card'] = numTrajeta
            registro['fecha_vencimiento'] = str(mesVen)+'/'+str(yearVen)
            registro['cod_verificacion'] = codVerif
            guardarRegistro(documento,registro)
            
            continuar = input('\n¿Desea agregar otro registro? (S/N): ').lower()
            if continuar == 'n':
                break

            input(constantes('continuar'))

        except ValueError as e:
            error(1,e)
            err = True
            
        except Exception as u:
            error(0,u)
            err = True

### Actualizar registros ###
def eliminarId(id):
    dataJson = leerJsonRegis()
    user = dataJson.get(id,False)

    if user:
        dataJson.pop(id)
    else:
        error(2,id)
        return
    
    with open(constantes('ruta'),'w',encoding='utf-8') as db:
        json.dump(dataJson,db,indent=4)


### Eliminar registro ###
def eliminarRegistro():
    while True:
        try:
            system('clear')
            dataJson = leerJsonRegis()
            template(9)
            
            id = input('\n=> Documento a buscar: ')

            idEncont = dataJson.get(id,False)

            if not idEncont:
                error(2,id)
                continuar = input('\n¿Desea buscar otro registro? (S/N): ').lower()
                if continuar == 'n':
                    break
                continue
            
            """ print(idEncont) """
            imprimirInfo(idEncont)

            confirmar = input(f'\n¿Está seguro de eliminar a {id}? (S/N): ').lower()
            if confirmar == 's':
                eliminarId(id)
                print(f'\nEl id {id} fue eliminado exitosamente...')

            continuar = input('\n¿Desea eliminar otro registro? (S/N): ').lower()
            if continuar == 'n':
                break

        except ValueError as e:
            error(1,e)
            input(constantes('continuar'))
            
        except Exception as u:
            error(0,u)
            input(constantes('continuar'))        

### Mostrar información de reporte ###
def mostrarInfoRepor(info,opc):
    '| ID\t\t| NOMBRE\t\t| TIPO CARD\t| NÚMERO CARD\t\t| Fecha de vencimiento\t| Cod. verificación'
    if opc == 1:
        print(f'\n| {info[0]}\t| {info[1]}\t\t| {info[2]}\t\t| {info[3]}\t\t| {info[4]}\t\t| {info[5]}',end='\n')
    
    if opc == 2:
        imprimirInfo(info)
    

### iterar y obtener resultados ###
def iterarData(data,clave,val):
    for i in data.keys():
        if data[i][clave] == val:
            return data[i]
        
    return 'noData'

### Imprimir reportes ###
def generarReportes(sel):
    dataJson = leerJsonRegis()

    if sel == 1:
        id = input('\nId cliente: ')
        user = dataJson.get(id,False)
        if not user:
            error(2,id)
            return 'error'
        inf = [user['CC'],user['nombre'],user['tipo_card'],user['numero_card'],user['fecha_vencimiento'],user['cod_verificacion']]
        template(11,id)

    if sel == 2:
        id = int(input('\nNúmero de tarjeta: '))
        res = iterarData(dataJson,'numero_card',id)

        if res == 'noData':
            error(10,id)
            return 'error'
        
        inf = res

    mostrarInfoRepor(inf,sel)

### Reportes ###
def reportes():
    while True:
        try:
            template(10)
            select = int(input('\n=> Selección: '))
            if select < 1 or select > 6:
                error(8,6,select)
                continue

            if select == 6:
                break

            res = generarReportes(select)
            if res == 'error':
                input(constantes('continuar'))
                continue

        except ValueError as e:
            error(1,e)
            input(constantes('continuar'))
            
        except Exception as u:
            error(0,u)
            input(constantes('continuar'))

### Menú ###
def menu():
    while True:
        try:
            system('clear')
            template(2)
            template(3)
            sel = int(input('\n=> Selección: '))

            if sel == 1:
                nuevoRegistro()

            elif sel == 2:
                modificarRegistro()

            elif sel == 3:
                eliminarRegistro()
                
            elif sel == 4:
                reportes()

            elif sel == 5:
                print(' :) '*20)
                print('Saliendo del sistema...')
                return 'salir'
        
        except ValueError as e:
            error(1,e)
            input(constantes('continuar'))
            
        except Exception as u:
            error(0,u)
            input(constantes('continuar'))

##### Inicio #####
def inicio():
    template(1)
    sleep(1)
    while True:
        try:
            
            res = menu()
            
            if res == 'salir':
                print('Hasta pronto...')
                print(' :) '*20)
                break
        
        except ValueError as e:
            error(1,e)
            input(constantes('continuar'))
            
        except Exception as u:
            error(0,u)
            input(constantes('continuar'))

inicio()