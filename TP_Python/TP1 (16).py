texto = input("Ingrese un texto ")
"""El programa elimina las vocales de un texto"""
def consonantes(texto):
    vocales = "aeiouAEIOU"
    #El programa busca las vocales, registradas en la varialbe "vocales", en el texto y las borra reemplzandolas por ""
    for letra in vocales:
        texto = texto.replace(letra,"") 
    print ("el texto solo tiene las siguientes letras consonantes: " , texto)

consonantes(texto)
