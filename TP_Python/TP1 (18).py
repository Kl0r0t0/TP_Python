def inversor_de_listas():
    """El programa recibe una lista y la devuelve invertida"""
    texto = input("Ingrese una frase ")
    lista = texto.split(" ")
    #El programa muestra la lista en reversa
    print (list(reversed(lista)))
inversor_de_listas()