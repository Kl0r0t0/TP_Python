def programa_contraeña():
    """El porgrama impide que el usuario continua a no ser que ingrese la contraseña correcta"""
    contraseña = "seguridad"
    verificador = input("Ingrese la contraseña usuario: ")
    #El programa compara la contraseña ingresada con la respuesta correcta y si la respuesta no es la correcta, el usuario debe ingresar la contraseña nuevamnete
    while contraseña != verificador:
        verificador = input("La contraseña no es valida, por favor, intete nuevamente: ")
    
    return verificador
    

verificador = programa_contraeña()
print ("La contraseña es la correcta")