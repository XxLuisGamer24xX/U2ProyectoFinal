from guardarMongo import *
import pymongo
MONGO_HOST = "localhost"
MONGO_PUERTO = "27017"
MONGO_TIEMPO_FUERA=1000
MONGO_NOMBREDB = "sistemaDeEmergencia911"
MONGO_NOMBRECOLECCION = "baseUsuarios"
MONGO_URI = "mongodb://"+MONGO_HOST+":"+MONGO_PUERTO+"/"
cliente = pymongo.MongoClient(MONGO_URI, serverSelectionTimeoutMS=MONGO_TIEMPO_FUERA)
baseDatos = cliente[MONGO_NOMBREDB]
coleccion = baseDatos[MONGO_NOMBRECOLECCION] 
def guardarUsuario(documento):
    '''
    def guardarUsuario(documento):
        Funcion pra guardar un documento en la coleccion en MongoDb y retorna un true o false
        True si se guardo correctamente, False si no se guardo, validando con try except
    Parametro:
    -----------------
        documento: Tipo diccionario, que contiene los datos del usuario a guardar en la base de datos
    '''
    try:
        '''
        try:
            Se intenta guardar el documento en la coleccion en MongoDb y se retorna un true
        except:
            Se retorna un false si no se guardo correctamente en la base de datos
        '''
        coleccion.insert_many(documento)
        return True
    except:
        return False