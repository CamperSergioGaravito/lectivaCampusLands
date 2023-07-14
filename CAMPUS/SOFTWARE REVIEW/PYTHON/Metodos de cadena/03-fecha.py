#! /usr/bin/env python3

'''
Escribir un programa que pregunte al usuario la fecha de su nacimiento en 
formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa
anterior para que tambien funcione cuando el día o el mes que se introduzcan con 
un solo caracter.
'''

meses = ['enero','febrero','marzo','abril','mayo','junio','julio','agosto',
         'septiembre','octubre','noviembre','diciembre']

año = None
mes = None
dia = None

while True:
    print('-'*60)
    print('Ingrese la fecha de su nacimiento\nen el siguiente formato: dd/mm/aaaa')
    print('-'*60)
    fecha = input('Ingrese fecha: ')
    if fecha.count('/') == 2:
        fecha = fecha.replace('/',' ').split()
        if fecha[0].isalnum() and (0 < len(fecha[0]) < 2 or len(fecha[0]) == 2) and int(fecha[0]) < 32:
            if len(fecha[0]) == 1:
                nueva = '0' + str(fecha[0])
                fecha[0] = nueva
            dia = fecha[0]
        else:
            print('\nError!, la fecha debe ser numerica y en el formato indicado.')
            año = None
            mes = None
            dia = None
            continue
    else:
        print('\nLa fecha debe de ser en el formato indicado.')
        año = None
        mes = None
        dia = None
        continue
    
    if fecha[1].isalnum() and (0 < len(fecha[1]) < 2 or len(fecha[1]) == 2) and int(fecha[1]) < 13:
        if len(fecha[1]) == 1:
            nueva = '0' + str(fecha[1])
            fecha[1] = nueva
        mes = fecha[1]
    else:
        print('\nError!, la fecha debe ser numerica y en el formato indicado.')
        año = None
        mes = None
        dia = None
        continue
    
    if fecha[2].isalnum() and len(fecha[2]) == 4:
        año = fecha[2]
    else:
        print('\nError!, la fecha debe ser numerica y en el formato indicado.')
        año = None
        mes = None
        dia = None
        continue

    if dia and mes and año:
        break

print('\nNaciste el {} de {} de {}'.format(dia,meses[int(mes)-1],año))