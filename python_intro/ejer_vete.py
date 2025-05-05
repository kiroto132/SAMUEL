nombres = []
edad = []
animal = []
enfermo = []

def agregar_anima():
    nema = input("Introduce el nombre:\n ")
    year = input("Introduce la edad:\n ")
    ane = input("tipo de animal:\n")
    estado = input("el animal esta enfermo?: si/no\n").strip().lower()
    
    nombres.append(nema)
    edad.append(year)
    animal.append(ane)
    enfermo.append(estado == "si")

    print(f"EL animal {nombres}, agregado existosamente")

def mostrar_mascota():
    if not nombres:
        print("NO hay animles regitrados")
        return 
    
    print("la lista de animales:\n")
    for i in range(len(nombres)):
        estado = "enfermo" if enfermo[i] else "sano"
        print(f"{i + 1}. nombre: {nombres[i]}, edad: {edad[i]}, tipo de animal: {animal[i]}, estado: {estado[i]}")
    print()


def eliminar():
    name = input("ingresa el nombre que deseas eliminar:\n")
    if name in nombres:
        index = nombres.index(name)
        nombres.pop(index)
        edad.pop(index)
        animal.pop(index)
        enfermo.pop(index)
        print(f"EL animal {name}, fue elimnado exitosamente:\n")
    else:
        print(f"el animal {nombres}, no esta en la lista de animales")


def contrasena():
    contrasena = "1234"
    while True:
        password = input("ingresa la contrasena:\n")
        if password == contrasena:
            print("contrasena correcta")
            break
        else:
            print("contrasena incorrecta, intenta de nuevo")
            
def menu():
    while True:
        print("Menu, organizar la citas de los animales")
        print("1. Agregar animales")
        print("2. mostrar animales")
        print("3. eliminar animales")
        print("4. salir")

        opcion = input("Elige una opcion: ")

        if opcion == "1":
            agregar_anima()
        elif opcion == "2":
            mostrar_mascota()
        elif opcion =="3":
            eliminar()
        elif opcion == "4":
            print("saliendo del programa")
            break
        else:
            print("opcion invalida intanta de nuevo")
if __name__ == "__main__":
    contrasena()
    menu()