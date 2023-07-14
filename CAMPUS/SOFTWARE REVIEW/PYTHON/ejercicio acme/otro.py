#! /usr/bin/env python3

lista1 = []

while True:
    nombre = input('Nombre: ')
    documento = int(input('Documento: '))
    if len(str(documento)) > 8:
        print('Documento no valido')
        continue
    vlrhora = int(input('Vlrhora: '))
    lista1.append([nombre,documento,vlrhora])
    print(lista1)