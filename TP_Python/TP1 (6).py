numero_valido = False
"""El programa devuelve el mayor producot entre 2 numeros"""
#El programa verifica que el valor ingresado por el usuario sea un valor valido
while (numero_valido == False):
    numero_1 = input ("Ingrese un numero: ") 
    try: 
        numero_1 = float (numero_1)
        numero_valido = True
    except ValueError:
        print ("El valor ingresado no es un valor valido, ingrese un valor valido ")
numero_valido = False
while (numero_valido == False):
    numero_2 = input ("Ingrese un numero: ") 
    try: 
        numero_2 = float (numero_2)
        numero_valido = True
    except ValueError:
        print ("El valor ingresado no es un valor valido, ingrese un valor valido ")
numero_valido = False
while (numero_valido == False):
    numero_3 = input ("Ingrese un numero: ") 
    try: 
        numero_3 = float (numero_3)
        numero_valido = True
    except ValueError:
        print ("El valor ingresado no es un valor valido, ingrese un valor valido ")
numero_valido = False
while (numero_valido == False):

    numero_4 = input ("Ingrese el ultimo nuemro: ") 
    try: 
        numero_4 = float (numero_4)
        numero_valido = True
    except ValueError:
        print ("El valor ingresado no es un valor valido, ingrese un valor valido ")
producto_A = numero_1 * numero_2
producto_B = numero_1 * numero_3
producto_C = numero_1 * numero_4
producto_D = numero_2 * numero_3
producto_E = numero_2 * numero_4
producto_F = numero_3 * numero_4
#El programa selecciona el numero de mayor valor y lo muestra al usuario
print (max(producto_A , producto_B , producto_C , producto_D , producto_E , producto_F))
