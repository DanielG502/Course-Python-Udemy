#mi solucion
"""
class Estudiante():
    def __init__(self):
        while True:
            try:
                nota = random.randint(0, 10)
                if nota > 5:
                    print('La nota del usuario es {}, aprobo el curso '.format(nota))
            except: ValueError
            print('Error de Sintaxis')
            break


print(Estudiante())
"""
#solucion del Curso
import random

class Estudiante():
    #init para iniciar
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def Imprimir(self):
        print('Nombre: {} \n Nota: {} \n'.format(self.nombre, self.nota))

    def Contador(self):
        if self.nota <= 5:
            print('La Nota es, {}, has Reprobado'.format(self.nota))
        else:
            print('La Nota es, {}, Has Aprobado'.format(self.nota))

estudiante1 = Estudiante('Jorge', 10)
estudiante1.Imprimir()
estudiante1.Contador()

estudiante2 = Estudiante('Karla', 5)
estudiante2.Imprimir()
estudiante2.Contador()