from Interfaces.interfazCallCenter import *
from MongoDb.guardarEnMongo import * 
import sys
class Usuarios():
    '''
    class Usuarios():
        Clase que Padre que contiene los atributos de los usuarios y métodos para registrar y iniciar sesión 
    Atributos:
        nombre: string
        apellido: string
        usuario: string
        email: string
        contraseña: string
    -------------------------
    Métodos:
        def __init__(self, usuario, contraseña,nombre ,apellido, email):
    '''
    usuarios=retornarUsuarios()
    contraseñas=retornarContraseñas()
    def __init__(self, usuario, contraseña,nombre ,apellido, email, cedula ):
        '''
        def __init__(self, usuario, contraseña,nombre ,apellido, email, cedula ):
            Método constructor de la clase Usuarios, que recibe los atributos de los usuarios como nombre, apellido, usuario, email, contraseña y cedula
        '''
        self.usuario = usuario
        self.contraseña = contraseña
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.cedula=cedula
    def inciar(usuario, contrasenia):
        '''
        def inciar(usuario, contrasenia):
            Método que recibe el usuario y contraseña los cuales validará con las query de usuario y contraseña que extraen de la base de datos
        Parametros:
            usuario: string
            contrasenia: string
        '''
        '''
        Llamado de la funcion retirnarUsuarios() que retorna una lista de usuarios
        Llamado de la funcion retornarContraseñas() que retorna una lista de contraseñas
        Donde almacenaremos los usuarios y contraseñas en una lista, para luego hacer una búsqueda con los parametros de usuario y contraseña
        '''
        usuarios=retornarUsuarios()
        contrasenias=retornarContraseñas()
        if usuario in usuarios and contrasenia in contrasenias:            
            print("Bienvenidp al sistema")
            return True
        else:
            print("Usuario o contraseña incorrectos")
            return False
