#en este ejercicio utilizaremos la libreria math y llamaremos el apartado de sqrt para poder sacar una raiz en codigo

from math import sqrt

A = int(input('Ingrese el Valor de a: '))
B = int(input('Ingrese el Valor de b: '))
C = int(input('Ingrese el Valor de c: '))

x1 = 0
x2 = 0

if((B**2) - (4*A*C)) < 0:
    print('No se puede sacar Raiz a un numero negativo')
else: 
    x1 = (-B + sqrt((B**2) - (4*A*C)))/(2*A)
    x2 = (-B - sqrt((B**2) - (4*A*C)))/(2*A)

    print("La Solucion es: \nx1=", x1, "\n x2=", x2)