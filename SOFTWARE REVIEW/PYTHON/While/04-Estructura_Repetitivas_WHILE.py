#! /usr/bin/env python3

''' 4. Se ingresan los nombres y notas de estudiantes, indique cual es el promedio del curso, cual es el
estudiante con mayor y menor nota (nombre y nota).
El ingreso se termina cuando el profesor ingrese FIN en el nombre.
'''

from os import system

bandera = True
mayorNota = ['',0]
menorNota = ['',True]
promedio = 0
cont = 0

while bandera:
    estudiante = input('Nombre de estudiante: ')
    if estudiante.lower() != 'salir':
        cont += 1
        nota = float(input('Ingrese la nota: '))
        if nota > mayorNota[1]:
            mayorNota = [estudiante,nota]
        if menorNota[1] == True or nota < menorNota[1]:
            menorNota = [estudiante,nota]
        
        promedio += nota
    else:
        bandera = False

print('El estudiante con mayor nota es: {} con {} puntos'.format(mayorNota[0],mayorNota[1]))
print('El estudiante con menor nota es: {} con {} puntos'.format(menorNota[0],menorNota[1]))
print('El promedio de la clase es: {:.2f} puntos'.format(promedio/cont))