num1 = int(input('Ingresa el Primer Numero: '))
num2 = int(input('Ingresa el Segundo Numero: '))

def valores():
    if num1 > num2:
        return 1
    elif num1 < num2:
        return -1
    else:
        num1 == num2
        return 0
    
print(valores())