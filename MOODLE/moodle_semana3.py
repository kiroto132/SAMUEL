#Eres parte del equipo de desarrollo de software de una tienda que desea mejorar la gestión de su inventario digital. Te han asignado la tarea de crear un programa en Python que permita al equipo añadir, consultar, actualizar y eliminar productos del inventario de manera eficiente, así como calcular el valor total del inventario. Tu programa debe interactuar con el usuario para realizar las siguientes operaciones:
# 1. Añadir un nuevo producto al inventario.
# 2. Consultar la información de un producto específico.
# 3. Actualizar la información de un producto existente.
# 4. Eliminar un producto del inventario.
# 5. Calcular el valor total del inventario.
# 6. Mostrar todos los productos en el inventario.
# 7. Salir del programa.

inve = {}
valor = 0
cantidad = 0
# Definimos una función para agregar un producto al inventario
def agregar_producto():
    global valor
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    if nombre in inve:
        print(f"El producto {nombre} ya existe en el inventario.")
    else:
        inve[nombre] = {"precio": precio, "cantidad": cantidad}
        valor += precio * cantidad
        print(f"Producto {nombre} agregado al inventario.")

# Definimos una función para mostrar el inventario
def mostrar_inventario():
    if not inve:
        print("le inventario esta vacio, ingresa los productos en la seccion de agregar productos")
    else:
        print("el inviterio es el siguiente:\n")
        for nombre, info in inve.items():
            print(f"nombre: {nombre}, precio: ${info['precio']}, cantidad: {info['cantidad']}")
        print(f"el valor total del inventario es: ${valor}")
        print()

# Definimos una función para consultar un producto
def consultar_producto():
    nombre = input("ingrese el nombre del producto para vereficar si esta en el inventario:\n")
    if nombre in inve:
        print(f"el producto {nombre} esta en el inventario")
    else:
        print(f"el producto {nombre} no esta en el inventario, Por favor agrege el producto en la seccion de agregar producto")

# Definimos una función para actualizar un producto
def actualizar_producto():
    nombre = input("ingresa el nombre del producta paara la actualizacion:\n")
    if nombre in inve:
        precio = float(input("ingrese el nuevo precio del producto:\n"))
        cantidad = int(input("engrese la nueva cantidasd del producto:\n"))
        inve[nombre]["precio"] = precio
        inve[nombre]["cantidad"] = cantidad
        print(f"el producto {nombre} fue actualizado exitosamente")
    else:
        print(f"el producto {nombre} no esta en el inventario, por favor agregue el producto en la seccion de agregar producto")

# Definimos una función para eliminar un producto
def eliminar_producto():
    nombre = input("ingrese el nombre del producto que deseas eliminar:\n")
    if nombre in inve:
        del inve[nombre]
        print(f"el producto {nombre} fue eliminado exitosamente")
    else:
        print(f"el producto {nombre} no esta en el inventario, por favor agregue el producto en la seccion de agregar producto")

# Definimos una función para calcular el valor total del inventario
# Esta función calcula el valor total del inventario sumando el precio de cada producto multiplicado por su cantidad
def calcular_valort():
    calcular_total = lambda productos: sum(map(lambda p: p["precio"] * p["cantidad"], productos))
    total = calcular_total(inve.values())
    print(f"El valor total del inventario es: ${total:.2f}")

# Definimos una función para verificar la contraseña(opcional)
def contrasena(no):
    contrasena = "1234"
    while True:
        password = input("ingresa la contrasena:\n")
        if password == contrasena:
            print(f"contrasena correcta")
            print(f"bienvenido al sistema de inventario {no}")
            print("por favor elige una opcion del menu")
            break
        else:
            print("contrasena incorrecta, intenta de nuevo")


def salir():
    print("saliendo del programa, feliz dia")
    exit()
    print("opcion no valida, por favor elige una opcion valida")

# Definimos una función para mostrar el menú y manejar la interacción con el usuario
def menu():
    while True:
        print("Menu de inventario")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Consultar producto")
        print("4. Actualizar producto")
        print("5. Eliminar producto")
        print("6. Calcular valor total del inventario")
        print("7. Salir")

        opcion = input("Elige una opcion: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            consultar_producto()
        elif opcion == "4":
            actualizar_producto()
        elif opcion == "5":
            eliminar_producto()
        elif opcion == "6":
            calcular_valort()
        elif opcion == "7":
            salir()
        else:
            print("opcion no valida, por favor elige una opcion valida")

contrasena(input("nombre del administrador:\n"))
menu()