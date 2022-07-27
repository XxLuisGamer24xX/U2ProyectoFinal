from Interfaces.InterfazLogin import *
if __name__=="__main__":
    '''
    if __name__=="__main__":
        Main del programa, se encarga de crear la ventana principal, y ejecutar la primera interfaz "Login".
        El cual es la que se encarga de iniciar sesión o registrarse, para los administradores del callcenter.
    '''
    app= QApplication([])
    window=MainApp3()
    window.show()
    app.exec_()
