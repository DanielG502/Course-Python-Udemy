practica1 = float(input("Ingrese el Valor de la Practica 1: "))
practica2 = float(input("Ingrese el valor de la Practica 2: "))
practica3 = float(input("Ingrese el valor de la Practica 3: "))
Parcial = float(input("Ingrese el valor del Examen Parcial: "))
examenFinal = float(input("Ingrese el valor del Examen Final: "))

promedioPracica = (practica1 + practica2 + practica3) /3
promedioFinal = (promedioPracica + 2*Parcial + 3*examenFinal) / 6

print("El Promedio final del estudiante es de:\n ", promedioPracica, "\n El promedio final es de: \n", promedioFinal)