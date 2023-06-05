class Marino():
    #aqui le agregamos e indicamos que hablar tiene predeterminado Hola
    #luego en Pulpo, lo modificamos
    def hablar(self):
        print('Hola')

class Pulpo(Marino):
    #aqui en pulpo, indicamos que hablar le declaramos como Soy un Pulpo y hablar se Hereda de Marino
    def hablar(self):
        print('Soy un Pulpo')

class Foca(Marino):
    #aqui indicamos que el usuario ingresara el mensaje como parametro, esto se puede revisar en la lina 26 para abajo
    #indicamos como parametro mensaje, luego indicamos que self.mensaje es = a mensaje para retornarlo 
    def hablar(self, mensaje):
        self.mensaje = mensaje
        print(self.mensaje)

marino = Marino()
marino.hablar()

pulpo = Pulpo()
pulpo.hablar()

foca = Foca()
foca.hablar('Hola, soy una Foca')