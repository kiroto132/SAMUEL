lista =[1, 2, 3, -4, 5]

lsitv = []

for i in lista:
    if i >= 0:
        lsitv.append(i)

print(f"La lista normal es: {lista}")
print(f"La lista sin el numero negativo es: {lsitv}")