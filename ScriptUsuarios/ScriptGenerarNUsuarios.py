import pandas as pd
import random as r
import time
from guardarMongo import*
data = pd.read_csv("ScriptUsuarios\BaseUsuarios.csv")
'''
data=pd.read_csv("ScriptUsuarios\BaseUsuarios.csv"):
    Sintaaxís para abrir el archivo csv y obtener los datos separados en un diccionario
'''
def obtenerDatosPorSeparados():
    '''
    def obtenerDatosPorSeparados():
        Funcion que obtiene los datos separados en diferentes  diccionarios
    '''
    nombres=[]
    apellidos=[]
    telefonos=[]
    direcciones=[]
    nombres = data["nombre"]
    apellidos = data["apellido"]
    telefonos= data["telefono"]
    direcciones = data["direccion"]
    return nombres, apellidos, telefonos, direcciones
def generarUsuarios(cantidadUsuarios):
    '''
    generarUsuarios(cantidadUsuarios):
        Funcion que genera N cantidad de usuarios en una coleccion, y luego es insertada en mongo db
    '''
    nombres=obtenerDatosPorSeparados()[0]
    apellidos=obtenerDatosPorSeparados()[1]
    telefonos=obtenerDatosPorSeparados()[2]
    direcciones=obtenerDatosPorSeparados()[3]
    
    diccionarios=[]
    for i in range(cantidadUsuarios):
        cedula=r.randint(2000000000,9999999999)
        diccionarios.append({"_id":cedula,"nombre":nombres[r.randint(0,999)],"apellido":apellidos[r.randint(0,999)],"telefono":telefonos[r.randint(0,999)],"direccion":direcciones[r.randint(0,999)]})
    if guardarUsuario(diccionarios)==True:
        print("Usuarios registrados correctamente")
    else:
        print("Error al registrar usuarios")




    