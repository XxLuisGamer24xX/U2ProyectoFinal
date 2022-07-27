from guardarMongo import *
from ScriptGenerarNUsuarios import *
def menuPrincipal():
    '''
    def menuPrincipal():
        Procedimiento que muestra el menu principal del programa, valiando con el try except los posibles errores que puedan ocurrir.
    '''
    try:
        print("-----------------------------------------------------")
        print("               MENÚ PRINCIPAL")
        print("-----------------------------------------------------")
        print("Ingrese 1..........: Para registrar N clientes")
        print("Ingrese 2..........: Para Salir")
        opcion=int(input("Ingrese una opción: "))
        if opcion==1:
            cantidadUsuarios=int(input("Cuántos Usuarios desea registrar: "))
            generarUsuarios(cantidadUsuarios)
        elif opcion==2:
            print("-----------------------------------------------------")
            print("       Gracias por usar nuestro sistema")
            print("-----------------------------------------------------")
        else:
            print("-----------------------------------------------------")
            print("|              No existe esta opción                  |")
            print("|     Lo redireccionaremos al menú [Principal]        |")
            print("-----------------------------------------------------")
            print ("                       |")
            print ("                       |")
            print ("                       |")
            print ("                       |")
            print ("                       V")
            menuPrincipal()
    except:
        print("-----------------------------------------------------")
        print("|       No puede ingresar valores no numéricos        |")
        print("|      Lo redireccionaremos al menú [Principal]       |")
        print("-----------------------------------------------------")
        print ("                       |")
        print ("                       |")
        print ("                       |")
        print ("                       |")
        print ("                       V")
        menuPrincipal()