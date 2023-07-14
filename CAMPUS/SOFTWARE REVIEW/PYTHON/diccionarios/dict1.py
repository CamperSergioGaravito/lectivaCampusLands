

dicccionario_categoria = {1: 25000,
                          2: 30000,
                          3: 40000,
                          4: 45000,
                          5: 60000
                          }

totHonor = 0
docentes = {}
while True:
    cedula = int(input('\nCédula del docente: '))
    nombre = input('\nNombre del docente: ')
    categoria = int(input('\nCategoría del docente: '))
    horas = int(input('\nHoras laboradas en el mes por el docente: '))
    docentes[cedula] = {}
    docentes[cedula]['nombre'] = nombre
    docentes[cedula]['categoria'] = categoria
    docentes[cedula]['horas'] = horas
    
    opc = input('\nDesea agregar otro docente? (S/N): ')

    if opc.lower() == 'n':
        break

print('\nInforme'.center(60,' '))

for k in docentes.keys():
    h = docentes[k]['horas'] * dicccionario_categoria[docentes[k]['categoria']]
    totHonor += h
    print(docentes[k]['nombre'],f'\t${h:,.0f}')

print(f'\nTotal honorarios docentes: ${totHonor:,.0f}')