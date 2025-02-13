import json
def abrirJSON():
    dicFinal={}
    with open('../Servicios.json','r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("../Servicios.json",'w') as outFile:
        json.dump(dic,outFile)

def abrirJSON2():
    dicFinal={}
    with open('../Usuarios.json','r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON2(dic):
    with open("../Usuarios.json",'w') as outFile:
        json.dump(dic,outFile)

def aggusuario():
    usuarios=abrirJSON2()
    nombre=input("Ingrese nombre del nuevo usuario usuario:")
    apellido=input("Ingrese apellido del nuevo usuario:")
    id=int(input("Ingrese id del nuevo usuario:"))
    telefono=input("Ingrese telefono del nuevo usuario:")
    direccion=input("Ingrese direccion del nuevo usuario:")
    servicios=input("Ingrese servicios usado del nuevo usuario:")
    usuarios.append({"id":id,
                     "nombre":nombre,
                     "apellido":apellido,
                     "tiempo":0,
                     "telefono":telefono,
                     "direccion":direccion,
                     "servicios":servicios})
    guardarJSON2(usuarios)
    print("Usuario agregado")

def aggServicio():
    servicios=abrirJSON()
    nombre=input("Ingrese nombre del nuevo servicio:")
    precio=int(input("Ingrese precio del nuevo servicio:"))
    descripcion=int(input("Ingrese la descripcion del nuevo servicio:"))
    servicios.append({"nombre":nombre,
                      "descripcion":descripcion,
                      "precio":precio,})
    guardarJSON(servicios)
    print("Servicio agregado")

def eliminarUsuario():
    usuarios=abrirJSON2()
    id=int(input("Ingrese el id del usuario a eliminar:"))
    for i in range(len(usuarios)):
        if usuarios[i]["id"]==id:
            usuarios.pop(i)
            print("Usuario eliminado")
            guardarJSON2(usuarios)

def eliminarServicio():
    servicios=abrirJSON()
    nombre=input("Ingrese el nombre del servicio a eliminar:")
    for i in range(len(servicios)):
        if servicios[i]["nombre"]==nombre:
            servicios.pop(i)
            print("Servicio eliminado")
            guardarJSON(servicios)

def modificarUsuario():
    usuarios=abrirJSON2()
    id=int(input("Ingrese el id del usuario a modificar:"))
    for i in range(len(usuarios)):
        if usuarios[i]["id"]==id:
            print("1. Modificar nombre")
            print("2. Modificar apellido")
            print("3. Modificar telefono")
            print("4. Modificar direccion")
            print("5. Modificar servicios")
            opcion=int(input("Ingrese la opcion a modificar:"))
            if opcion==1:
                usuarios[i]["nombre"]=input("Ingrese el nuevo nombre:")
            elif opcion==2:
                usuarios[i]["apellido"]=input("Ingrese el nuevo apellido:")
            elif opcion==3:
                usuarios[i]["telefono"]=input("Ingrese el nuevo telefono:")
            elif opcion==4:
                usuarios[i]["direccion"]=input("Ingrese la nueva direccion:")
            elif opcion==5:
                usuarios[i]["servicios"]=input("Ingrese el nuevo servicio:")
            else:
                print("Opcion invalida")
            guardarJSON2(usuarios)

def modificarServicio():
    servicios=abrirJSON()
    nombre=input("Ingrese el nombre del servicio a modificar:")
    for i in range(len(servicios)):
        if servicios[i]["nombre"]==nombre:
            print("1. Modificar nombre")
            print("2. Modificar descripcion")
            print("3. Modificar precio")
            opcion=int(input("Ingrese la opcion a modificar:"))
            if opcion==1:
                servicios[i]["nombre"]=input("Ingrese el nuevo nombre:")
            elif opcion==2:
                servicios[i]["descripcion"]=input("Ingrese la nueva descripcion:")
            elif opcion==3:
                servicios[i]["precio"]=int(input("Ingrese el nuevo precio:"))
            else:
                print("Opcion invalida")
            guardarJSON(servicios)

def verUsuarios():
    usuarios=abrirJSON2()
    for i in range(len(usuarios)):
        print("Nombre:",usuarios[i]["nombre"])
        print("Apellido:",usuarios[i]["apellido"])
        print("ID:",usuarios[i]["id"])
        print("Telefono:",usuarios[i]["telefono"])
        print("Direccion:",usuarios[i]["direccion"])
        print("Servicios:",usuarios[i]["servicios"])
        print("Tiempo:",usuarios[i]["tiempo"])
        print("")

def verServicios():
    servicios=abrirJSON()
    for i in range(len(servicios)):
        print("Nombre:",servicios[i]["nombre"])
        print("Descripcion:",servicios[i]["descripcion"])
        print("Precio:",servicios[i]["precio"])
        print("")

def verserviciosleal():
    servicio=abrirJSON()
    for i in range(len(servicio)):
        precio=servicio[i]["price"]
        descuento=precio*0.15
        print("Nombre del servicio",servicio[i]["name"])
        print("descripcion del servicio",servicio[i]["description"])
        print("Valor con descuento por ser cliente leal",precio-descuento)