#! /usr/bin/env python3

'''5. Construya un programa que me ayude a encontrar el próximo número de la siguiente serie.
1, 1, 2, -1, 1, -2, ?'''

serie = [1, +1, +2, -1, +1, -2]

print('+'*25)
for x in range(0,len(serie),2):
    resultado = serie[x] + serie[x+1]
    print('{}, {},'.format(serie[x],serie[x+1]),end=' ')

print('{}'.format(resultado))
print('+'*25)