class A():
    def primero(self):
        return 'Esta es la Clase A'
    
class B():
    def segunda(self):
        return 'Esta es la Clase B'

#aqui hacemos herencia multiple agregando como parametro A B
class C(A, B):
    def tercera(self):
        pass

c = C()
print(c.primero())
print(c.segunda())
