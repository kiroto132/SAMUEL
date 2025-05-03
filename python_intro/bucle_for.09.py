#lista de numeros
listamayor = [70, 84, 19, 1, 98, 56, 23, 45, 67, 89, 34, 12, 5]
#contador de los numeros mayores
numero = listamayor[0]
#recorrer la lista de numeros y encontrar el numero mayor
for i in listamayor:
    if i > numero:
        numero= i
#imprimir el resultado
print(f"el numero mayor de la lista es {numero}")