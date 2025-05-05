#nombre del producto
producto = input('ingrese el nombre del producto: \n')
#cantidad del producto
cantidad = int(input('ingrese la cantidad deseada: \n'))
#precio
precio = float(input('precio del producto: \n'))
#descuento
Dsc = float(input('descuento asignado entre 0 y 100: \n'))
valtotal = cantidad * precio
valord = valtotal - Dsc

if 0 <= Dsc <= 100:
    if Dsc <= 0:
        print(f'el producto no tiene descuento: {valtotal}')
    else:
        Descuento = valtotal*(Dsc / 100)
        
        print(f'el valor del descuento es: {Descuento}')
        print(f'el valor total con descuento es: {valord}')
        print(f'el valor total sin descuento es:{valtotal}')
else:
    print('el valor ingresado no es valido, por favor ingrese un valor del 0 al 100')
if cantidad < 0:
    print('cantidad invalida, por favor ingrese un valor mayor')
    if precio < 0:
        print('pecio invalido, por favor ingrese un valor mayor')


print(f'el {producto} cuesta {precio} por unidad.')
print(f'La cantidad de productos es {cantidad} y su valor total es {valtotal} sin descuento')
print(f'La cantidad de productos es {cantidad} y su valor total es {valord} con descuento')
