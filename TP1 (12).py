def contar_vocales(frase):
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    

    for letra in frase:
         if letra.lower() in "a":
            a += 1
         if letra.lower() in "e":
            e += 1
         if letra.lower() in "i":
            i += 1
         if letra.lower() in "o":
            o += 1
         if letra.lower() in "u":
            u += 1
    return a, e, i, o, u
palabra_vocales = str(input("Introduzca una palabra: "))
print(contar_vocales(palabra_vocales))
print("(a- e- i-o- u)")

