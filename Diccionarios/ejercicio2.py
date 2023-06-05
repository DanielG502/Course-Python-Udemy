"""lista = {
    1 : "Casillas", 15 : "Ramos",
    3 : "Pique", 5 : "Puyol",
    11 : "Capdevila", 14 : "Xabi Alonso",
    16 : "Busquets", 8 : "Xavi Hernandez",
    18 : "Pedrito", 6 : "Iniesta",
    7 : "Villa", 10 : "Messi"
}
dorsal = [1, 15, 3, 5, 11, 14, 16, 8, 18, 6, 7, 10]

print('\n')
print('Numero de Jugadores')
dorsal.sort()
print(dorsal)
print('\n')
respuesta = int(input('Ingrese el Numero del Jugador: '))

if respuesta == 1:
    print(lista[1])
elif respuesta == 15:
    print(lista[15])
elif respuesta == 3:
    print(lista[3])
elif respuesta == 5:
    print(lista[5])
elif respuesta == 11:
    print(lista[11])
elif respuesta == 14:
    print(lista[14])
elif respuesta == 16:
    print(lista[16])
elif respuesta == 8:
    print(lista[8])
elif respuesta == 18:
    print(lista[18])
elif respuesta == 6:
    print(lista[6])
elif respuesta == 7:
    print(lista[7])
elif respuesta == 10:
    print(lista[10])
else:
    print('Numero Incorrecto, vuelve a intentarlo')"""

#otro ejemplo

#Con el siguiente diccionario, debes crear un programa que pregunte al usuario por un número; el programa debe imprimir el jugador al que hace referencia ese número

diccionario = {
    1 : "Casillas", 15 : "Ramos",
    3 : "Pique", 5 : "Puyol",
    11 : "Capdevila", 14 : "Xabi Alonso",
    16 : "Busquets", 8 : "Xavi Hernandez",
    18 : "Pedrito", 6 : "Iniesta",
    7 : "Villa"
}
OpcionJugador = int(input("Ingresa el numero de jugador: "))
if OpcionJugador in diccionario:
    print(diccionario[OpcionJugador])
else:
    print("No es un numero dentro del diccionario")