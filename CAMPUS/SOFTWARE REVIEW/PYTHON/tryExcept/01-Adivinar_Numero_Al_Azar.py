#! /usr/bin/env python3
import random
from os import system
from time import sleep

listJugados = []
menor = [True]
mayor = [True]
reinicia = True
info = None

while True:
    try:
        system('clear')
        if info:
            print('-'*70)
            print('  JUGADOR: {}\t INTENTOS: {}  '.center(60,'-').format(info.upper(),intentos))
            print('-'*70)
        print('-'*30)
        print(' Adivina el número '.center(30, '-'))
        print('-'*30)
        if menor[0] != True and reinicia == True:
            print('\n','-' * 60)
            print('El jugador con menor cantidad de intentos es {}, con {} intentos'.format(menor[0],menor[1]))
            print('-' * 60)
        if mayor[0] != True and reinicia == True:
            print('-' * 60)
            print('El jugador con mayor cantidad de intentos es {}, con {} intentos'.format(mayor[0],mayor[1]))
            print('-' * 60)
        if len(listJugados) != 0:
            print('-' * 60)
            x = 0
            print('Jugadores e intentos en el juego: ')
            while x < len(listJugados):
                print('\n==> {} con {} intentos al Número {}'.format(listJugados[x][0], listJugados[x][1],listJugados[x][2]))
                x += 1
            print('-' * 60)
        if reinicia == True:
            numAle = random.randint(1,100)
            nombre = input('\nIngrese su nombre: ')
            info = nombre
            intentos = 0
            """ print('\nnum rand: ',numAle) """

        numSel = int(input('Ingrese un número (1 - 100): '))
        if 0 < numSel < 101:
            if numSel == numAle:
                print('\n','-' * 60)
                print('Has acertado al Número {} en {} intentos'.format(numAle,intentos))
                print('-' * 60)
                info = None
                reinicia = True
                listJugados.append([nombre.upper(),intentos,numAle])
                if menor[0] == True or intentos < menor[1]:
                    menor = [nombre.upper(),intentos]
                if mayor[0] == True or intentos > mayor[1]:
                    mayor = [nombre.upper(),intentos]
                
                sleep(3)
                continue
            elif numSel > numAle:
                print('\n','-' * 60)
                print('Estas cerca pero muy arriba.')
                print('-' * 60)
            elif numSel < numAle:
                print('\n','-' * 60)
                print('Estas cerca pero muy abajo.')
                print('-' * 60)

            reinicia = False
            intentos += 1
            sleep(2)

        else:
            print('\n','x' * 60)
            print('Los números solo pueden ser desde 1 hasta 100')
            print('x' * 60)
            reinicia = False
            sleep(2)

    except ValueError:
        print('\n','x' * 60)
        print('Error!, debe ingresar un número entero.')
        print('x' * 60)
        reinicia = False
        sleep(2)