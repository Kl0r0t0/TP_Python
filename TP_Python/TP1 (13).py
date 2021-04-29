def compradaor_de_palabras():
    """El programa verifica si una palabra es la version capitalizada de la otra"""
    palabra1 = input("Ingrese una palabra ") 
    palabra2 = input ("ingrese la misma palabra (peude estar capitalizada o no) ")

    #El programa capitaliza la primera palabra y la compara con la segunda, si son iguales, y muestra el mensaje correspondiente
    if palabra1.upper() == palabra2:
        print ("La palabra 2 es la version capitalizada de la palabra 1")
    else:
        print ("La palabra 2 no es la version capitalizada de la palabra 1")
compradaor_de_palabras()
