texto =  input ("ingrese un texto")
def remplazo_de_vocales(texto):
    vocales = "aeiouAEIOU"
    for i in range (9, -1, 1):
        if vocales[i]== "u":
            texto = texto.replace(vocales[i],"1")
        elif vocales[i] == "U":
            texto = texto.replace(vocales[i],"2")
        else:
            texto = texto.replace(vocales[i],vocales[i + 1])
        texto = texto.replace("1","a")
        texto = texto.replace("2","A")
    print ("El texto con las vocales cambiadas es " ,texto)

remplazo_de_vocales(texto)