numero = int(input("Ingrese un numero "))

"""negativo = numero * -1

print("El numero Positivo es", numero)
print("El numero Negativo es", negativo)"""

if numero > 0:
    print("El Valor absoluto de {} es: {}".format(numero, numero))
else:
    print("El valor absoluto de {} es: ".format(numero), abs(numero))

#metodo facil
#se agrega abs() para sacar el valor absoluto de un numero 