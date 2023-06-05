"""lista = {"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}
print('\n')
print("Hola, en esta Lista, puedes elegir las capitales de estos Paises")
print('Puedes escribir cualquier de estos paises para que puedas saber cual es su capital:')
print('Guatemala,', 'El Salvador,', 'Honduras,', 'Nicaragua,', 'Costa Rica,', 'Panama,', 'Argentina,', 'Colombia,', 'Venezuela,', 'España')

respuesta = input('Ingrese el Pais que quieres ver su Capital: ')


if respuesta == 'Guatemala':
    print('La capital es: ', lista["Guatemala"])
elif respuesta == 'El Salvador':
    print('La capital es: ', lista['El Salvador'])
elif respuesta == 'Honduras':
    print('La capital es: ', lista["Nicaragua"])
elif respuesta == 'Costa Rica':
    print['La capital es: ', 'Costa Rica']
elif respuesta == 'Panama':
    print('La capital es: ', lista['Panama'])
elif respuesta == 'Argentina':
    print('La capital es: ', lista['Argentina'])
elif respuesta == 'Colombia':
    print('La capital es: ', lista['Colombia'])
elif respuesta == 'Venezuela':
    print('La capital es: ', lista['Venezuela'])
elif respuesta == 'España':
    print('La capital es: ', lista['España'])
else:
    print('El resultado que buscas, no esta disponible')"""

#no es lista, este es un Diccionario

#Otro Ejemplo

#En el siguiente diccionario se encuentran capitales de los paises en el mundo, debes realizar un programa que pida un pais al usuario, y muestre la capital de ese pais, en dado caso el pais no este en el diccionario, se debe mostrar un mensaje diciendo que ese pais no se encuentra.

#{"Guatemala": "Ciudad de Guatemala", "Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}

diccionario = {"Guatemala": "Ciudad de Guatemala", "Honduras": "Tegucigalpa","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid" , "El Salvador" : "San Salvador"}

pais = input('Ingrese un pais para conocer su capital: ')
letra = pais.title() in diccionario

if letra:
    print(diccionario[pais.title()])
else:
    print("El pais no se encuentra en el diccionario")

    #pendiente