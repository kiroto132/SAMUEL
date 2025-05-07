agenda = {}


def agregar_contacto(nombre, telefono):
    agenda[nombre] = telefono
    print(f"se ha agregado el contacto {nombre} con el numero {telefono} a la agenda")


def buscar_contacto(nombre):
    if nombre in agenda:
        print(f"el contacto {nombre} con el numero {agenda[nombre]} esta en la agenda")
    else:
        print(f"el contacto {nombre} no se encuentra en la agenda")


def mostrar_todos_los_contactos():
    if agenda:
        print("contactos en la agenda:")
        for nombre, telefono in agenda.items():
            print(f"estos son los cotactos {nombre}: {telefono}")
    else:
        print("no hay contactos en la agenda")


def eliminar_contacto(nombre):
        if nombre in agenda:
            del agenda[nombre]
            print(f"se ha eliminado el contacto {nombre} de la agenda")
        elif nombre not in agenda:
            print(f"el contacto {nombre} no se encuentra en la agenda")
        else:
            print("no hay contactos en la agenda")
        mostrar_todos_los_contactos()


def menu():
    while True:
        print("1. agregar contacto")
        print("2. buscar contacto")
        print("3. mostrar todos los contactos")
        print("4. eliminar contacto")
        print("5. salir")

        opcion = int(input("selecciona una opcion:\n"))
        try:
            match opcion:
                case 1:
                    nombre = input("ingrese el nombre del contacto:\n")
                    telefono = int(input(f"ingrese el numero de {nombre}:\n"))
                    agregar_contacto(nombre, telefono)
                case 2:
                    nombre = input("ingresa el nombre del cntacto que quieres buscar:\n")
                    buscar_contacto(nombre)
                case 3:
                    mostrar_todos_los_contactos()
                case 4:  
                    nombre = input("ingresa el nombre del contacto que quieres elinar:\n")
                    eliminar_contacto(nombre)
                case 5:
                    print("saliendo del programa")
                    return
                case _:
                    print("opcion no valida, por favor selecciona una opcion valida")
        except ValueError:
            
            print("por favor ingresa un numero valido")
menu()