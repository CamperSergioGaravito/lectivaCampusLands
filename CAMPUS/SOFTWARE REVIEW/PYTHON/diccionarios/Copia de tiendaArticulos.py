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

def calcularPrecios(cod,cant):
    articulos = {1:"Lapiz",2:"Cuadernos",3:"Borrador",4:"Calculadora",5:"Escuadra"}
    valores = {1:2500,2:3800,3:1200,4:35000,5:3700}

    vlrUnid = valores[cod]
    nameArt = articulos[cod]
    vlrTotalArts = valores[cod] * cant
    return nameArt,vlrTotalArts,vlrUnid

def mostrarFactura(dicc):
    print('Cod.\tArticulo\tCant.\tV. unidad\tV. total')
    totalPagar = 0
    for clave in dicc.keys():
        print('-' * 80)
        if len(dicc[clave]['articulo']) > 5:
            print(f'{clave}\t{dicc[clave]["articulo"]}\t{dicc[clave]["cantidadArts"]}\t${dicc[clave]["vlrUni"]:,.0f}\t\t${dicc[clave]["vlrArts"]:,.0f}')
        else:
            print(f'{clave}\t{dicc[clave]["articulo"]}\t\t{dicc[clave]["cantidadArts"]}\t${dicc[clave]["vlrUni"]:,.0f}\t\t${dicc[clave]["vlrArts"]:,.0f}')

        totalPagar += dicc[clave]['vlrArts']
    
    print('-' * 80)
    print('\t' * 4,f'Total a pagar: ${totalPagar:,.0f}')
        
def inicio(dicc):
    bandera = False
    while True:
        try:
            print('-' * 80)
            print('CAJA REGISTRADORA'.center(80,' '))
            print('-' * 80)
            if bandera:
                mostrarFactura(dicc)
                print('-' * 80)
            print('Cod\tArtículo')
            print('-' * 80)
            print('1:\tLapiz\n2:\tCuadernos\n3:\tBorrador\n4:\tCalculadora\n5:\tEscuadra')
            print('-' * 80)
            codArt = int(input('Cod. artículo: '))
            
            if codArt < 1 or codArt > 5:
                error(2,5)
                continue

            cantArts = int(input('\nCantidad de articulos solicitados: '))
            print('-' * 80)

            if cantArts < 1:
                print('\nDebe ingresar mínimo 1 artículo.')
                continue

            nameArt,vlrTotalArts,vlrUnid = calcularPrecios(codArt,cantArts)
            dicc[codArt] = {}
            dicc[codArt]['articulo'] = nameArt
            dicc[codArt]['cantidadArts'] = cantArts
            dicc[codArt]['vlrUni'] = vlrUnid
            dicc[codArt]['vlrArts'] = vlrTotalArts
            bandera = True

    
        except ValueError:
            error(1)

listaCompras = {}
inicio(listaCompras)