frase = input("Ingresa una frase de al menos 50 caracteres: ")


while len(frase) < 50:
    print(f"Faltan caracteres. Llevas {len(frase)} de 50.")
    frase = input("Por favor, ingresa una frase más larga: ")

cantidad_a = 0

for letra in frase:
    if letra.lower() == "a":
        cantidad_a = cantidad_a + 1

print(f"La letra 'a' se repite {cantidad_a} veces en tu frase.")
