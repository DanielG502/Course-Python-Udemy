numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

i = 0

for i in range(numero1 , numero2, 2):
    print(i)


#otro modo de hacerlo como lo hicieron en el curso

num1 = int(input("Ingresa el primer Numero: "))
num2 = int(input("Ingresa el segundo Numero: "))

for i in range(num1 , num2 + 1):
    if i % 2 == 0:
        continue
    print(i)