frase = input("Ingrese una frase: ")
frase2 = input("Ingrese una frase: ")
"""
resultado1 = frase[-3] == frase2[-3]

if Resultado1:
    print("Las palabras si Riman")
else:
    print("Las palabras no Riman") """

    #len(resultado1) < 3 or len(resultado1) < 3 es para sacar el restulado de las ultimas 3 palabras del string 


if len(frase) < 3 or len(frase2) < 3:
    print("Las palabras no riman por que tienen menos de 3 caracteres")
elif frase[-3] == frase2[-3]:
    print("Las Palabras Riman")
elif frase[-2] == frase2[-2]:
    print("Las palabras riman un poco")
else:
    print("Las Palabras No riman")