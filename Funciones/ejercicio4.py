
"""multi = iva * retencion / 100

print(multi)
"""



def calcularIVA():
    cant = int(input('Ingrese la Cantidad para descontar el IVA: '))
    multi = 21
    if 0 != cant:
        totl = ((cant * multi) / 100)
        tot2 = ((cant * multi) / 100) + cant
        return ('El IVA de la cantidad de {}, es: {}, el total es {}'.format(cant, totl, tot2))
    else:
        print('Datos Incorrectos')

print(calcularIVA())
#calcularIVA()
#print('La Retencion del IVA de la cantidad {}, es el {}'.format(iva , retencion))



"""


def calcularIVA():
    cantidad = int(input('Ingrese la Cantidad para descontar el IVA: '))
    iva = int(input('Ingresa la cantidad de IVA que quieres descontar: '))
    if iva != 0:
        if iva > 0:
            total = ((cantidad * iva) / 100)
            return total
        else:
            return('El monto es negativo, no podemos avanzar')
    else:
        total = (cantidad * 0.21) + cantidad
        return total

print(calcularIVA())"""