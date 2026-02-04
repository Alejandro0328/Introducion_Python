import random
numero = random.randint(1,10)
print("Tienes 10 intentos para adivinar el numero que estoy pensando")
print(" Tienes 10 intentos para adivinar el numero random")
for s in range (10):
    adivina = int(input("Ingresa un numero del 1 al 1000:"))
    if adivina == numero:
        print("Adivinaste el numero random")
        print(f"Lo hiciste en {s + 1} intentos")
        break
    elif adivina < numero:
        print("El numero es mayor al que ingresaste")
    elif adivina > numero:
        print("El numero es menor al que ingresaste")


print("Acabaste los 10 intentos. Hasta luego")
print(f"El numero random era {numero}")