def entero():
    print('Este es un Dato entero')
    return 10

def decimal():
    print('Este es un Dato Decimal')
    return 90.99

def frase():
    return 'Mi Nombre es, Jorge Gonzalez'

def asignacion():
    return 1, 2, 3, 4, 5

print(entero())
print('\n')
print(decimal())
print('\n')
print(frase())
print('\n')
print(asignacion())
print('\n')

#aqui le asignamos un valor a los caracteres de return de asignacion a vale 1, b vale 2 y asi hasta llegar a 5
a, b, c, d, e = asignacion()

print(a)
print(b)
print(c)
print(d)
print(e)

