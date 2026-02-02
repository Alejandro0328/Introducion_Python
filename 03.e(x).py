def factorial(num):
    fact=1
    for n in range (2,num+ 1):
       fact *= n
    return fact







x= int(input("Ingrese X : "))
n= int(input("Ingrese N : "))
e = 1+ x + x**2 /factorial(2) + x **3/factorial(3)
