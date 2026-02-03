n =int( input("Ingrese las letras : "))
letras = []
cant = [0]
vocales =["a", " e","i","o","u"]
for i in range(n):
    letra= input (f"Letra{i}: ")
    letras.append (letra)
    for v in range (len(vocales)):
        if vocales[v] == letra:
            cant[v] += 1
            break
for pos in range(len(vocales)):
    print(f"Cantidad de {vocales[pos]}: {cant[pos]}")