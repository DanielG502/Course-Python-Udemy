class FabricaTelefonos():
    #si ponemos un * lo reconoce como Tupla si ponemos ** lo reconoce como diccionario
    #la tupla se ingresa luego del primer parametro
    #para ingresar un diccionario, hay que hacerlo de esta forma M1 = J7, m2 = Iphone11
    def __init__(self, marca, *colores, **modelos):
        self.modelos = modelos
        self.marca = marca
        self.colores = colores

telefono = FabricaTelefonos('Alcatel', 'Negro', 'Azul', 'Rojo', 'Morado', m1 = 'Samsumg J7', m2 = 'Iphone 11')
print(telefono.marca)
print(telefono.colores)
print(telefono.modelos)
telefono.memoria = 512
#agregamos un nuevo dato a la asignacion
print(telefono.memoria)