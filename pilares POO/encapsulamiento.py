class A():
    def __init__(self):
        self.contador = 0
    def incrementar(self):
        self.contador += 1
    def cuenta(self):
        return self.contador
    
#le podemos agregar __ guiones para llamarlos y lo encapsulamos y volvemos privada una variable o parametro
class B():
    def __init__(self):
        self.__contador = 0
    def incrementar(self):
        self.__contador += 1
    def cuenta(self):
        return self.contador
    
a = A()

print(a.cuenta())
a.incrementar()
print(a.cuenta())
print(a.contador)
print('\n')

b = B()
print(b.cuenta())
b.incrementar()
print(b.cuenta())

print(b.__contador)