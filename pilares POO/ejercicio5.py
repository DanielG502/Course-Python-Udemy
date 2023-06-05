class Universidad():
    #aqui podemos englobalizar variables :D como         self.nombre = nombre para usarlo en otra clase
    def __init__(self, Nombre):
        self.Nombre = Nombre

class Carrera():
    def carrera(self, especialidad):
        self.especialidad = especialidad

class Estudiante(Universidad, Carrera):
    def datos(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        print('Mi nombre es, {}, tengo {}, años, Mi especialidad es, {}, estudio en la Universidad, {}'.format(self.nombre, self.edad, self.especialidad, self.Nombre))
print('\n')
persona = Estudiante('UMG')
persona.carrera('Ingenieria en Sistemas')
persona.datos('Jorge Gonzalez', 23)

#esto es polimorfismo