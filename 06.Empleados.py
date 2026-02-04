

def calcular_mayor(lista_sueldos):
    if len(lista_sueldos) > 0:
        el_mayor = max(lista_sueldos)
        print(f"El sueldo mayor de los {len(lista_sueldos)} ingresados es: {el_mayor}")
    else:
        print("No se ingresaron sueldos.")

def capturar_sueldos():
    lista_temporal = []
    print("Ingresa los sueldos (escribe '0' o un número negativo para terminar):")
    while True:
        try:
            n = float(input("Sueldo: "))
            if n > 0:
                lista_temporal.append(n)
            else:
                break
        except ValueError:
            print("Por favor, ingresa un número válido.")
    return lista_temporal

def main():

    mis_sueldos = capturar_sueldos()


    calcular_mayor(mis_sueldos)

main()



#ERRORES

# def mayor(sueldos):
#     if sueldos[0] > sueldos[1] and sueldos[0] > sueldos[2]:
#         print("El sueldo mayor es:", sueldos[0])
#     elif sueldos[1] > sueldos[0] and sueldos[1] > sueldos[2]:
#         print("El sueldo mayor es:", sueldos[1])
#     else:
#         print("El sueldo mayor es:", sueldos[2])

# # while True:
# #     for i in range -------- COMPLETAMETNE INNESESARIO

# def sueldos():
#     while True:
#         n =float(input(f"Ingresa el sueldo"))
#         if n > 0:
#             return n
#         elif n <= 0:
#             break

# def main():
#     sueldos()
#     sueldo = [n]