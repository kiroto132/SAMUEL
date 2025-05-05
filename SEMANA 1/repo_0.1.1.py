#intercambio de variables 
a = int(input('ingrese un numero:\n'))
b = int(input('ingrese un numero:\n'))

a , b = b, a 

print(f'intercambio1 {a}')
print(f'intercambio {b}')