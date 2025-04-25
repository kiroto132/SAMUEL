nombre = input('¿Que comida comiste?: \n')
print(nombre)
#Valor de la comida 
comida = int(input('¿Cual es el valor de la comida?: \n'))
#Opcional
print('¿quieres dar propina?')
pro = input('')
#identificaciòn
if pro == 'si':
    propina  = ('las opciones son 0.10%, 0.15% y 0.20%: ')
    print(propina)
opr = float(input('¿Que porciento quieres escoger para la propina?: \n'))
totalV = 0.10 * comida
totalV2 = 0.15 * comida
totalV3 = 0.20 * comida
#Resultados
if opr == 0.10:
        print(f'El valor total es: {totalV}')    
        if opr == 0.15:
            print(f'El valor total es: {totalV2}')
        if opr == 0.20:
            print(f'El valor total es: {totalV3}')
        else:
            print('¡Gracias por dejar propina!')
#Opcional
elif pro == 'no':
    print('Deja de ser tacaño y deja una propina')
#Error
else:
    print('error valor no valido')

print(f'El total a pagar del 10% es: {totalV}')
print(f'El total a pagar del 15% es: {totalV2}')
print(f'El total a pagar del 20% es: {totalV3}')
