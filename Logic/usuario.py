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