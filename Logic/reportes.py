from Logic.cordinador import *
def reportecantidadproductos():
    productos=abrirJSON()
    print("Cantidad de productos disponibles:")
    print(len(productos))
    print("Productos:")
    for i in range(len(productos)):
        print(productos[i]["name"])
        print(productos[i]["description"])
        print(productos[i]["price"])
        print(" ")

def serviciopopular():
    usuario=abrirJSON2()
    n=0
    m=0
    t=0
    h=0
    s=0
    for i in range(len(usuario)):
        if usuario[i]["servicio en uso"]=="Internet":
            n+=1
        if usuario[i]["servicio en uso"]=="Mobile Plan":
            m+=1
        if usuario[i]["servicio en uso"]=="TV Package":
            t+=1
        if usuario[i]["servicio en uso"]=="Home Phone":
            h+=1
        if usuario[i]["servicio en uso"]=="Smart Home":
            s+=1
    if n>m:
        if n>t:
            if n>h:
                if n>s:
                    print("El servicio mas popular es: Internet")
                else:
                    print("El servicio mas popular es: Smart Home")
            elif h>s:
                print("EL servicio mas popular es: Home Phone")
            else:
                print("El servicio mas popular es: Smart Home")
        elif t>h:
            if t>s:
                print("EL servicio mas popular es: TV Package")
            else:
                print("EL servicio mas popular es: Smart Home")
        elif h>s:
            print("EL servicio mas popular es: Home Phone")
        else:
            print("EL servicio mas popular es: Smart Home")
    else:
        if m>t:
            if m>h:
                if m>s:
                    print("El servicio mas porpular es: Mobile Plan")
                else:
                    print("El servcio mas popular es: Smart Home")
            elif h>s:
                print("EL servicio mas popular es: Home Phone")
            else:
                print("EL servicio mas popular es: Smart Home")
        elif t>h:
            if t>s:
                print("EL servicio mas popular es: TV Package")
            else:
                print("EL servicio mas popular es: Smart Home")
        elif h>s:
            print("EL servicio mas popular es: Home Phone")
        else:
            print("EL servicio mas popular es: Smart Home")