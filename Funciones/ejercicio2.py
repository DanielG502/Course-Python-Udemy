
num1 = int(input('Ingrese un numero, para sacar el Factorial: '))

def factorial():
    if num1 > 0:
        fact =1
        for i in range(1, num1+1):
            fact*=i
            print('El factorial del {}, es {}'.format(num1, fact))
    else:
        print('Error 404')
factorial()


#tambien puedes importar todo de matematicas, la libreria Math y puedes importar factorial
#ejemplo
#from math import factorial