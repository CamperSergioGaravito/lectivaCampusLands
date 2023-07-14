#! /usr/bin/env python3

'''6. La empresa ACME desea calcular el valor de la nómina de N empleados (estos N empleados son
ingresados por el usuario), tanto el sueldo bruto como el sueldo neto. El sueldo bruto se calcula a partir
del valor de la hora y la cantidad de horas trabajadas. A esto se le descuenta el valor de la EPS que es el
4%, el valor de la Pensión que es el 4%. El sueldo neto es el sueldo bruto menos los descuentos. Por
cada empleado se quiere mostrar, el valor del sueldo bruto, cada uno de los descuentos y el valor del
sueldo Neto. Para este ejercicio el valor de la hora es $20.000.

Al final se debe mostrar una estadística con los totales de los salarios brutos, EPS, Pensión y salarios
netos. Luego mostrar el empleado que más gana en salario neto (nombre y salario neto), el empleado
que menos gana en salario neto (nombre y salario neto) y los promedios de sueldos brutos y sueldos
netos.'''

from os import system
from time import sleep

valorNomina = 0
sueldoBruto = 0
sueldoNeto = 0
valorHora = 20000
valorEps = 0.04
valorPension = 0.04
mayorSalNeto = []
menorSalNeto = []


usuarios = [['Carlos Contreras',280000,257600,11200,11200,14],
            ['Mariana Camargo',240000,220800,9600,9600,12],
            ['Fabiola Lopez',160000,147200,6400,6400,8],
            ['Javier Nieves',0,0,0,0,0],
            ['Pablo Corzo',0,0,0,0,0]
            ]

############ Estadisticas #############
def verEstadisticas():
    bandera = True
    promedio = 0
    print(' Estadisticas '.center(30,'-'))
    for x in range(0,len(usuarios)):
        if bandera:
            mayorSalNeto = [usuarios[x][0],usuarios[x][2]]
            menorSalNeto = [usuarios[x][0],usuarios[x][2]]
            bandera = False
        if usuarios[x][2] > mayorSalNeto[1] and usuarios[x][2] != 0:
            mayorSalNeto = [usuarios[x][0],usuarios[x][2]]
        elif usuarios[x][2] < menorSalNeto[1] and usuarios[x][2] != 0:
            menorSalNeto = [usuarios[x][0],usuarios[x][2]]
        
        promedio = promedio + usuarios[x][1]
    
    promedio = promedio / len(usuarios)

    print('\nMenor salario Neto: {} con ${},\nMayor salario Neto: {} con ${},\nPromedio salario bruto: ${:.2f}'.format(
        menorSalNeto[0],menorSalNeto[1],mayorSalNeto[0],mayorSalNeto[1],promedio
    ))

    print('-' * 30,end='\n')

    input('Presione ENTER para ir al menú.')
    menu()

############# Buscar usuario ##############
def buscarUsuario(user):
    bandera = True
    for x in range(0,len(usuarios)):
        if usuarios[x][0].lower() == user.lower():
            cantHoras = float(input('Ingrese cant. horas trabajadas: '))
            sueldoBruto = cantHoras * valorHora
            eps = sueldoBruto * valorEps
            pension = sueldoBruto * valorPension
            sueldoNeto = sueldoBruto - eps - pension
            print('\n','-'*30)
            print('Empleado: {}\nSalario bruto: ${}\nSalario Neto: ${}\n\nDescuentos --------------------\nEPS: ${}\nPensión: ${}\n\nHoras trabajadas: {}'.format(
                user,sueldoBruto,sueldoNeto,eps,pension,cantHoras
            ))

            confirmar = input('¿Confirma los cambios? S/N: ')

            if confirmar.lower() == 's':
                usuarios[x][1] = sueldoBruto
                usuarios[x][2] = sueldoNeto
                usuarios[x][3] = eps
                usuarios[x][4] = pension
                usuarios[x][5] = cantHoras
                print('-'*30)
                bandera = False
            else:
                calcularSalarios()
        
        if bandera == False:
            bandera = True
            break
        

################ Agregar empleado ###############
def agregarEmpleado():
    empleado = input('Nombre de empleado: ')
    usuarios.append([empleado,0,0,0,0,0])
    print('Empleado {} agregado con exito.'.format(empleado))
    sleep(3)
    menu()

##################################
def calcularSalarios():
    system('clear')
    print(' Calcular salario '.center(40,"-"),end='\n')
    print('Se modificarán datos en esta acción, tenga cuidado.\n')
    print('Empleados:\n')
    for x in range(0,len(usuarios)):
        print(usuarios[x][0],end='\n')
    bEmpleado = input('\nIngrese nombre del empleado: ')
    buscarUsuario(bEmpleado)
    print('\n1) Nuevo calculo\n2)Menú\n')
    salir = input('Selección: ')
    if salir == '1':
        calcularSalarios()
    elif salir == '2':
        menu()
    else:
        calcularSalarios()

##################################
def mostrarNomina():
    for empleado in range(0,len(usuarios)):
        print('-' * 30)
        print('Nombre: {}\nSalario bruto: {}\nSalario Neto: {}\nEps: {}\nPensión: {}\nHoras extra: {}'.format(
            usuarios[empleado][0],usuarios[empleado][1],usuarios[empleado][2],usuarios[empleado][3],usuarios[empleado][4],
            usuarios[empleado][5]
        ),end='\n')
        print('-' * 30,'\n')
    input('Enter para salir al menú: ')
    menu()    
##################################
def menu():
    system('clear')
    print('#' * 60)
    print('Seleccione con el número asignado a cada opción:\n')
    print('1) Mostrar nómina\n2) Calcular salarios\n3) Agregar empleado\n4) Ver estadisticas\n')
    seleccionM1 = input('Selección: ')
    if seleccionM1 == '1':
        mostrarNomina()
    elif seleccionM1 == '2':
        calcularSalarios()
    elif seleccionM1 == '3':
        agregarEmpleado()
    elif seleccionM1 == '4':
        verEstadisticas()

##################################
menu()
