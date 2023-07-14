#! /usr/bin/env python3

import json
from datetime import datetime
from os import system
from time import sleep

##### CONSTANTES #####
CONTINUAR = '\n> ENTER < para continuar...'
RUTA_INVENTARIO = 'database/inventario.json'
RUTA_CAJA_DIA = 'database/cajaDia.json'

###### FUNCIONES ######

###### ERRORES ######
def error(cod,e=None):
    if cod == 0:
        print('x' * 80)
        print(f'Error inesperado. Error: {e}'.center(80,' '))
        print('x' * 80)
    if cod == 1:
        print('x' * 80)
        print(f'Error de tipo de valores, Error: {e}'.center(80,' '))
        print('x' * 80)

##### Templates #####
def template(sel,e=None):
    if sel == 1:
        print('-' * 80)
        print('Bienvenido...'.center(80,' '))
        print('-' * 80)

    elif sel == 2:
        print('-' * 80)
        print('MICRO ACME'.center(80,' '))
        print('-' * 80)

    elif sel == 3:
        print('-' * 80)
        print('MENÚ'.center(80,' '))
        print('-' * 80)
        print('\n1) Agregar venta\n2) Ver historial de ventas\n3) Ver inventario\n4) Salir')
        print('-' * 80)

### Crear registro ###
def crearRegistro(user=None,accion=None):
    historialDia = {}

    with open(RUTA_CAJA_DIA,'a') as caja:
        date = {"ingreso" : str(datetime.now())}
        date['salida'] = {}
        date['historial'] = {}  
        date['inventario'] = {}
        if user and accion == 'nuevoRegistro':
            date['regAccesos'] = {user[0]:(user[1],user[2])}
        else:
            date['regAccesos'] = {}
        historialDia[1] = date
        print(historialDia)
        json.dump(historialDia,caja,indent=4)

    return RUTA_CAJA_DIA,RUTA_INVENTARIO,historialDia
""" crearRegistro() """

### Ver inventario ###
def verInventario():
    inventario = {}
    with open(RUTA_INVENTARIO) as inv:
        data = json.load(inv)
        for id in data.keys():
            inventario[id] = data[id]

    return inventario

### Mostrar inventario ###
def imprimirInventario(inv):
    print('-' * 80)
    print('INVENTARIO'.center(80,' '))
    print('-' * 80)

    for id in inv.keys():
        print(f'\nId producto: {id}\nProducto: {inv[id]["nombre"]}\nPrecio: {inv[id]["precio"]}\nCantidad: {inv[id]["cantidad"]}',end='\n')
        print(f'Cantidad vendida: {inv[id]["cantidad_vendida"]}\nIVA: {inv[id]["iva"]}')
    
    print('-' * 80)
    input(CONTINUAR)

### CAJA REGISTRADORA ###
def cajaRegis():
    pass
    # empezar a hacer la caja registradora

### Menú ###
def menu():
    while True:
        try:
            template(2)
            template(3)
            sel = int(input('\n=> Selección: '))

            if sel == 1:
                cajaRegis()

            if sel == 3:
                obtInventario = verInventario()
                imprimirInventario(obtInventario)

        
        except ValueError as e:
            error(1,e)
            input(CONTINUAR)
            
        except Exception as u:
            error(0,u)
            input(CONTINUAR)

##### Inicio #####
def inicio():
    template(1)
    sleep(2)
    while True:
        try:
            system('clear')
            template(2)
            documento = int(input('\nDocumento (Número sin comas o puntos): '))
            print(len(str(documento)))
            if len(str(documento)) < 6 or len(str(documento)) > 10:
                print('\nEl documento debe ser de mínimo 6 o máximo 10 caracteres...')
                sleep(2)
                continue
            
            nombre = input('\nSu nombre: ')
            meta = str(datetime.now())
            crearRegistro((documento,nombre,meta),'nuevoRegistro')
            res = menu()
            
            if res == 'salir':
                print('Hasta pronto...')
                break
        
        except ValueError as e:
            error(1,e)
            input(CONTINUAR)
            
        except Exception as u:
            error(0,u)
            input(CONTINUAR)

inicio()