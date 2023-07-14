#! /usr/bin/env python3

'''Los teléfonos de una empresa tienen el siguiente formato: 
    prefijo-número-extensión donde el prefijo es el código del país +34, 
    y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). 
    Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número
    de teléfono sin el prefijo y la extensión.
'''

""" print(numTel.replace('-',' ').split())
print(numTel.split()) 
print(listaFormato[0].startswith('+'))
print(listaFormato[0].replace('+','').strip())
print(listaFormato[0].replace('+','').strip().isnumeric())
print(listaFormato[1].isnumeric(),' ',len(listaFormato[1]))
print(listaFormato[1].startswith('9'))
print(listaFormato[2].isnumeric(),' ',len(listaFormato[2])) """

while True:
    try:
        print('-' * 30)
        print('El número de teléfono debe de tener el siguiente formato:\nprefijo-número-extensión\nEjemplo: +00-1234567891-00')
        print('-' * 30)
        print('-' * 30)
        numTel = input('Ingrese número de teléfono: ')
        print('-' * 30)
        listaFormato = numTel.replace('-',' ').split()
        if listaFormato[0].startswith('+'):
            listaFormato[0] = listaFormato[0].replace('+','').strip()
            if listaFormato[0].isnumeric() and len(listaFormato[0]) == 2:
                if listaFormato[1].isnumeric() and len(listaFormato[1]) == 10:
                    if listaFormato[2].isnumeric() and len(listaFormato[2]) == 2:
                        break
                    else:
                        print('==> La extensión debe ser de 2 numeros.')
                else:
                    print('==> El número de teléfono debe ser de 10 digitos numericos.')
            else:
                print('==> El prefijo debe ser de 2 digitos numericos.')
        else:
            print('==> El prefijo debe iniciar con el simbolo +')

    except Exception as e:
        print(f'Hubo un error inesperado: {e}')
        
print('Numero de teléfono: {}'.format(listaFormato[1]))