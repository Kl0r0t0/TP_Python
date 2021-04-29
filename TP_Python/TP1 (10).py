import random
def numero_aleatorio ():
    """El programa genera un numero aleatorio entre 1 y 10 y el usuario debe adivinarlo"""
    print ("Hola usuario, estoy pensando en un numero entre 1 y 10")
    numero = random.randrange (1,11)
    intento = int(input("ingrese un nuemero usuario: "))
    #El programa crea un buclea que compara la respuesta con el numero aleatorio, si la respuesta es correcta el bucle termina, si no lo es se repite hasta ingresar el numero correcto
    while intento != numero:
        if intento < numero:
           intento = int (input ("El numero ingresado es menor que el numero a adivinar, intente nuevamente: "))
        if intento > numero: 
           intento = int (input ("El numero ingresado es mayor que el numero a adivinar, intente nuevamente: "))
        if intento == numero:
            break
    print ("¡Ganaste!")

numero_aleatorio()