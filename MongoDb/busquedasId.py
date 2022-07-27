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

def buscarId(id):
    '''
    buscarId(id):
        Funcion que retorna una lista de usuarios extraido de la base de datos
    '''
    datosDeLaColeccion = coleccion.find()
    usuariosUsuarios = []
    for i in datosDeLaColeccion:
        if i['_id'] == id:
            usuariosUsuarios.append(i)
    return usuariosUsuarios
    print(usuariosUsuarios[0]['_id'])
    print(usuariosUsuarios[0]['usuario'])
    print(usuariosUsuarios[0]['contraseña'])
    print(usuariosUsuarios[0]['cedula'])
    print(usuariosUsuarios[0]['nombre'])
    print(usuariosUsuarios[0]['apellido'])
#print(buscarId(2911219224)[0]['nombre'])
