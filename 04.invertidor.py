n= int(input("ingrese el Número a invertir: "))
resultado=0
while n > 0:
    n_1 = n % 10
    n = n //10
    resultado=resultado* 10 + n_1
print(resultado)
