capital=(int(input("ingrese el capital: $ ")))
I =(int(input("Ingrese el interes anualde 1 a 100%: ")))/100
m = (int(input("Ingrese lso años: ")))
for s in range(1, m+1):
    interes = capital* I
    capital= capital + interes
    print(f"año {s} el capitals es ${capital:,.2f}")