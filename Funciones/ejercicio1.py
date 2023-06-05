lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista)
def agregar():
    num1 = int(input("Hola, ingresa el numero que quieres agregar: "))
    num2 = int(input("Hola, ingresa el numero que quieres agregar: "))
    lista.insert(0, num1)
    lista.insert(10, num2)
agregar()
print(lista)
print('\n')

def ordenar():
    for i in lista:
        if i % 2 == 0:
            print(i)
ordenar()

print('\n')

def ordenar1():
    for i in lista:
        if i % 3 ==0:
            print(i)
ordenar1()

#append() nos permite agregar datos a una lista 
#.sort() ordenar lista en pares y inpares 


#otro metodo para hacer el ejercicio

lista = []
num = 0

def pedir():
    i = 0 
    while i <= 5:
        num = float(input("Ingresa un numero: "))
        lista.append(num)
        i += 1

def ordenar():
    lista.sort()
    pares = []
    impares = []
    for i in lista:
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    print(pares)
    print(impares)

pedir()
ordenar()