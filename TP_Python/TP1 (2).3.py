print ("Bienvenido al programa de calculo de area de rectangulos en base a coordenadas")
valores = False
while not valores:
    base1 = input("Ingrese la coordenada X1 de su rectangulo ")
    base2 = input("Ingrese la coordenada X2 de su rectangulo ")
    altura1 = input("Ingrese la coordenada Y1 de su rectangulo ")
    altura2 = input("Ingrese la coordenada Y2 de su rectangulo ")
    try:
        base1 = float(base1)
        base2 = float(base2)
        altura1 = float(altura1)
        altura2 = float(altura2)      
        if base1 < 0 or base2 < 0 or altura1 < 0 or altura2 < 0 or base2 <= base1 or altura2 <= altura1:
            print ("El numero ingresado es un numero negativo o las coordenadas de base y/o altura estan invertidas")             
        else:
           valores = True       
    except:  
        print ("Uno o mas datos no son validos, solo se aceptan valores mayores a 0, porfavor, introduzca los datos nuevamente")
print ("El area de su rectangulo es ", ((((float(base2) - float(base1)) * (float (altura2) - float (altura1))))))