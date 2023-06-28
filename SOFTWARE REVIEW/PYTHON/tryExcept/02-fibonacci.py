#! /usr/bin/env python3

from os import system

fibonacci = 1
res = None
res2 = None
cont = 0

system('clear')
while fibonacci >= 1:
    try:
        cont += 1
        print('{}'.format(fibonacci),end=' | ')
        if fibonacci == 1 and res == None:
            res = fibonacci
            continue
        if fibonacci >= 1 and res:
            if fibonacci > 1:
                res = res2 + fibonacci
            else:
                res += fibonacci
                res2 = fibonacci
                fibonacci = res
                continue
            res2 = fibonacci
            fibonacci = res
        if cont % 5 == 0:
            continuar = input('\n\nDesea continuar (S/N): ')
            print('\n')
            if continuar.lower() == 'n':
                break
    
    except Exception as e:
        print('A ocurrido un error inesperado, error: {}'.format(e))

print('Programa finalizado')