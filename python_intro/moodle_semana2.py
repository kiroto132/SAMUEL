try:
        calificacion = float(input("Ingresa una calificación numérica (0-100): "))
        if 0 <= calificacion <= 100:
            if calificacion >= 60:
                print("El estudiante ha aprobado.")
            else:
                print("El estudiante ha reprobado.")
        else:
            print("Por favor, ingresa un número entre 0 y 100.")
except ValueError:
        print("Entrada inválida. Por favor, ingresa un número.")


try:
    calificaciones = input("Ingresa una lista de calificaciones separadas por comas: ")
    lista_calificaciones = [float(x) for x in calificaciones.split(',')]
    promedio = sum(lista_calificaciones) / len(lista_calificaciones)
    print(f"El promedio de las calificaciones es: {promedio:.2f}")
except ValueError:
    print("Entrada inválida. Asegúrate de ingresar números separados por comas.")



try:
    valor = float(input("Ingresa un valor para comparar: "))
    contador = 0
    for calificacion in lista_calificaciones:
        if calificacion > valor:
            contador += 1
        print(f"Hay {contador} calificaciones mayores que {valor}.")
except ValueError:
        print("Entrada inválida. Por favor, ingresa un número.")



try:
        valor_especifico = float(input("Ingresa una calificación específica para contar: "))
        contador = 0
        for calificacion in lista_calificaciones:
            if calificacion == valor_especifico:
                contador += 1
        print(f"La calificación {valor_especifico} aparece {contador} veces en la lista.")
except ValueError:
        print("Entrada inválida. Por favor, ingresa un número.")