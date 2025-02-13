from Logic.cordinador import *

def verservicios():
    servicio=abrirJSON
    print("Servicios disponibles y caracteristicas:")
    print("1. Internet")
    print("2. Mobile Plan")
    print("3. TV Package")
    print("4. Home Phone")
    print("5. Smart Home")
    x=int(input("Seleccione una opción:"))
    for i in range(len(servicio)):
        if i==0 and x==1:
            print(servicio[i]["name"])
            print(servicio[i]["description"])
            print(servicio[i]["price"])
        elif i==1 and x==2:
            print(servicio[i]["name"])
            print(servicio[i]["description"])
            print(servicio[i]["price"])
        elif i==2 and x==3:
            print(servicio[i]["name"])
            print(servicio[i]["description"])
            print(servicio[i]["price"])
        elif i==3 and x==4:
            print(servicio[i]["name"])
            print(servicio[i]["description"])
            print(servicio[i]["price"])
        elif i==4 and x==5:
            print(servicio[i]["name"])
            print(servicio[i]["description"])
            print(servicio[i]["price"])
        else:
            print("Opcion invalida")

def interaccionempresa():
    Usuarios=abrirJSON2()
    print("numero de id del cliente: ")
    cliente=int(input(": "))
    print("Ingrese que quiere hacer")
    print("1. Poner un reclamo")
    print("2. Generar consulta al servicio al cliente")
    print("3. generar sugerencia")
    hacer=int(input("Ingrese la opcion:"))
    for i in range(len(Usuarios)):
        if cliente==Usuarios[i]["id"]:
            if hacer==1:
                reclamo=input("Ingrese el reclamo:")
                Usuarios[i]["reclamo"]=reclamo
                guardarJSON2(Usuarios)
            elif hacer==2:
                consulta=input("Ingrese la consulta:")
                Usuarios[i]["consulta"]=consulta
                guardarJSON2(Usuarios)
            elif hacer==3:
                sugerencia=input("Ingrese la sugerencia:")
                Usuarios[i]["sugerencia"]=sugerencia
                guardarJSON2(Usuarios)

def vermisdatos():
    Usuarios=abrirJSON2()
    print("numero de id del cliente: ")
    cliente=int(input(": "))
    for i in range(len(Usuarios)):
        if cliente==Usuarios[i]["id"]:
            print("Nombre:",Usuarios[i]["nombre"])
            print("Apellido:",Usuarios[i]["apellido"])
            print("ID:",Usuarios[i]["id"])
            print("Telefono:",Usuarios[i]["telefono"])
            print("Direccion:",Usuarios[i]["direccion"])
            print("Servicios:",Usuarios[i]["servicios"])
            print("Tiempo:",Usuarios[i]["tiempo"])
            print("Reclamo:",Usuarios[i]["reclamo"])
            print("Consulta:",Usuarios[i]["consulta"])
            print("Sugerencia:",Usuarios[i]["sugerencia"])
            print("")

def vermisservicios():
    Usuarios=abrirJSON2()
    print("numero de id del cliente: ")
    cliente=int(input(": "))
    for i in range(len(Usuarios)):
        if cliente==Usuarios[i]["id"]:
            print("Servicios:",Usuarios[i]["servicios"])
            print("Tiempo:",Usuarios[i]["tiempo"])
            print("")
