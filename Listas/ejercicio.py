lista = ['Jorge', 'Gonzalez', 23, 'Python', 'JavaScript']
print('Hola, esto es una lista')
print(lista)
print('¿Quieres editar la lista?')


nombre = input('Ingresa tu nombre: ')
apellido = input('Ingresa tu Apellido: ')

print(lista)

lista[0] = nombre
lista[1] = apellido

print(lista)