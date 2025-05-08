# en este codigo lo que utilizamos fue crear una agenda de contactos en un diccionario dentro de una lista 
contactos = []

def agregar_contacto(nombre, celular, estado_civil, genero):
    print(f"se ha registrado el contacto {nombre} con el numero {celular} con el estado civil {estado_civil} y el genero {genero}.")
    agenda = {
        "name" : nombre,
        "phone" : celular,
        "estado" : estado_civil,
        "genero" : genero
    }
    contactos.append(agenda)
#
def buscar_contacto(nombre):
    for agenda in contactos:
        if agenda["name"] == nombre:
            print(f"el numero de {nombre} es {agenda['phone']}")
            return agenda
        print("el contacto no existe")
        return None

#
def mostrar_contactos():
    if not contactos:
        print("no hay contactos")
        return
    print("contactos registrados:")
    for agenda in contactos:
        print(f"nombre:{agenda['name']},celular: {agenda['phone']}, estado civil: {agenda['estado']},genero: {agenda['genero']}")

#
def modificar_contacto(nombre, nuevo_celular, estado_n, genero_n):
    contacto = buscar_contacto(nombre)
    if contacto:
        if nuevo_celular:
            contacto["phone"] = nuevo_celular
        if estado_n:
            contacto["estado civil"] = estado_n
        if genero_n:
            contacto["genero"] = genero_n
        print(f"se ha modificado el contacto {nombre} con el nuevo numero {nuevo_celular} con el nuevo {estado_n} y genero {genero_n}.")
        return True
    return False

#
def eliminar_contactos(nombre):
    for contacto in contactos:
        if contacto["name"] == nombre:
            contactos.remove(contacto)
            print(f"Se ha eliminado el contacto {nombre}.")
            return
    print("El contacto no existe.")

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
                    celular = int(input(f"ingresa el numero de celular de {nombre}:\n"))
                    estado_civil = str(input("estado civil:\n"))
                    genero = str(input("cual es tu genero:\n"))
                    agregar_contacto(nombre, celular, estado_civil, genero)
                case 2:
                    nombre = input("ingresa el nombre del contacto que quieres buscar:\n")
                    buscar_contacto(nombre)
                case 3:
                    mostrar_contactos()
                case 4:
                    print(f"lista de contactos {contactos}")
                    nombre = input("ingresa el nombre del contacto que quieres modificar:\n")
                    nuevo_celular = int(input(f"ingresa el nuevo numero de {nombre}:\n"))
                    estado_n = str(input("cual es el nuevo estado civil:\n"))
                    genero_n = str(input("cual es el nuevo genero:\n"))
                    modificar_contacto(nombre, nuevo_celular, estado_n, genero_n )
                case 5:
                    print(f"lista de contatos {contactos}")
                    nombre = input("ingresa el nombre del contacto que quieres eliminar:\n")
                    eliminar_contactos(nombre)
                case 6:
                    print("saliendo del programa")
                    break
                case _:
                    print("opcion no valida")
        except ValueError:
            print("opcion no valida, por favor selecciona una opcion valida")
menu()