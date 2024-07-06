import json
datos=[]
election=0
on=0
tipo=None
numero=None
def datos_de_evento(nombre,apellido,numero,direccion,tipo,fecha):
    evento={
        "nombre":nombre,
        "apellio":apellido,
        "numero":numero,
        "direccion":direccion,
        "tipo":tipo,
        "fecha":fecha
        }
    datos.append(evento)
    print(" Se agregaron los datos ")

while on==0:
    print("""----- Seleccione una opcion -----
          1).Agregar evento
          2).ver eventos
          3).guardar registro de evento
          4).cargar registro de eventos
          5).Terminar proceso
          """)
    try:
        election=int(input())
    except ValueError:
        print(" solo se aceptan numeros enteros del 1 al 6 ")
    if election==1:
        nombre=input(" Ingrese el nombre del cliente: ")
        print("----- Nombre ingresado -----")
        apellido=input(" Ingresa el apellido del cliente: ")
        while numero==None:
            try:
                numero=int(input(" Ingrese un numero "))
            except ValueError:
                print(" Ingrese un numero telefonico de 10 digitos ")
            print("----- Numero ingresado telefonico -----")
        while tipo==None:
            print("""----- Seleccione el tipo de comida -----
                  1)comida italianada
                  2)comida japonesa
                  3)BBQ
                  """)
            try:
                election=int(input())
            except:
                print(" solo se permiten numeros enteros del menu ")
            if election==1:
                tipo="camida italina"
                print("----- Se agrego el tipo de comida -----")
            elif election==2:
                tipo="comida japonesa"
                print("----- Se agrego el tipo de comida -----")
            elif election==3:
                tipo="BBQ"
                print("----- Se agrego el tipo de comida -----")
            else:
                print(" no se encontro ese tipo de comida ")
        direccion=input(" Ingrese direcion ")
        print("----- Direccion ingresada -----")
        fecha=input(" Ingrese fecha ")
        print("----- Fache ingresada -----")
        datos_de_evento(nombre,apellido,numero,direccion,tipo,fecha)
        print(" Pedido registrado ")

    elif election==2:
        for evento in datos:
            print(evento)
    elif election==3:
        with open('RegistroDeEvento.json','w') as file:
            json.dump(datos,file,indent=4)
        with open('RegistroDeEvento.txt','w') as Archivo:
            Archivo.write(f"{datos}")
            print(" Archivo guardado ")
    elif election==4:
        with open('RegistroDeEvento.json','r') as file:
            datos=json.load(file)
    elif election==5:
        print("-----Termino de proceso -----")
