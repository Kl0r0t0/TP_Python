print ("Bienvenido al programa de calculo de perimetro de rectangulos")
valores = False
while not valores:
    base = input("Ingrese la base de su rectangulo ")
    altura = input("Ingrese la latura de su rectangulo ")
    try:
        base = float(base)
        altura = float(altura)      
        if base < 0 or altura < 0: 
           print ("El numero ingresado es un numero negativo") 
        else:
           valores = True 
    except:  
        print ("Uno o mas datos no son validos, solo se aceptan valores mayores a 0, porfavor, introduzca los datos nuevamente")
print ("El perimetro de su rectangulo es ", (((float(base) + float (altura)) * 2)))