print ("Bienvenido al programa de calculo de hipotenusas")
valores = False
while not valores:
    cateto1 = input("Ingrese la longitud del primer cateto ")
    cateto2 = input("Ingrese la longitud del segundo cateto ")
    try:
        cateto1 = float(cateto1)
        cateto2 = float(cateto2)      
        if cateto1 < 0 or cateto2 < 0:
           print ("El numero ingresado es un numero negativo") 
        else:
           valores = True 
    except:  
        print ("Uno o mas datos no son validos, solo se aceptan valores mayores a 0, porfavor, introduzca los datos nuevamente")
print ("El  valor de la hipotenusa es ", (((float(cateto1) ** 2) + (float (cateto2) ** 2 ))))