#cuando le asignamos un * se convierte en Tupla
def argumento(*num):
    for i in num:
        print(i)
    """return type(num)"""
#aqui le podemos asignar caracteres, datos tipo entero u flotante
print(argumento(10, 20, 30, 40, 50))