numero = int(input('elige un numero:\n'))


if numero %3==0 and numero %5==0:
    print('FizzBuzz')
elif numero %3==0:
    print('fizz')
elif numero %5==0:
    print('buzz')

else:
    print(f'el {numero} no es multiplo de ninguno')
    