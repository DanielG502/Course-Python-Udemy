lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista)
multi = lista[4]*2
multi2 = lista[7]*2
multi3 = lista[9]*2

lista[4] = multi
lista[7] = multi2
lista[9] = multi3
#shorcut ejemplo lista[] *= 2 para multiplicar
#otro ejemplo fuera de shorcut
#lista[] = lista[]*2

print(lista)

