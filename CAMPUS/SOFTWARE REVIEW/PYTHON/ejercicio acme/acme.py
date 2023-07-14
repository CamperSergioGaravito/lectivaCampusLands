#! /usr/bin/env python3

#### EJERCICIO EMPRESA ACME ####
'''
id,nombre,horasTrabajadas,valorHora,salarioBruto,eps,pensión,subsidioTransporte,salarioNeto
'''

##### FUNCIONES ####
### Título ###
def titulo():
    nombreEmpresa = ('-' * 80 + '\n' + 'NOMINA ACME'.center(80,' ') + '\n' + '-' * 80)
    print(nombreEmpresa)

#### Errores ####
def error(cod,e=None):
    if cod == 0 and e:
        print('x' * 80)
        print(f':( Error inesperado. Error: {e}.')
        print('x' * 80)

    elif cod == 1:
        print('x' * 80)
        print(f'==> Error en tipo de valores de ingreso.')
        print('x' * 80)

    elif cod == 2:
        print('x' * 80)
        print(f'==> Solo hay {e} opciones')
        print('x' * 80)
    
    elif cod == 3:
        print('x' * 80)
        print('==> Solo estan permitidas mínimo 1 hora, máximo 160 horas.')
        print('x' * 80)

    elif cod == 4:
        print('x' * 80)
        print('==> Solo está permitido mínimo 8000, máximo 150000 x hora.')
        print('x' * 80)

    elif cod == 5:
        print('x' * 80)
        print('==> El id {e} no se encuentra registrado.')
        print('x' * 80)

### Calcular salario ###
def calcSalario(hrsTrabajadas,vlrHora,op=None,subTrans=0,eps=0,pension=0):
    SMMLV = 1_160_000
    SUB_TRANS = 140_606
    EPS = 0.04
    PENSION = 0.04
    salarioBruto = hrsTrabajadas * vlrHora

    if op:
        if subTrans == 0:
            subTrans = SUB_TRANS
        if eps == 0:
            eps = EPS
        if pension == 0:
            pension = PENSION
        if salarioBruto < SMMLV:
            descuento = salarioBruto * (eps + pension)
            salarioNeto = (salarioBruto + subTrans) - descuento
            return salarioBruto,eps*100,pension*100,subTrans,salarioNeto
        else:
            descuento = salarioBruto * (eps + pension)
            salarioNeto = salarioBruto - descuento
            return salarioBruto,eps*100,pension*100,0,salarioNeto
    else:        
        if salarioBruto < SMMLV:
            descuento = salarioBruto * (EPS + PENSION)
            salarioNeto = salarioBruto + (SUB_TRANS - descuento)
            return salarioBruto,EPS*100,PENSION*100,SUB_TRANS,salarioNeto
        else:
            descuento = salarioBruto * (EPS + PENSION)
            salarioNeto = salarioBruto - descuento
            return salarioBruto,EPS*100,PENSION*100,0,salarioNeto
       

### Opciones menú mod por usuario id ###
def validarOpciones(select,lista):
    if select == 1:
        nuevoValor = input('\nNuevo nombre: ')
        result = accionEmpleado(nuevoValor,2,lista,select)
    elif select == 2:
        nuevoValor = int(input('\nHoras trabajadas: '))
        result = accionEmpleado(nuevoValor,2,lista,select,)
    elif select == 3:
        nuevoValor = int(input('\nValor hora (valor sin puntos): '))
        result = accionEmpleado(nuevoValor,2,lista,select,)
    elif select == 4:
        nuevoValor = int(input('\nS. bruto: '))
        result = accionEmpleado(nuevoValor,2,lista,select,)
    elif select == 5:
        nuevoValor = float(input('\nEPS: '))
        result = accionEmpleado(nuevoValor,2,lista,select,)
    elif select == 6:
        nuevoValor = float(input('\nPensión: '))
        result = accionEmpleado(nuevoValor,2,lista,select,)
    elif select == 7:
        nuevoValor = int(input('\nSubsidio de transporte: '))
        result = accionEmpleado(nuevoValor,2,lista,select,)
    elif select == 8:
        nuevoValor = int(input('\nNuevo salario neto: '))
        result = accionEmpleado(nuevoValor,2,lista,select,)

    salarioBruto,eps,pension,subTrans,salarioNeto = calcSalario(result[2],result[3],1,result[7],result[5]/100,result[6]/100)
    result = [result[0],result[1],result[2],result[3],salarioBruto,eps,pension,subTrans,salarioNeto]
    return result

### Buscar ###
def buscar(id,lista,mod=0,bus=0):
    menu = '\n1) NOMBRE \t2) H. TRABAJADAS \t3) V. HORA \t4) S. BRUTO \t5) EPS \t6) PENSIÓN \t7) SUB. TRANSP. \t8) S. NETO'

    for pos in range(0,len(lista)):
        if mod == 1:
            if lista[pos][0] == id:
                if bus == 1:
                    print('-' * 140)
                    print('ID \t| NOMBRE \t| H. TRABAJADAS \t| V. HORA \t| S. BRUTO \t| EPS \t| PENSIÓN \t| SUB. TRANSP. \t| S. NETO')
                    print('-' * 140)
                    print(f'\n{lista[pos][0]} \t| {lista[pos][1]} \t| {lista[pos][2]} \t\t\t| ${lista[pos][3]:,.0f} \t| ${lista[pos][4]:,.0f} \t| {lista[pos][5]:.0f}% \t| {lista[pos][6]:.0f}% \t\t| ${lista[pos][7]:,.0f} \t| ${lista[pos][8]:,.0f}')
                    print('-' * 140)
                    continuar = input('\n¿Desea buscar de nuevo? (S/N): ')
                    if continuar.lower() == 'n':
                        return 'salir'
                    return
                
                elif bus == 2:
                    print('-' * 140)
                    print('ID \t| NOMBRE \t| H. TRABAJADAS \t| V. HORA \t| S. BRUTO \t| EPS \t| PENSIÓN \t| SUB. TRANSP. \t| S. NETO')
                    print('-' * 140)
                    print(f'\n{lista[pos][0]} \t| {lista[pos][1]} \t| {lista[pos][2]} \t\t\t| ${lista[pos][3]:,.0f} \t| ${lista[pos][4]:,.0f} \t| {lista[pos][5]:.0f}% \t| {lista[pos][6]:.0f}% \t\t| ${lista[pos][7]:,.0f} \t| ${lista[pos][8]:,.0f}')
                    print('-' * 140)
                    confirmar = input(f'\n¿Esta seguro de borrar a {lista[0][1]} con código {lista[pos][0]}? (S/N): ')

                    if confirmar.lower() == 's':
                        try:
                            lista.remove(lista[pos])

                        except ValueError:
                            error(5,lista[pos][0])
                        

                    continuar = input('\n¿Desea buscar de nuevo? (S/N): ')
                    if continuar.lower() == 'n':
                        return 'salir'
                    return

                else:
                    while True:
                        try:
                            print('-' * 140)
                            print('ID \t| NOMBRE \t| H. TRABAJADAS \t| V. HORA \t| S. BRUTO \t| EPS \t| PENSIÓN \t| SUB. TRANSP. \t| S. NETO')
                            print('-' * 140)
                            text = f'\n{lista[pos][0]} \t| {lista[pos][1]} \t| {lista[pos][2]} \t\t\t| ${lista[pos][3]:,.0f} \t| ${lista[pos][4]:,.0f} \t| {lista[pos][5]:.0f}% \t| {lista[pos][6]:.0f}% \t\t| ${lista[pos][7]:,.0f} \t| ${lista[pos][8]:,.0f}'
                            print(text)
                            print('-' * 140)
                            print(menu)
                            select = int(input('\n>> Selección: '))
                            if select > 0:
                                result = validarOpciones(select,lista[pos])
                                lista[pos] = result
                            else:
                                error(2,8)                        

                            continuar = input('\n¿Desea modificar algun otro dato? (S/N): ')
                            if continuar.lower() == 'n':
                                return 'salir'

                        except ValueError:
                            error(1)
                        except Exception as e:
                            error(0,e)
                
        elif mod == 2:
            if id < 2:
                print('-' * 140)
                print('ID \t| NOMBRE \t| H. TRABAJADAS \t| V. HORA')
                print('-' * 140)
                id += 1
            if lista[pos][8] < 1_000_000:
                print(f'\n{lista[pos][0]} \t| {lista[pos][1]} \t| {lista[pos][2]} \t\t\t| ${lista[pos][3]:,.0f}')
                
            else:
                print(f'\n{lista[pos][0]} \t| {lista[pos][1]} \t| {lista[pos][2]} \t\t\t| ${lista[pos][3]:,.0f}')

            print('-' * 140)

        elif mod == 3:
            if id < 2:
                print('-' * 140)
                print('ID \t| NOMBRE \t| H. TRABAJADAS \t| V. HORA \t| S. BRUTO \t| EPS \t| PENSIÓN \t| SUB. TRANSP. \t| S. NETO')
                print('-' * 140)
                id += 1
            if lista[pos][8] < 1_000_000:
                print(f'\n{lista[pos][0]} \t| {lista[pos][1]} \t| {lista[pos][2]} \t\t\t| ${lista[pos][3]:,.0f} \t| ${lista[pos][4]:,.0f} \t| {lista[pos][5]:.0f}% \t| {lista[pos][6]:.0f}% \t\t| ${lista[pos][7]:,.0f} \t| ${lista[pos][8]:,.0f}')
                
            else:
                print(f'\n{lista[pos][0]} \t| {lista[pos][1]} \t| {lista[pos][2]} \t\t\t| ${lista[pos][3]:,.0f} \t| ${lista[pos][4]:,.0f} \t| {lista[pos][5]:.0f}% \t| {lista[pos][6]:.0f}% \t\t| ${lista[pos][7]:,.0f} \t\t| ${lista[pos][8]:,.0f}')

            print('-' * 140)
        
        elif mod == 4:
            if id < 2:
                print('-' * 140)
                print('ID \t| NOMBRE \t| H. TRABAJADAS \t| V. HORA \t| S. BRUTO \t| EPS \t| PENSIÓN \t| SUB. TRANSP. \t| S. NETO')
                print('-' * 140)
                id += 1
            if lista[pos][8] < 1_000_000:
                print(f'\n{lista[pos][0]} \t| {lista[pos][1]} \t| {lista[pos][2]} \t\t\t| ${lista[pos][3]:,.0f} \t| ${lista[pos][4]:,.0f} \t| {lista[pos][5]:.0f}% \t| {lista[pos][6]:.0f}% \t\t| ${lista[pos][7]:,.0f} \t| ${lista[pos][8]:,.0f}')
                
            else:
                print(f'\n{lista[pos][0]} \t| {lista[pos][1]} \t| {lista[pos][2]} \t\t\t| ${lista[pos][3]:,.0f} \t| ${lista[pos][4]:,.0f} \t| {lista[pos][5]:.0f}% \t| {lista[pos][6]:.0f}% \t\t| ${lista[pos][7]:,.0f} \t\t| ${lista[pos][8]:,.0f}')

            print('-' * 140)

    return -1

### Validación menu opcion 1 ###
def validacion1():
    while True:
        try:
            titulo()
            nombre = input('\nNombre: ')
            hrsTrabajadas = int(input('Horas Trabajadas: '))

            if hrsTrabajadas < 1 or hrsTrabajadas > 160:
                error(3)
                return 'continue'

            vlrHora = int(input('\nValor hora (valor sin puntos): '))

            if vlrHora < 8000 or vlrHora > 150000:
                error(4)
                return 'continue'
            
            return nombre,hrsTrabajadas,vlrHora

        except ValueError:
            error(1)
        except Exception as e:
            error(0,e)

### Menú ###
def menu(lista):
    menu = ('-'*80) + '\n' + 'Menu'.center(80,' ') + '\n' + '-'*80 + '\n1- Agregar empleado\n2- Modificar empleado\n3- Buscar empleado\n4- Eliminar empleado\n5- Listar empleados\n6- Listar nómina de un empleado\n7- Listar nómina\n8- Salir'

    while True:
        try:
            print(menu)
            select = int(input('\n>> Escoja una opción (1-8): '))
            if select < 1 or select > 8:
                error(2,8)
                continue

            if select == 1:
                nombre,hrsTrabajadas,vlrHora = validacion1()
                if nombre == 'continue':
                    continue

                salarioBruto,eps,pension,subTrans,salarioNeto = calcSalario(hrsTrabajadas,vlrHora)

                id = len(lista) + 1
                accionEmpleado([id,nombre,hrsTrabajadas,vlrHora,salarioBruto,eps,pension,subTrans,salarioNeto],1,lista)

            elif select == 2:
                while True:
                    try:
                        id = int(input('\nID USUARIO: '))
                        result = buscar(id,lista,1)

                        if result == -1:
                            error(5,id)
                            continuar = input('\n¿Desea continuar? (S/N): ')
                            if continuar.lower() == 'n':
                                break
                            continue

                        if result == 'salir':
                            break
                    
                    except ValueError:
                        error(1)
                    except Exception as e:
                        error(0,e)

            elif select == 3:
                while True:
                    try:
                        id = int(input('\nID USUARIO: '))
                        result = buscar(id,lista,1,1)

                        if result == -1:
                            error(5,id)
                            continuar = input('\n¿Desea continuar? (S/N): ')
                            if continuar.lower() == 'n':
                                break
                            continue

                        if result == 'salir':
                            break
                    
                    except ValueError:
                        error(1)
                    except Exception as e:
                        error(0,e)

            elif select == 4:
                while True:
                    try:
                        id = int(input('\nID USUARIO: '))
                        result = buscar(id,lista,1,2)

                        if result == -1:
                            error(5,id)
                            continuar = input('\n¿Desea continuar? (S/N): ')
                            if continuar.lower() == 'n':
                                break
                            continue

                        if result == 'salir':
                            break
                    
                    except ValueError:
                        error(1)
                    except Exception as e:
                        error(0,e)

            elif select == 5:
                            while True:
                                try:
                                    result = buscar(1,lista,2)

                                    if result == -1:
                                        continuar = input('\n¿Desea continuar? (S/N): ')
                                        if continuar.lower() == 'n':
                                            break
                                        continue

                                    if result == 'salir':
                                        break
                                
                                except ValueError:
                                    error(1)
                                except Exception as e:
                                    error(0,e)

            input('>> Presione ENTER para volver al menú...')

        except ValueError:
            error(1)
        except Exception as e:
            error(0,e)
        
#### Agregar empleado ###
def accionEmpleado(emple,accion,lista=None,pos=None):
    if accion == 1:
        lista.append(emple)
    elif accion == 2:
        lista[pos] = emple

    return lista

### Inicio ###
'''Se simula una BD, se deja como global porque al tener permisos de modificar datos, 
    ya tendría acceso a la bd posterior a un login.'''
listaEmpleados = [[1, 'camila', 38, 52000, 1976000, 4.0, 4.0, 0, 1817920.0], [2, 'morgana', 68, 35000, 2380000, 4.0, 4.0, 0, 2189600.0], [3, 'marcos', 20, 25000, 500000, 4.0, 4.0, 140606, 600606.0]]
'------------------------------------------------------------------------------------'
titulo()
menu(listaEmpleados)