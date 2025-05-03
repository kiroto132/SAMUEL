#colocar el dia, la fecha y el año

dia = int(input('ingrese el dia: \n'))
#validación de la fecha 
if dia <= 31:
    mes = int(input('ingrese el mes: \n'))
    if mes <= 12:
        año = int(input('ingrese el año: \n'))
    else:
        print('el mes que ingreso no existe')
else:
    print('el dia ingresado no es valido')
#resultado
diamesaño = (f'{dia}/{mes}/{año}')
añomesdia = (f'{año}-{mes}-{dia}')
print('las fechas son:')
print(diamesaño)
print(añomesdia)

