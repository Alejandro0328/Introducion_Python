x= int(input("Ingrese X : "))
n= int(input("Ingrese N : "))

def factorial(num):
    fact=1
    for n in range (2,num+ 1):
       fact *= n
    return fact

for s in range(n+1):
    e= 0
    e += (x**s) / factorial(s)


print(e)
