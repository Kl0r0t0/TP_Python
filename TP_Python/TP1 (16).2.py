texto = input("Ingrese un texto ")
"""El programa elimina las consonantes de un texto"""
def vocal(texto):
    consonantes = "BCDFGHJKLMNÑPQRSTVWXYZbcdfghjklmnñpqrstvwxyz"
    #El programa busca las consonantes, registradas en "consonantes", en el texto y las reemplaza por ""
    for letra in consonantes:
        texto = texto.replace(letra, "")
    print ("El texto solo tiene las siguientes letras vocales: " ,texto)
vocal(texto)
