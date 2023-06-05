def areaCuadrado(base, altura):
    return base * altura

print(areaCuadrado(10, 10))

# los ** es para elevar al cuadrado o el numero que quieras
#podemos usar pow para elevar pow(radio, 2)
def areaCirculo(radio):
    area = (radio **2) * 3.14
    print(area)

areaCirculo(10)