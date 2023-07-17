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
def error(cod,e=None,u=None):
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
        print(f'El id {e} no está en inventario.'.center(80,' '))
        print('x' * 80)

    elif cod == 3:
        print('x' * 80)
        print(f'El id {e} solo tiene {u} unidades en inventario.'.center(80,' '))
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

    elif sel == 4:
        print('-' * 80)
        print('CAJA REGISTRADORA'.center(80,' '))
        print('-' * 80)

    elif sel == 5:
        print('-' * 80)
        print(f'Total compra: {e}'.center(80,' '))
        print('-' * 80)

    elif sel == 6:
        print('-' * 80)
        print('Factura de compra'.center(80,' '))
        print('-' * 80)
        print('MICRO ACME'.center(80,' '))
        print('-' * 80)


### Crear registro ###
def crearRegistro(user,accion,hora,numRegistro):
    """ print(numRegistro,'Num re') """

    dataCaja = leerJsonRegis()

    """ print(len(dataCaja)) """
    if accion == 'ingreso':
        dataCaja[numRegistro] = {}
        dataCaja[numRegistro]['historial'] = {}
        dataCaja[numRegistro]['inventario'] = {}

    dataCaja[numRegistro][accion] = {user[0]:(user[1],hora)}

    with open(RUTA_CAJA_DIA,'w+') as caja:
        json.dump(dataCaja,caja,indent=4)
    
    return str(numRegistro)

### Leer Json registro ###
def leerJsonRegis():
    try:
        with open(RUTA_CAJA_DIA,'r',encoding='utf-8') as cajaDia:
            dataCaja = json.load(cajaDia)

    except Exception as e:
        dataCaja = {}
    
    return dataCaja

### Guardar factura ###
def guardarFactura(factura,numRegistro):
    dataCaja = leerJsonRegis()
    """ print(dataCaja)
    print(len(dataCaja.keys()))
    print('nfactura >',factura) """
    numFact = len(dataCaja[numRegistro]['historial'])
    
    dataCaja[numRegistro]['historial'][numFact+1] = factura


    with open(RUTA_CAJA_DIA,'w+') as cajaDia:
        json.dump(dataCaja,cajaDia,indent=4)
    

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
    system('clear')
    print('-' * 80)
    print('INVENTARIO'.center(80,' '))
    print('-' * 80)

    for id in inv.keys():
        print(f'\nId producto: {id}\nProducto: {inv[id]["nombre"]}\nPrecio: {inv[id]["precio"]}\nCantidad: {inv[id]["cantidad"]}',end='\n')
        print(f'Cantidad vendida: {inv[id]["cantidad_vendida"]}\nIVA: {inv[id]["iva"]}')
    
    print('-' * 80)
    input(CONTINUAR)

def calcularVlrProd(product,cantVendida,idProd):
    nombreProd = product['nombre']
    vlrProdUni = product['precio']
    vlrTotalProd = product['precio'] * cantVendida
    iva = product['iva'] * 100
    totalIva = vlrTotalProd * product['iva']
    totalPagarProd = totalIva + vlrTotalProd

    return {
            "id":idProd,
            "nombre":nombreProd,
            "cantidad":cantVendida,
            "vlrUnidad":vlrProdUni,
            "totalProd":vlrTotalProd,
            "iva":iva,
            "totalIva":totalIva,
            "totalPagar":totalPagarProd
            }
            
### Imprimir factura ###
def imprimirFactura(factura):
    total = 0
    print('-' * 140)
    print('MICRO ACME')
    print('-' * 140)
    print('FACTURA DE COMPRA'.center(140,' '))
    print('-' * 140)
    print('\n| Item\t| Id prod\t| Producto\t\t| Cantidad\t| Vlr und\t| V. bruto\t| Iva %\t| Total iva\t| Total')
    print('-' * 140)
    for i in factura.keys():
        total += factura[i]["totalPagar"]
        if len(factura[i]["nombre"]) > 15:
            print(f'\n| {i}\t| {factura[i]["id"]}\t\t| {factura[i]["nombre"]}\t| {factura[i]["cantidad"]}\t| ${factura[i]["vlrUnidad"]:,.0f}\t| ${factura[i]["totalProd"]:,.0f}\t| {factura[i]["iva"]}%\t| ${factura[i]["totalIva"]:,.0f}\t| ${factura[i]["totalPagar"]:,.0f}')
        else:
            print(f'\n| {i}\t| {factura[i]["id"]}\t\t| {factura[i]["nombre"]}\t\t| {factura[i]["cantidad"]}\t\t| ${factura[i]["vlrUnidad"]:,.0f}\t| ${factura[i]["totalProd"]:,.0f}\t| {factura[i]["iva"]}%\t| ${factura[i]["totalIva"]:,.0f}\t| ${factura[i]["totalPagar"]:,.0f}')
        print('-' * 140)

    print(f'Total Neto: ${total:,.0f} <==')
    print('-' * 140)

### Imprimir total ###
def sumarTotales(factura,docClient):
    total = 0
    for i in factura[docClient].keys():
        total += factura[docClient][i]['totalPagar']
    
    return total

### CAJA REGISTRADORA ###
def cajaRegis(inventario,numRegistro):
    factura = {}
    puertaDocCliente = True
    item = 0

    while True:
        try:
            system('clear')
            """ print('=> factura: ',factura,'n') """
            template(2)
            template(4)
            if len(factura) > 0:
                total = sumarTotales(factura,docCliente)
                template(5,total)

            if puertaDocCliente:
                docCliente = int(input('\nDocumento cliente: '))
                if len(str(docCliente)) < 8 or len(str(docCliente)) > 10:
                    print('\nEl documento debe ser de mínimo 8 o máximo 10 caracteres...')
                    sleep(2)
                    continue
                
                puertaDocCliente = False
                factura[docCliente] = {}

            idProd = input('\nId producto: ').upper()
            prodEncon = inventario.get(idProd)
            
            if not prodEncon:
                error(2,idProd)
                continue
            
            cantProd = int(input('\nCantidad a comprar: '))
            if cantProd < 1 or cantProd > prodEncon['cantidad']:
                error(3,idProd,prodEncon['cantidad'])
                continue
            
            item += 1
            regVenta = calcularVlrProd(prodEncon,cantProd,idProd)
            factura[docCliente][item] = regVenta
            
            cobrar = input('\nDesea realizar el cobro de la venta? (S/N): ').lower()
            if cobrar == 's':
                system('clear')
                imprimirFactura(factura[docCliente])
                ### guardar la factura
                guardarFactura(factura,numRegistro)
                factura = {}
                puertaDocCliente = True
                docCliente = None
                input(CONTINUAR)
                break

        except ValueError as e:
            error(1,e)
            input(CONTINUAR)
            
        except Exception as u:
            error(0,u)
            input(CONTINUAR)

### Ver historial de ventas ###
def historialVentas(numRegistro):
    system('clear')
    dataCaja = leerJsonRegis()
    print('-'*80)
    print('HISTORIAL DE VENTAS'.center(80,' '))
    for f in dataCaja[numRegistro]['historial'].keys():
        print('-'*80,end='\n')
        print(f'\nNúmero factura: {f}')
        for d in dataCaja[numRegistro]['historial'][f].keys():
            print(f'\nDoc. cliente: {d}\n')
            dt = dataCaja[numRegistro]['historial'][f]
            imprimirFactura(dt[d])
    
    input(CONTINUAR)

### Menú ###
def menu(numRegistro,documento,nombre):
    while True:
        try:
            system('clear')
            template(2)
            template(3)
            sel = int(input('\n=> Selección: '))
            obtInventario = verInventario()

            if sel == 1:
                cajaRegis(obtInventario,numRegistro)

            elif sel == 2:
                historialVentas(numRegistro)

            elif sel == 3:
                imprimirInventario(obtInventario)

            elif sel == 4:
                print(' :) '*20)
                print('Saliendo del sistema...')
                x = crearRegistro((documento,nombre),'salida',str(datetime.now()),numRegistro)
                return 'salir'
        
        except ValueError as e:
            error(1,e)
            input(CONTINUAR)
            
        except Exception as u:
            error(0,u)
            input(CONTINUAR)

##### Inicio #####
def inicio():
    template(1)
    sleep(1)
    while True:
        try:
            system('clear')
            template(2)
            documento = int(input('\nDocumento (Número sin comas o puntos): '))
            if len(str(documento)) < 8 or len(str(documento)) > 10:
                print('\nEl documento debe ser de mínimo 8 o máximo 10 caracteres...')
                sleep(2)
                continue
            
            nombre = input('\nSu nombre: ').title()
            meta = str(datetime.now())
            reg = len(leerJsonRegis()) + 1

            numRegistro = crearRegistro((documento,nombre),'ingreso',meta,reg)
            res = menu(numRegistro,documento,nombre)
            
            if res == 'salir':
                print('Hasta pronto...')
                print(' :) '*20)
                break
        
        except ValueError as e:
            error(1,e)
            input(CONTINUAR)
            
        except Exception as u:
            error(0,u)
            input(CONTINUAR)

inicio()