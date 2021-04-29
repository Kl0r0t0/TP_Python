cad=input("Cadena:")				
"""El programa devuelve, la primera letra de cada palabra, en mayusculas, y en un grupo aparte las palabras que empiezan con A"""
# La primera letra de cada palabra. Por ejemplo, si recibe Universal Serial Bus debe devolver USB.
lista=cad.split(" ")
for palabra in lista:
    print (palabra[0],end="")
print()
# Dicha cadena con la primera letra de cada palabra en mayúsculas. Por ejemplo, si recibe república argentina debe devolver República Argentina.
for palabra in lista:
    print (palabra.capitalize(),end=" ")
print()			
# Las palabras que comiencen con la letra A. Por ejemplo, si recibe Antes de ayer debe devolver Antes ayer.
for palabra in lista:
    if palabra.startswith("a") or palabra.startswith("A"):
        print (palabra,end=",")
print()