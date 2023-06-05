"""while True:
    try:
        num1 = int(input('Ingresa un Numero: '))
        resultado = 100 / num1
        print(resultado)
    except ZeroDivisionError:
        print('No se puede Dividir un Cero ')
    finally:
        print('Ejecucion Finalizada')
        break
"""
"""while True:
    try:
        edad = int(input('Ingresa tu Edad: '))
        print('Tu edad es: ',edad)
    except ValueError:
        print('Has colocado un Valor Erroneo')
    finally:
        print('Ejecucion Finalizada')
    break
"""
while True:
    try:
        edad = int(input('Ingresa tu Edad: '))
        print('Tu edad es: ',edad)
        break
    except KeyboardInterrupt:
        print("\nHas cancelado la ejecucion")
        break

#keyboradinterrupt, es para cancelarla con control + c