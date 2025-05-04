lista = [1, 2, 3, 4, 5]

listv = []

for i in range(len(lista)-1,-1,-1):
    listv.append(lista[i])


print(f"La lista normal es: {lista}")
print(f"La lista invertida es: {listv}")