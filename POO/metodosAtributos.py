class fabricaTelefonos():
    marca = "Samsumg"
    Color = "Azul"
    MRam = 32
    almacenamiento = 128

#self pendiente
    def llamar(self , mensaje):
        return mensaje
    
    def escucharMusica(self):
        print('Estas Escuchando Musica')
#metodos: son objetos que pueden realizar

telefono = fabricaTelefonos()
telefono.marca
telefono.Color
telefono.MRam
telefono.almacenamiento

print(telefono.marca)
print(telefono.Color)
print(telefono.MRam)
print(telefono.almacenamiento)


print(telefono.llamar('Hola, con quien hablo?'))
telefono.escucharMusica()