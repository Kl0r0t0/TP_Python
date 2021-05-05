import math
print ("Bienvenido al programa de calculo de area de circulos")
valores = False    
while not valores:
    radio = input("Ingrese el radio de su circulo ")
    try:
        radio = float(radio)      
        if radio < 0:
            print ("El valor del radio ingresado es un numero negativo, por favor, introduzca un numero valido ") 
        else:
            valores = True 
    except:  
        print ("Uno o mas datos no son validos, solo se aceptan valores mayores a 0, porfavor, introduzca los datos nuevamente")
print ("El area de su circulo es ", ( math.pi * (float(radio) ** 2)))