#! /usr/bin/env python3

# 1. Construya un programa que muestro los números divisibles de 3 y 7 entre 1 y 1000.

### Variables ###
contX = []
contY = []
cont = 0

### Muestra de proceso ###
for x in range(1,1000):
    if x % 3 == 0:
        contX.append(x)
    elif x % 7 == 0:
        contY.append(x)

print('#'*30)
print('Divisibles de 3:')
print('#'*79)
for x in range(0,len(contX)):
    cont += 1
    if cont < 10:
        print(f'{contX[x]}\t| ',end='')
    else:
        print(contX[x],end=' #\n')
        cont = 0
print('\n','-' * 78,'\n')

print('#'*30)
print('Divisibles de 7:')
print('#'*79)
cont = 0
for y in range(0,len(contY)):
    cont += 1
    if cont == 1:
        print(f'{contY[y]}\t| ',end='')
    elif cont < 10 and cont != 1:
        print(f'{contY[y]}\t| ',end='')
    else:
        print(contY[y],end=' #\n')
        cont = 0
        
print('\n','-' * 78,'\n')

print('#' * 35)
print(f'Cantidad de divisibles de 3: {len(contX)}')
print('#' * 35)
print(f'Cantidad de divisibles de 7: {len(contY)}')
print('#' * 35)