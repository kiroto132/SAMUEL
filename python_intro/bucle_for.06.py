#lista de numeros pasitivos y negativos
lista = [4, -3, -4, -5, -6, 7]
#conteo de los numeros negativos
negativos = 0
#recorrer la lista y sumar los negativos
for i in lista:
    if i < 0:
        negativos += i
#imprimir el resultado
print(f"la suma de los negativos es {negativos}")