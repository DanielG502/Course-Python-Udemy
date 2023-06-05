vocal = input("Ingrese una Vocal Minuscula: ")
caracter = input("Ingrese una Letra Mayuscula: ")


"""resultado = vocal + caracter 

print(resultado.swapcase())"""

#otra forma de poder hacer es con el upper() y lower
#upper es para pasar una letra en mayuscula y lower a minuscula


vocal = vocal.upper()
caracter = caracter.lower()

print("La Vocal es: {} \n el Caranter es: {}".format(vocal , caracter))