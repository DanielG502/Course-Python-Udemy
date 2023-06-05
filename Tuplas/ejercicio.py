TuplaMes = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
mes = {0 : "Enero", 1 : "Febrero", 2 : "Marzo", 3 : 'Abril', 4 : "Mayo", 5 : "Junio", 6 : "Julio" , 7 : "Agosto", 8 : "Septiembre", 9 : "Octubre", 10 : "Noviembre", 11 : "Diciembre"}

tuplayMes = mes.values() == TuplaMes
print('\n')
numero = int(input('Ingrese el numero de Mes: '))
if numero in mes:
    print(TuplaMes[numero])
else:
    print("Error 404 Not Found")