class Calculadora():
    def __init__(self):
        self.num1 = int(input('Ingrese el Primer Numero: '))
        self.num2 = int(input('Ingrese el Segundo Numero: '))
    #esto son metodos
    def Suma(self):
        self.Suma = self.num1 + self.num2
        return 'La Suma da como Resultado: {}'.format(self.Suma)
    
    def Resta(self):
        self.Resta = self.num1 - self.num2
        return 'La Resta da como Resultado: {}'.format(self.Resta)
    
    def Multi(self):
        self.Multi = self.num1 * self.num2
        return 'La Multiplicacion da como Resultado: {}'.format(self.Multi)

    def Division(self):
        #para division entera podemos poner 2 barras //
        self.Division = self.num1 / self.num2
        return 'La Division da como Resultado: {}'.format(self.Division)
    

calcular = Calculadora()
print(calcular.Suma())
print(calcular.Resta())
print(calcular.Multi())
print(calcular.Division())




#podemos estudiar esta clase