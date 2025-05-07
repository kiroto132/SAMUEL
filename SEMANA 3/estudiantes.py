estudiantes = {}

def agregar_estudantes(nombre_estduantes, edad_estudiantes, calificacion):
    estudiantes[nombre_estduantes] = {"edad": edad_estudiantes, "calificacion": calificacion}
    print(f"se ha agregado el estudiante {nombre_estduantes} con la edad {edad_estudiantes} y la calificacion {calificacion} a la lista de estudiantes")

def modificar_calificacion(nombre_estduantes, calificacion):
    if nombre_estduantes in estudiantes:
        estudiantes[nombre_estduantes]["calificacion"] = calificacion
        print(f"se ha modificado la calificacion de {nombre_estduantes} a {calificacion}")
    else:
        print(f"el estudiante {nombre_estduantes} no se encuentra en la lista de estudiantes")


def mostrar_todos_los_estudiantes():
    if estudiantes:
        print("estudiantes en la lista:")
        for nombre_estduantes, datos in estudiantes.items():
            print(f"este es el estudiante {nombre_estduantes}: edad: {datos['edad']}, calificacion: {datos['calificacion']}")
    else:
        print("no hay estudiantes en la lista")
def eliminar_estudiante(nombre_estduantes):
    if nombre_estduantes in estudiantes:
        del estudiantes[nombre_estduantes]
        print(f"se ha eliminado el estudiante {nombre_estduantes} de la lista de estudiantes")
    else:
        print(f"el estudiante {nombre_estduantes} no se encuentra en la lista de estudiantes")



def menu():
    while True:
        print("1. agregar estudiante")
        print("2. modificar la calificacion de un estudiante")
        print("3. mostrar todos los estudiantes")
        print("4. eliminar estudiante")
        print("5. salir")

        opcion = int(input("selecciona una opcion:\n"))
        try:
            match opcion:
                case 1:
                    nombre_estduantes = input("ingrese el nombre del estudiante:\n")
                    edad_estudiantes = int(input(f"ingrese la edad de {nombre_estduantes}:\n"))
                    calificacion = float(input(f"ingrese la calificacion de {nombre_estduantes}:\n"))
                    agregar_estudantes(nombre_estduantes, edad_estudiantes, calificacion)
                case 2:
                    nombre_estduantes = input("ingresa el nombre del estudiante:\n")
                    calificacion = float(input(f"ingrese la nueva calificacion de {nombre_estduantes}:\n"))
                    modificar_calificacion(nombre_estduantes, calificacion)
                case 3:
                    mostrar_todos_los_estudiantes()
                case 4:  
                    nombre_estduantes = input("ingresa el nombre del estudiante que quieres eliminar:\n")
                    eliminar_estudiante(nombre_estduantes)
                case 5:
                    print("saliendo del programa")
                    break
        except ValueError:
            print("opcion no valida, por favor selecciona una opcion valida")
menu()