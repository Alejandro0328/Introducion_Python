# for l1 in range (2,1001):
#     if l1 == 2 or l1 == 3 or l1 ==5 or l1== 7:
#         print(l1)
#     elif l1 % 2 != 0 and l1 % 3 != 0 and l1 % 5 !=0 and l1 % 7 != 0:
#         print (l1)
def construir_cadena(max):
    cad = ""
    for i in range(2, max+1):
        cad += f"{i},"
    return cad.rstrip(",")

def quitar_cadena(str, num):
    cad = ""
    for n in str.split(","):
        if n != num:
            if int(n) % int(num) != 0:
                cad += f"{n},"
        else:
            cad += f"{n},"

    return cad.rstrip(",")



MAX = 1000
str = construir_cadena(MAX)
for snum in str.split(","):
    new_str= quitar_cadena(str, snum)
    if len(new_str) == len(str): 
        break # pare si no hay cambios
    str = new_str

print(str)