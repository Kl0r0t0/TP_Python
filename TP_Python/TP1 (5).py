def farenheit_celsius():    
    """El programa muestra las temperaturas de 0 a 120"""
    #El programa iguala la temperatura a i, luego i pasa a celsius.
    #i cambia su valor de 0 a tods los numeros hasta 120, mostrando todos los resultados
    for i in range(0, 121):
        temperatura = i * 10
        temperaturacelsius = (temperatura - 32) * (5/9)
        print (round (temperaturacelsius, 2))
farenheit_celsius()
    
