def farenheit_celsius():   
    """Convierte fahrenheit en celsius"""
    #El programa iguala la temperatura introducida a la mismatemperatura, en la ecuacion de pasage de fahrenheit a celsius
    temperatura = input ("ingrese el valor de la temperatura que desea convertir: ")
    temperatura = float(temperatura)
    temperatura = (temperatura - 32) * (5/9)
    return temperatura
print ("la temperatura en celsius es " + str (farenheit_celsius())) 