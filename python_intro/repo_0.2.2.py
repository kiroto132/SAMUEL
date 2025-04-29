#pelicula 
recomendaciones = {
        "accion": {
            "niños": ["mini espias", "como entrenar a tu dragon1,2,3"],
            "adultos": ["Enter the Dragon", "John Wick"]
        },
        "comedia": {
            "niños": ["albin y las ardillas", "matilda"],
            "adultos": ["ese es mi hijo", "project x"]
        },
        "terror": {
            "niños": ["Coraline", " Frankenweenie"],
            "adultos": ["The Conjuring", "31"]
        }
    }
edad =int(input("ingresa tu edad:\n"))
print("tipo de peliculas: accion, comedia, terror")
preferencia = input("ingresa la preferencia de pelicula:\n").lower()

if edad <= 13:
    grupo_edad = "niños"
else:
    grupo_edad = "adultos"

if preferencia in recomendaciones:
    peliculas = recomendaciones[preferencia][grupo_edad]
    print(f"te recomendamos las siguientes peliculas de tu {preferencia}: {", ".join(peliculas)}")
else:
    print("lo sentimos, no tenemos recomendaciones para ese genero")
