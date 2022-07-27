'''
Librerías y módulos necesarios para ejecución del main y la interfaz de usuario
'''
from Interfaces.interfazCallCenter import *
from Interfaces.InterfazRegistro import *
from clases import *
from PyQt5.QtWidgets import* 
from PyQt5.QtCore import*
from PyQt5.QtGui import*
import sys
class MainApp(QMainWindow):
    '''
    class MainApp(QMainWindow):
        clase MainApp, que hereda de QMainWindow almecenar todos los valores  de la ventana mediante funciones de la clase QmainWindow.
    Slots:
    ---------------------
    def iniciarSesion(self):
        Metodo que se encarga de iniciar sesion, recibe el usuario y contraseña, y verifica si existe en la base de datos.
    def registrar(self):
        Metodo que me abre una nueva ventana de registro, y se encarga de registrar un nuevo usuario.
    '''
    def __init__(self, parent=None, *args, **kwargs):
        '''
        def __init__(self, parent=None, *args, **kwargs):
            Metodo construntor de la clase MainApp, que hereda de QMainWindow almecenar todos los valores  de la ventana mediante funciones de la clase QmainWindow.
        '''
        super(MainApp, self).__init__(parent=parent)
        self.setMinimumSize(400, 500)
        self.setMaximumSize(400,550)
        self.setWindowTitle('Login ')
        #========================= Atributos/priedades para el widget principal  =========================
        '''
        Creamos los laber("Mensajes por pantalla"), dentro de la clase MainApp.
        '''
        width=self.frameGeometry().width()
        height=self.frameGeometry().height()
        
        #=========================Atributos para el  los label Iniciar Sesión ==========================
        labelTitulo=QLabel("I n i c i a r   S e s i ó n ", self)
        labelTitulo.setGeometry(0,30, width, 40)
        labelTitulo.setAlignment(Qt.AlignCenter)
        labelTitulo.setFont(QFont("Stencil", 15))
    
        #=========================Atributos para el  los label Usuario ==========================
        labelUsuario=QLabel("U s u a r i o", self)
        labelUsuario.setGeometry(40,110, 100, 40)
        labelUsuario.setAlignment(Qt.AlignCenter)
        labelUsuario.setFont(QFont("Stencil", 10))
        labelUsuario.setStyleSheet("color:black")

        #=========================Atributos para el  los label contraseña ==========================
        labelContraseña=QLabel("C o n t r a s e ñ a", self)
        labelContraseña.setGeometry(9,210, 200, 40)
        labelContraseña.setAlignment(Qt.AlignCenter)
        labelContraseña.setFont(QFont("Stencil", 10))
        labelContraseña.setStyleSheet("color:black")
        #=========================Atributos para el label "contraseña incorrecta"==========================
        self.labelContraseñaIncorrecta=QLabel("", self)            
        #==========================Atributos para la caja de texto Usuario=========================
        self.cajaUsuario=QLineEdit(self)
        self.cajaUsuario.setGeometry(60,150, 300, 30)
        self.cajaUsuario.setTextMargins(20, 0, 4, 1)
        self.cajaUsuario.setFont(QFont("Yu Gothic Medium", 10))
        self.cajaUsuario.setStyleSheet("border-radius:10px; border:1px solid #D1A5A5;")
        self.cajaUsuario.setToolTip("Ingrese su usuario")
        #==========================Atributos para la caja de texto contraseaña=========================
        self.cajaContraseña=QLineEdit(self)
        self.cajaContraseña.setGeometry(60,250, 300, 30)
        self.cajaContraseña.setTextMargins(20, 0, 4, 1)
        self.cajaContraseña.setFont(QFont("Yu Gothic Medium", 6))
        self.cajaContraseña.setEchoMode(QLineEdit.Password)
        self.cajaContraseña.setStyleSheet("border-radius:10px; border:1px solid #D1A5A5;")
        self.cajaContraseña.setToolTip("Ingrese constraseña")
        #=========================Atributos para botón Iniciar Sesión==========================
        iniciarSesion=QPushButton("Iniciar Sesion", self)
        iniciarSesion.setGeometry(90,350, 220, 40)
        iniciarSesion.setFont(QFont("Stencil", 10))
        iniciarSesion.setStyleSheet("""QPushButton {background:#EC3333;color:#fff; border-radius:10px; }QPushButton:hover {background:#D90808; color:black;}""")
        #=========================Atributos para botón Iniciar Sesión==========================
        registrarse=QPushButton("Registrarse", self)
        registrarse.setGeometry(90,400, 220, 40)
        registrarse.setFont(QFont("Stencil", 10))
        registrarse.setStyleSheet("""QPushButton {background:#EC3333;color:#fff; border-radius:10px; }QPushButton:hover {background:#D90808; color:black;}""")
        #usar el hover para cambiar el color del boton
        
        #=========================Acciones de los botones==========================
        iniciarSesion.clicked.connect(self.iniciarSesion)
        registrarse.clicked.connect(self.registrar)
        #=========================Slots de las botones==========================
    def iniciarSesion(self):
        '''
        def iniciarSesion(self):
            Slot que se encarga de iniciar sesion, recibe el usuario y contraseña, y verifica si existe en la base de datos al precionar el botón inicar sesión.
        '''
        usuario=self.cajaUsuario.text()
        contraseña=self.cajaContraseña.text()
        if Usuarios.inciar(usuario, contraseña)==True:
        #Abrir el ejecutable de la interfazCallCenter
            pass           
        else:
            self.labelContraseñaIncorrecta.setText("USUARIO  O  CONTRASEÑA  INCORRECTA")
            self.labelContraseñaIncorrecta.setGeometry(75,300, 250, 40)
            self.labelContraseñaIncorrecta.setAlignment(Qt.AlignCenter)
            self.labelContraseñaIncorrecta.setFont(QFont("Stencil", 10))
            self.labelContraseñaIncorrecta.setStyleSheet("color:red")
    def registrar(self):
        self.app2= QApplication([])
        self.windows=MainApp2()
        self.windows.show()
        self.app2.exec_()
        self.close()