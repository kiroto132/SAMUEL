edad = int(input('ingrese su edad por favor: \n'))
if edad >= 18 and edad <= 25:
    pase = input('¿tienes pase dorado?: \n')
    if edad >= 18 and edad <= 25 and pase=='si':
        print('puedes entrar al club')
    elif edad >= 18 and edad >= 25 and pase=='si/no':
        print('entras al club que eres mayor de edad')
else:
    print('No puedes entrar al club, tines que ser mayor')
