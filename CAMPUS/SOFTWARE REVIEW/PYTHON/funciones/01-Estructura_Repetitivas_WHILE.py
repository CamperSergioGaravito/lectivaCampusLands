#! /usr/bin/env python3

####### MENÚ ######
def inicio():
    print('-' * 50)
    print(' MENU '.center(50,' '))
    print('-' * 50)
    print('1- Cantidad de palabras en un String\n2- Calcular el mcd de dos números\n3- Calcular el IVA de una factura\n4- Salir')
    print('-' * 50)
    select = selector('? Selección: ','menu')
    print('select: ',select)

######### SELECTOR ##########
def selector(text,validador):
    select = input(text)
    if validador == 'menu':
        while True:
            try:
                selectInt = int(select)
                if selectInt == 1:
                    palabra = input('\nIngrese la texto: ')
                    res = cantPalabras(palabra)
                    print(f'\nHay {res} palabras en el texto: ')
                    sel = input('Desea ingresar otro texto? (S/N): ')
                    if sel.lower() == 'n':
                        break
                    continue

                if selectInt == 2:
                    print('-' * 50)
                    num1 = int(input('\nIngrese un número: '))
                    num2 = int(input('\nIngrese otro número: '))
                    menor, mayor = buscarMayMen(num1,num2)
                    print(mayor,' ',menor)
                    res1,res2 = algorEuclides(mayor,menor)
                    print('res: ',res1,' ',res2)
            except ValueError:
                print('Error!. Solo ingresar números')
        

    return

############ Buscar número mayor / menor ###########
def buscarMayMen(v1,v2):
    if v1 < v2:
        menor = v1
        mayor = v2
    elif v1 > v2:
        mayor = v1
        menor = v2
    
    return menor,mayor
        

########## ALGORITMO DE EUCLIDES ##########
def algorEuclides(v1,v2):
    while v1 % v2 != 0:
        v1, v2 = v2, v1 % v2
    
    return v1,v2

########## CANT. DE PALABRAS ############
'''1. Cree una función que retorne el número de palabras presentes en un String que le llega cómo parámetro.
(obs: considere que toda palabra válida está separada por un espacio de la anterior)'''
def cantPalabras(palabra):
    print(palabra.count(','))

    if palabra.count(',') > 0:
        palabra = palabra.replace(',',' ')
    if palabra.count('.') > 0:
        palabra = palabra.replace('.',' ')

    cantPalabra = len(palabra.split())
    print('cantPalabra: ', cantPalabra)
    print('palabra: ', palabra)
    return cantPalabra

inicio()