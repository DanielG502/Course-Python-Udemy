diccionario = {'Nombre' : 'Jorge' , 'Apellido' : "Gonzalez", 'Estatura' : 176}

print(diccionario)

#solicitar solo las claves
print(diccionario.keys())
print(diccionario.values())
#llamar al valor de la clave 
print(diccionario['Estatura'])

#agregar uno nuevo

diccionario['Peso'] = 230

print(diccionario)

#modificar el valor existente

diccionario['Nombre'] = 'Daniel'

print(diccionario)