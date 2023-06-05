class FabricaTelefonos():
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color
        print('El Objeto {}, ha sido construido'.format(self.marca))

    def __str__(self):
        return 'El Objeto es {}'.format(self.marca)
#destructor es con __del__(self):
    def __del__(self):
        print('El Objeto {}, ha sido destruido'.format(self.marca))
telefono = FabricaTelefonos('Nokia', 'Negro')
print(telefono.marca)
print(telefono)

"""
def __str__(self):
        return 'El Objeto es {}'.format(self.marca)

#con este def podemos imprimir el error 
"""