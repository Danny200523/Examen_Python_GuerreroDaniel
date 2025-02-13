from Logic.cordinador import *

def menu_usuario():
    print("Bienvenido, Usuario")

def menu_principal():
    print('''
    ======================
    === Menú Principal ===
    ======================
    =   1. Coordinador   =
    =   2. Usuario       =
    =   0. Salir         =
    ======================
          ''')

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        menu_coordinador()
    elif opcion == "2":
        menu_usuario()
    elif opcion == "0":
        print("Saliendo del programa...")
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")

def menu_coordinador():
    print("Bienvenido, Coordinador")
    print("1. Agregar usuario")
    print("2. Agregar servicio")
    print("3. Eliminar usuario")
    print("4. Eliminar servicio")
    print("5. Modificar usuario")
    print("6. Modificar servicio")
    print("Ver usuarios")
    print("Ver servicios")
    print("0. Salir")
    opcion=int(input("Ingrese la opcion:"))
    if opcion==1:
        aggusuario()
    elif opcion==2:
        aggServicio()
    elif opcion==3:
        eliminarUsuario()
    elif opcion==4:
        eliminarServicio()
    elif opcion==5:
        modificarUsuario()
    elif opcion==6:
        modificarServicio()
    elif opcion==0:
        print("Saliendo del programa...")
    else:
        print("Opcion invalida")
