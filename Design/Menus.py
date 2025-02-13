from Logic.cordinador import *
from Logic.usuario import *
from Logic.reportes import *
from Logic.autosistem import *

def menu_usuario():
    usuaro=abrirJSON2()
    print("Bienvenido, Usuario")
    print("Digite su ID")
    id=int(input(": "))
    for i in range(len(usuaro)):
        if id==usuaro[i]["id"]:
            if usuaro[i]["categoria"]=="Leal":
                print("Bienvnido le ofrecemos un 15%"," de descuento en todos nuestros servicios por ser un cliente leal")
                print("Que desea hacer?")
                print("1. Ver servicios")
                print("2. Ver mis servicios")
                print("3. Ver mis datos")
                print("4. hacer interaccion a la empresa")
                print("0. Salir")
                opcion=int(input(":"))
                if opcion==1:
                    verserviciosleal()
                elif opcion==2:
                    vermisservicios()
                elif opcion==3:
                    vermisdatos()
                elif opcion==4:
                    interaccionempresa()
                elif opcion==0:
                    print("Saliendo del programa...")
                else:
                    print("Opcion invalida")
            else:
                print("Que desea hacer?")
                print("1. Ver servicios")
                print("2. Ver mis servicios")
                print("3. Ver mis datos")
                print("0. Salir")
                opcion=int(input(":"))
                if opcion==1:
                    verServicios()
                elif opcion==2:
                    vermisservicios()
                elif opcion==3:
                    vermisdatos()
                elif opcion==0:
                    print("Saliendo del programa...")
                else:
                    print("Opcion invalida")

def menu_principal():
    asignarcategoria()
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
    print("7. Ver usuarios")
    print("8. Ver servicios")
    print("9. reporte cantidad de productos")
    print("10. ver el servicio mas popular")
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
    elif opcion==7:
        verUsuarios()
    elif opcion==8:
        verServicios()
    elif opcion==9:
        reportecantidadproductos()
    elif opcion==10:
        serviciopopular()
    elif opcion==0:
        print("Saliendo del programa...")
    else:
        print("Opcion invalida")
