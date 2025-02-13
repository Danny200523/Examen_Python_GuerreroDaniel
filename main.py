from Design.Menus import *
while True:
    menu_principal()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        menu_coordinador()
    elif opcion == "2":
        menu_usuario()
    elif opcion == "0":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")