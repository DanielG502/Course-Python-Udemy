"""lista = []

def llenar():
    i = 0
    valor = 0
    valor = int(input('cuanto numeros quieres ingresar?: '))
    while i < valor:
            num = int(input('Ingresa el numero que quieres registrar: '))
            lista.append(num)
            i +=1
            print(lista)
print(llenar())
print('La cantidad nueva de la lista es {}'.format(len(lista)))"""

"""def medida(*tupla):
      print(len(tupla))

medida(1, 2, 3, 4, 5)"""

#cuando se returna algo, hay que imprimir toda la funcion no solo llamarla, en vez de med() es print(med())
def med(*tuplaaa):
    return len(tuplaaa)
print(med(1, 2, 3, 4, 5))
