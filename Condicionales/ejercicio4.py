print("\n")
print("Hola, bienvenido al programa de votaciones")
print("Tenemos 3 candidatos para la eleccion de hoy")
print("\n")
print("Opcion A por el Partido Rojo")
print("Opcion B por el Partido Verde")
print("Opcion C por el Partido Azul")
print("\n")

voto = input("Ingrese Su Voto: ")

if voto.lower() == "a":
    print("Usted ha votado por el Candidato del Partido Rojo")
elif voto.lower() == "b":
    print("Usted ha votado por el Candidato del Partido Verde")
elif voto.lower() == "c":
    print("Usted ha votado por el Candidato del Partido Azul")
else:
    print("Opcion Incorrecta, vuelve a intentarlo")

#upper() para que la palabra ingresada pase de minuscula a mayuscula o viseversa 
