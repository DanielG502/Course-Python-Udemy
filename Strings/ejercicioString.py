cadena = 'Te quiero solo como amigo'

print(cadena[0:2], cadena[-3:])

cadena2 = 'recta'

print(cadena2[0:1],cadena2[2:-2],cadena2[-1:])

cadena3 = 'Hola Mundo!'

print(cadena3[::-1])
#para invertir una cadena, puedes hacer lo siguiente [::-1] se coloca :: 2 veces 2 puntos para que lo tome como una impresion a la inversa 

#reverse() es para imprimir y que nos retorne las palabras separadas con '' 
#, e ingresadas con [], Ejemplo de Hola Mundo ['Hola', 'Mundo']


cadena4 = 'reflejo'


print(cadena4,cadena4[::-1])
#otro ejemplo de imprimir a la inversa
print(cadena4 + cadena4[::-1])

cadena5 = 'separar'
cadena5 = list(cadena5)
print(cadena5)
#para poner la frase dividina por ,  es necesario que luego de declararla se realice tipo lista 

#uso del metodo de replace es para tomar un caracter de una cadena de texto y asi puedas modificarlo, por ejemplo si tienes una cadena como esta Hola Mundo, podemos seleccionar la letra o y pasarla a Mayuscula con este metodo
#ejemplo
# print(cadena3)
#creamos una variable para pasarle el parametro .replace()
# reemplazar = cadena.replace("o", "O") con esto, pasamos las letras de minusculas y viseversa
# print(reemplazar)

#otro metodo para imprimir separado con comas

palabra = "Separado"
print(palabra)

reemplazo = palabra.replace("" , ",")
print(reemplazo)

#esta mejor el metodo de List