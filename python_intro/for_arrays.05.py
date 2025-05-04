lista = [12, 23, 23, 34, 45, 56]
print(lista)
num = int(input("Ingrese un numero:\n"))
conta = 0
for i in lista:
    if i == num:
        conta += 1
if conta > 0:
    print(f"El numero {num} se repite {conta} veces")
else:
    print(f"El numero {num} no se repite en la lista")
        