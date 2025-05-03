segundostol = int(input('ingrese los segundos deseados: \n'))
def extraer_hms(segundos_totales):
    horas = (segundos_totales // 3600)
    minutos = (segundos_totales % 3600) // 60
    segundos = (segundos_totales % 60)
    return horas, minutos, segundos 

h, m, s = extraer_hms(segundostol)

print(f'{h} horas, {m} minutos, {s} segundos')