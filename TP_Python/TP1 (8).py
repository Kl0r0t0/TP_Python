def enteros_a_romanos(entero):
    """El programa convierte numeros a numeros romanos"""
    #El programa tien 2 listas, una para los numeros del 1 al 1000
    numeros = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    numerales = ['M', 'CM','D', 'CD', 'C', 'XC', 'L', 'XL', 'X' ,'IX', 'V', 'IV', 'I']

    numeral = ''
    i = 0
    #El programa asigna a numerla su valor correspondiente en su lsita de numerals
    #El programa asigna a entero su valor correspodniente en la lista numeros
    while entero > 0:
        for _ in range (entero // numeros[i]):
            numeral += numerales[i] 
            entero -= numeros[i]
        #Mientras el ciclo while se mantenga a i se le suma 1     
        i += 1
    return numeral

print(enteros_a_romanos(3)) 