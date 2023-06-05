"""tupla = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
#convertimos a lista o mas bien lo comparamos
lista = {0 : "A", 1 : "B", 2 : "C", 3 : "D", 4 : "E", 5 : "F", 6 : "G", 7 : "H", 8 : "I", 9 : "J", 10 : "K", 11 : "L", 12 : "M", 13 : "N", 14 : "O", 15 : "P", 16 : "Q", 17 : "R", 18 : "S", 19 : "T", 20 : "U", 21 :  "V", 22 : "W", 23 :"X", 24 : "Y", 25 : "Z"}
print('\n')


numero = int(input('Ingres un numero, para retornar una Vocal: '))

numero -=1
if numero in lista:
    print(tupla[numero])
else:
    print("Error 404, Not Found")
"""

#solucion del codigo en el curso

tupla = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")

opcionMes = int(input('Ingrese el numero de tu Mes: '))

print('El Mes corresponde a: ', tupla[opcionMes-1])

