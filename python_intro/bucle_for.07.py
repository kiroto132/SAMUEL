#pedir al usuario que ingrese una oracion 
palabra = input("ingrese una oracion:\n")
#contar la oracion para que no cuente los espacios 
oracion = palabra.split()
#contador de las palabras en la oracion 
contador = 0
#opcional, si quieres saber cuales son las palabras que tienen mas de 3 letras
palabraslar = []
#recorrer la oracion y hace el conteo de las palabras que tienen mas de 3 letras
for i in oracion:
    if len(i) > 3:
        contador += 1   
        palabraslar.append(i)
#imprimir los resultados
print(f"el numero de palabras con mas letras es: {contador}")
print("Las palabras con más de 3 letras son:", ", ".join(palabraslar))