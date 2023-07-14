#! /usr/bin/env python3

'''
Hacer un programa que reciba una palabra e indicar si esta es un palíndrome.
Una palabra palíndroma es aquella que se lee igual adelante que atrás.
'''

print(' Validador de palabras palindromas '.center(80,' '))

palindromo = input('\nIngrese una palabra: ')
palindromoBkup = palindromo.replace(' ','')
palindromoBkup = palindromoBkup.replace(',','')

cont = -1
x = 0

while x < len(palindromoBkup):
    try:
        print(palindromoBkup[palindromoBkup.rfind(palindromoBkup[cont])].lower(), ' ',palindromoBkup[palindromoBkup.find(palindromoBkup[x])].lower())
        if palindromoBkup[palindromoBkup.rfind(palindromoBkup[cont])].lower() != palindromoBkup[palindromoBkup.find(palindromoBkup[x])].lower():
            print(f'\nLa palabra "{palindromoBkup}" no es palíndroma')
            siPal = False
            break
        x += 1
        cont -= 1
        siPal = True
    except Exception as e:
        print('\nHa ocurrido un error inesperado.')

if siPal:
    print(f'\nLa palabra "{palindromo}" es palindroma.\n')

    