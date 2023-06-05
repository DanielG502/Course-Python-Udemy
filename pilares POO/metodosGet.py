class A():
    #encapsulamiento
    def __init__(self):
        #estos _ son atributos encapsulados
        self._cuenta = 0
        self._contador = 0
#este es el metodo ideal
#self es metodo de instancia

#@property es para que puedan ser tomados como si fuera GET como si fuera un atributo
    @property
    def cuenta(self):
        return self._cuenta
    #con @property podemos llamar a esta def sin usar el parametro 
    @property
    def contador(self):
        return self._contador
    
a = A()
#forma incorrecta
#print(a._cuenta)

#forma correcta
print(a.cuenta)
print(a.contador)
#esto no se debe de hacer 
#print(a._contador)
#print(a._cuenta)

