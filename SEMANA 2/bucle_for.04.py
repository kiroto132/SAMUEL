"""
pide al usuario una palbra donde se repitan las letras
"""

#la palabra que se repita mas de dos veces
letra = input("ingresa un palabra donde se repita las letras:\n")
lsita={}
for i in letra:
    if i in lsita:
        lsita[i]=lsita[i]+1
    else:
        lsita[i]=1

#frecuncia de las letras que estan repetidas
letrafrecu = ''
letramayor =0
#recorrer el diccionario y contar las letras que se repiten
for i in lsita:
    if lsita[i]>letramayor:
        letramayor=lsita[i]
        letrafrecu=i
print("la letra que se repite  es:", letrafrecu)
print("se repite",letramayor, "es veces")
