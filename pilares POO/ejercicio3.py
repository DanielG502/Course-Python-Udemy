#Clase Padre
class Fabrica():
    #aqui le pasamos los parametros que queremos
    def __init__(self, llantas, color, precio):
        #aqui declaramos los parametros
        self.llantas = llantas
        self.color = color
        self.precio = precio

    #clase hija, se le adjunta como parametro padre
class Carro(Fabrica):
    #aqui se le asignan valor a los parametros para que los ingresemos al solicitarlo 
    #en la clase hijo, declaramos que es lo que queremos retornar, para que luego ingresemos el los valores cuando lo solicitemos
    def datos(self):
        print('La Cantidad de Llantas es de: {}'.format(self.llantas))
        print('El Color del carro es de: {}'.format(self.color))
        print('El Precio del carro es de: {}'.format(self.precio))
    
class Moto(Fabrica):
    def datos(self):
        print('La cantidad de Llantas de la Moto es de: {}'.format(self.llantas))
        print('El Color de la Moto es de: {}'.format(self.color))
        print('El Precio de la Moto es de: {}'.format(self.precio))

#aqui le ingresamos como valor en los parametros ya que estan declarados en el padre y les asignamos el valor 
moto = Moto(2, 'Negro', 4000)
moto.datos()

print('\n')

carro = Carro(4, 'Rojo', 15000)
carro.datos()

#estudiar Herencia en Python