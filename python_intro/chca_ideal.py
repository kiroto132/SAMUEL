puntaje = 0


pregunta1 = input('¿Eress mujer?\n')
if pregunta1 == 'si':
    puntaje=puntaje+10
    pregunta2 = input('¿Eres trans?\n')
    if pregunta2 == 'si':
            puntaje=puntaje-1000
    elif pregunta2 == "no":
            puntaje=puntaje+50
            pregunta3 = input("¿Tienes como demostrarlo?\n")
            if pregunta3 == "si":
                puntaje=puntaje+100
            elif pregunta3 == "no":
                    puntaje=puntaje+0
                    print("NO PUEDES CONTINUAR")
                    pregunta4 = int(input("¿Cuantos años tienes?\n"))  
            if pregunta4 >=16 and pregunta4 <=21:
                puntaje=puntaje+100
                if pregunta4 <=15 and pregunta4 >=21:
                    puntaje=puntaje+0
                    print("No pasas por la edad")  
                else:
                    pregunta5 = input("¿te gustan los animales?\n")
                    if pregunta5 == "si":
                        puntaje=puntaje+50
                    elif pregunta5 == "no":
                        puntaje=puntaje-50
                    preguntaja6 = input("¿te gustan las motos de alto cilindraje?\n")
                    if preguntaja6 == "si":
                        puntaje=puntaje+1000
                        if preguntaja6== "no":
                            puntaje=puntaje-50
                            

else: 
     print("no aplicas")

print("El cuestiomario termino")
print(f"tu puntaje es: {puntaje}")
if puntaje <= 210:
    print("no pasaste como mi chica ideal")
