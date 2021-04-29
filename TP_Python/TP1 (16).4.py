def detectar_palindromo():
    "El programa verifica si la frase ingresade es o no un palindromo"
    texto = input ("ingrese una palabra ")
    #El programa borra los espacios
    texto = texto.replace(" ", "")
    #El programa compara el texto original con el invertido, y muestra el mensaje correspondiente
    if str(texto) == str(texto)[::-1]:
        print ("Es palindromo")
    else:
        print ("No es palindromo")

detectar_palindromo()
