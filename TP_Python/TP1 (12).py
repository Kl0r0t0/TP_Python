def contar_vocales(frase):
    vocales = "aeiouAEIOU"
    return set([c for c in frase if c in vocales])

texto = " puse la gucci con un short de nike, puse cadenas 'toy que goteo "
print (contar_vocales(texto))
print (len(contar_vocales(texto)))
