# en este codigo lo que utilizamos fue crear una agenda de contactos en un diccionario dentro de una lista 

contactos = [{

}]

def agregar_contacto(nombre, celular):
    contactos[0][nombre] = celular
    print(f"se ha registrado el contacto {nombre} con el numero {celular}.")

#
def buscar_contacto(nombre):
    if nombre in contactos[0]:
        print(f"el numero de {nombre} es {contactos[0][nombre]}")
    else:
        print("el contacto no existe")

#
def mostrar_contactos():
    print("contactos registrados:")
    for nombre, celular in contactos[0].items():
        print(f"{nombre}: {celular}")

#
def modificar_contacto(nombre, nuevo_celular):
    if nombre in contactos[0]:
        contactos[0][nombre] = nuevo_celular
        print(f"se ha modificado el numero de {nombre} a {nuevo_celular}.")
    else:
        print("el contacto no existe")

#
def eliminar_contacto(nombre):
    if nombre in contactos[0]:
        del contactos[0][nombre]
        print(f"se ha eliminado el contacto {nombre}.")
    else:
        print("el contacto no existe")

#
def menu():
    while True:
        print("1. agregar contacto")
        print("2. buscar contacto")
        print("3. mostrar contactos")
        print("4. modificar contacto")
        print("5. eliminar contacto")
        print("6. salir")
        
        opcion = int(input("elige una opcion:\n"))
        try:    
            match opcion:
                case 1:
                    nombre = str(input("registra el nuevo contacto:\n"))
                    celular = int(input(f"ingresa el numero de celualar de {nombre}:\n"))
                    agregar_contacto(nombre, celular)
                case 2:
                    nombre = input("ingresa el nombre del contacto que quieres buscar:\n")
                    buscar_contacto(nombre)
                case 3:
                    mostrar_contactos()
                case 4:
                    print(f"lista de contactos {contactos[0]}")
                    nombre = input("ingresa el nombre del contacto que quieres modificar:\n")
                    nuevo_celular = int(input(f"ingresa el nuevo numero de {nombre}:\n"))
                    modificar_contacto(nombre, nuevo_celular)
                case 5:
                    print(f"lista de contatos {contactos[0]}")
                    nombre = input("ingresa el nombre del contacto que quieres eliminar:\n")
                    eliminar_contacto(nombre)
                case 6:
                    print("saliendo del programa")
                    break
                case _:
                    print("opcion no valida")
        except ValueError:
            print("opcion no valida, por favor selecciona una opcion valida")
menu()
