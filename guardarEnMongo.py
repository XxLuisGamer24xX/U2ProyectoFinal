'''
import pymongo
    La libreria pymongo es una libreria que nos permite conectarnos a una base de datos
'''
import pymongo
MONGO_HOST = "localhost"
MONGO_PUERTO = "27017"
MONGO_TIEMPO_FUERA=1000
MONGO_NOMBREDB = "sistemaDeEmergencia911"
MONGO_NOMBRECOLECCION = "usuariosRegistrados"
MONGO_URI = "mongodb://"+MONGO_HOST+":"+MONGO_PUERTO+"/"
cliente = pymongo.MongoClient(MONGO_URI, serverSelectionTimeoutMS=MONGO_TIEMPO_FUERA)
baseDatos = cliente[MONGO_NOMBREDB]
coleccion = baseDatos[MONGO_NOMBRECOLECCION]
#-----------------------------------------------------------------------------
def guardarEnColeccion(documento):
    '''
    def guardarEnColeccion(documento):
        Funcion pra guardar un documento en la coleccion en mongo
    '''
    coleccion.insert_one(documento)

def retornarUsuarios():
    '''
    retornarUsuarios():
        Funcion que retorna una lista de usuarios extraido de la base de datos
    '''
    datosDeLaColeccion = coleccion.find()
    usuariosUsuarios = []
    for i in datosDeLaColeccion:
        usuariosUsuarios.append(i['usuario'])
    return usuariosUsuarios

    
def retornarContraseñas():
    '''
    retornarContraseñas():
        Funcion que retorna una lista de contraseñas extraido de la base de datos
    '''
    datosDeLaColeccion = coleccion.find()
    usuariosContraseñas = []
    for i in datosDeLaColeccion:
        usuariosContraseñas.append(i['contraseña'])
    return usuariosContraseñas

def retornarCedula():
    '''
    retornarCedula():
        Funcion que retorna una lista de cedulas extraido de la base de datos
    '''
    datosDeLaColeccion = coleccion.find()
    usuariosContraseñas = []
    for i in datosDeLaColeccion:
        usuariosContraseñas.append(i['cedula'])
    return usuariosContraseñas

def retornarNombre():
    '''
    retornarNombre():
        Funcion que retorna una lista de nombres extraido de la base de datos
    '''
    datosDeLaColeccion = coleccion.find()
    usuariosContraseñas = []
    for i in datosDeLaColeccion:
        usuariosContraseñas.append(i['nombre'])
    return usuariosContraseñas

def retornarApellido():
    '''
    retornarApellido():
        Funcion que retorna una lista de apellidos extraido de la base de datos
    '''
    datosDeLaColeccion = coleccion.find()
    usuariosContraseñas = []
    for i in datosDeLaColeccion:
        usuariosContraseñas.append(i['apellido'])
    return usuariosContraseñas