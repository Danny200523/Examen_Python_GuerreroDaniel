from Logic.cordinador import *

def asignarcategoria():
    usuario=abrirJSON2()
    print("Asignar categoria a usuario")
    for i in range(len(usuario)):
        if usuario[i]["id"]:
            if usuario[i]["tiempo"]>=10:
                usuario[i]["categoria"]="Leal"
            elif usuario[i]["tiempo"]>=3:
                usuario[i]["categoria"]="Regular"
            elif usuario[i]["tiempo"]<3:
                usuario[i]["categoria"]="Nuevo"
            else:
                print("Opcion invalida")
            guardarJSON2(usuario)