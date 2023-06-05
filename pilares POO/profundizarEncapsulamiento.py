class A():
    #esto es un atributo
    #ahora ya no se puede usar __ bueno si pero es mejor solo usar un _
    def __init__(self):
        self._contador = 0

    def incrementar(self):
        self._contador += 1

    def cuenta(self):
        return self._contador

a = A()
#esto no lo debemos de hacer ya que las variables que llevan _ no se puede cambianr ni llamar de este modo 
print(a.cuenta)
a.cuenta = 20
print(a.cuenta)