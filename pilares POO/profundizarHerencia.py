class Animales():
    def __init__(self, nombre):
            self._nombre = nombre

class Perro(Animales):
    def __init__(self, nombre, sonido):
        #que es super()?
        super().__init__(nombre)
        self._sonido = sonido

perro = Perro('Firulais', 'Woof!')
print(perro._nombre)