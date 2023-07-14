#! /usr/bin/env python3

import io

## contar lineas
""" fd = open("archivos/mbox-short.txt", "r",encoding="utf-8")

cont = 0

for linea in fd:
    cont += 1

fd.close()

print(cont) """

# contar lineas que empiezan con From
""" fd = open("archivos/mbox-short.txt")

cont = 0

for linea in fd:
    if linea.lower().find('from') > -1:
        cont += 1

fd.close()

print(cont) """

# contar lineas que contengan @uct.ac.za
""" fd = open("archivos/mbox-short.txt")

cont = 0

for linea in fd:
    line = linea.rstrip()
    if not "@uct.ac.za" in line:
        continue

    print(line)

fd.close()

print(cont) """

####

""" fd = open("archivos/mbox-short.txt")

cont = 0

for linea in fd:
    if linea.find('Subject') > -1:
        cont += 1

fd.close()

print(cont) """

##############
""" fd = open("archivos/mbox-short.txt")

cont = 0

for linea in fd:
    print(linea.upper())

fd.close()

print(cont) """

########

fd = open('archivos/mbox-short.txt')

msg = "Enviado [ok]"
correosEnv = []

for line in fd:
    if line.startswith('From'):
        cr = line.replace('From: ','').strip()
        print('>>',line)
        correosEnv.append()
    else:
        print('xx ',line)    


fd.close()

for email in range(0,len(correosEnv)):
    print(f'{msg} {correosEnv[email]}')