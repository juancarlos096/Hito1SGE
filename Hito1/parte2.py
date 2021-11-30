#Cifrar

texto = input("Tu texto: ")
abc="ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz0123456789"
k = int(input("Valor de desplazamiento: "))
cifrado = ""
for c in texto:
    if c in abc:
        cifrado += abc[(abc.index(c)+k)%len(abc)]
    else:
        cifrado += c
print("Texto cifrado: ",cifrado)

#Descifrar
texto = input("Descifrar: ")
letras="ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz0123456789"
for key in range(len(letras)):
    traduccion=""
    for elem in texto:
        if elem in letras:
            elemIndex = letras.find(elem)
            tradIndex = elemIndex - key
            if tradIndex<0:
                tradIndex = tradIndex + len(letras)
            traduccion = traduccion + letras[tradIndex]
        else:
            traduccion = traduccion + elem
        print("key #%s: %s" % (key, traduccion))