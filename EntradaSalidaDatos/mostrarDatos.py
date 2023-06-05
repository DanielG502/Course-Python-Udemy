nombre = input("Ingresa tu Nombre: ")
edad = int(input("Ingresa tu Edad: "))

#para concatenar se puede usar la , o la +
print("Hola", nombre, "tu edad es: ", edad)
#otra forma de imprimir

print("Hola {} tu edad es: {}".format(nombre, edad))
#Los {} sustituyen la concatenacion