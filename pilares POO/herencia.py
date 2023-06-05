#que una propiedad de una clase, se herede de otra

class animales():
    def habla(self):
        print('Yo soy un Animal')

    def descripcion(self):
        print('Yo soy una {}'.format(self.animal))

class Perro(animales):
    pass

class Abeja(animales):
    def __init__(self, animal):
        self.animal = animal



animal = animales()
animal.habla()

perro = Perro()
perro.habla()

abeja = Abeja('Abeja')
abeja.descripcion()