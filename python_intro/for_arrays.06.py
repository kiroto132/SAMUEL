lista = [12, 23, 23, 34, 45, 56]

elem = []


for i in lista:
    if i not in elem:
        elem.append(i)

print(f"La lista normal es: {lista}")
print(f"La lista sin los elementos repetidos es: {elem}")