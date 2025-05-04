oracion = input("Escribe una oracion:\n")

palabras = oracion.split()

cond = 0

palabraslar = []
for i in palabras:
    if len(i) > 5:
        cond += 1   
        palabraslar.append(i)

print(f"la oracion tiene {cond} palabras con mas de 5 letras")
print(f"Las palabras con más de 5 letras son:", ", ".join(palabraslar))