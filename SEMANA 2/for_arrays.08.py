lsita = [25, 50, 75, 86, 29, 87, 45, 12, 36, 99]

suma = 0

sumn = []
for i in range(1, len(lsita), 2):
    suma += lsita[i]
    sumn.append(suma)
print(f"La lista normal es: {lsita}")
print(f"La lista de los elementos sumados son: {sumn}")
print(f"la suma completa de los elementos es: {suma}")
