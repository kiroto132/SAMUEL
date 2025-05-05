#pedir al usuario que ingrese un numero
numero = int(input("ingrese un numero:\n"))
#verificar si el numero es primo
primo = True
#verificar si el numero es primo
if numero <= 1:
    primo = False
else:
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            primo = False
            break
#imprimir el resultado
if primo:
    print(f"el numero {numero} es primo")
else:
    print(f"el numero {numero} no es primo")