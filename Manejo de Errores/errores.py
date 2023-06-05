while True:
    try:
        edad = int(input('Ingrese su Edad: '))
        print('Tu edad es: ', edad)
        break
    except:
        print('Ingresaste un Valor Erroneo')
    finally:
        print('La ejecucion ha Finalizado')

#try y except, es para retornar un error mas legible 
#finally para controlar mas los errores 
#con While True, empezamos un bucle hasta que declares el Break