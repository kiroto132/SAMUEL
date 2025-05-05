#pedir al ususario que ingrese un numero
numero = int(input("ingrese un numero:\n"))
#mostrar los numeros que son divisores del numero ingresado
print(f"Los divisores de {numero}, excepto el propio número, son:")
for i in range(1, numero):
    if numero % i == 0:
        print(i)
