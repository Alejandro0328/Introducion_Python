def mayor(sueldos):
    if sueldos[0] > sueldos[1] and sueldos[0] > sueldos[2]:
        print("El sueldo mayor es:", sueldos[0])
    elif sueldos[1] > sueldos[0] and sueldos[1] > sueldos[2]:
        print("El sueldo mayor es:", sueldos[1])
    else:
        print("El sueldo mayor es:", sueldos[2])
def main():
    sueldos=[]
    n1=float(input("Ingrese Sueldo 1: "))
    n2=float(input("Ingrese Sueldo 2: "))
    n3=float(input("Ingrese Sueldo 3: "))
    sueldos=[n1,n2,n3]
    mayor(sueldos)
main()

# while True:
#     for i in range