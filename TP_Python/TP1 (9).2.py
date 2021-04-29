import time
def programa_contraeña():
    """El porgrama impide que el usuario continua a no ser que ingrese la contraseña correcta, ademas, el usuario tiene 3 intentos para ingresar la contraseña correctamnete, cada vez que el usuario falla en ingresar la contraseña hay un tiempo de espera"""
    intentos = 3
    espera = 4
    contraseña = "seguridad"
    verificador = input("Ingrese la contraseña, usuario: ")
    #El programa compara la contraseña ingresada con la respuesta correcta y si la respuesta no es la correcta, el usuario debe ingresar la contraseña nuevamnete
    #El programa tiene un contador de intentos que empieza en 0, por cada vez que el usuario falla en ingresar la contraseña, el ciclo while se repite, por lo que el valor del numero de intntos aumenta
    #Si el numero de intentos es igual a 3 el programa termina, sin dejar que el usuario continue
    #El programa utiliza la funcion sleep para generear un tiempo de espera el cual aumenta con cada paso del bucle while
    while contraseña != verificador:
        time.sleep (espera)
        espera += 1
        verificador = input("La contraseña no es valida, por favor, intete nuevamente: ")
        intentos = intentos - 1
        if (intentos == 0):
            print("limite de intentos alncanzado")
            break
        else:
            if (verificador == contraseña):
                print ("La contraseña ingresada es correcta")
    return verificador
    



verificador = programa_contraeña()
print ("La contraseña es la correcta")