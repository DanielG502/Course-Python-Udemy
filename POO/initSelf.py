"""class FabricaTelefonos():
    marca = 'Samsumg'

#self nos permite englobalizar un atributo a toda una clase 
    def ElaborarHuawei(self):
        self.marca = 'Huawei'

telefono = FabricaTelefonos()
telefono.ElaborarHuawei()
print(telefono.marca)"""

class FabricaTelefonos():
    # init es lo primero que se ejecuta en el objeto 
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color
        print('Estoy ejecutando el metodo Init, por que se ha creado un nuevo objeto')

telefono = FabricaTelefonos('Huawei', 'Azul')
print(telefono.marca)
print(telefono.color)