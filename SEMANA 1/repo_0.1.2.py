numero = int(input('ingrese el numero de 3 cifras: \n'))
def invertir_tres_cifras(n):
    centenas = n // 100
    decenas = (n // 10) %10
    unidades = n % 10
    return unidades * 100 + decenas * 10 + centenas

print(invertir_tres_cifras(numero)) 