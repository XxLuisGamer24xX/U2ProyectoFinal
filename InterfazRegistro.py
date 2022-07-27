
from PyQt5.QtWidgets import* 
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from clases import*
from InterfazLogin import *
class MainApp2(QMainWindow):
    '''
    class MainApp2(QMainWindow):
        clase MainApp2, que hereda de QMainWindow almecenar todos los valores  de la ventana mediante funciones de la clase QmainWindow.
    '''
    def __init__(self, parent=None, *args, **kwargs):
        '''
        def __init__(self, parent=None, *args, **kwargs):
            Metodo construntor de la clase MainApp, que hereda de QMainWindow almecenar todos los valores  de la ventana mediante funciones de la clase QmainWindow.
        '''
        #========================= Atributosde del widget central =========================
        super(MainApp2, self).__init__(parent=parent)
        self.setMinimumSize(400, 700)
        self.setMaximumSize(400,550)
        self.setWindowTitle('Registro de usuarios ')
        '''
        Creamos los label("Mensajes por pantalla"), dentro de la clase MainApp.
        '''
        width=self.frameGeometry().width()
        #=========================Propiedades label Registro de Usuarios ==========================
        labelTitulo=QLabel("R e g i s t r o   d e   u s u a r i o s", self)
        labelTitulo.setGeometry(0,10, width, 40)
        labelTitulo.setAlignment(Qt.AlignCenter)
        labelTitulo.setFont(QFont("Stencil", 15))
    
        #=========================Propiedades label Registro de Usuarios ==========================
        labelUsuario=QLabel("U s u a r i o", self)
        labelUsuario.setGeometry(40,50, 100, 40)
        labelUsuario.setAlignment(Qt.AlignCenter)
        labelUsuario.setFont(QFont("Stencil", 10))
        labelUsuario.setStyleSheet("color:black")

        #=========================Atributos label Registro de Contraseña ==========================
        labelContraseña=QLabel("C o n t r a s e ñ a", self)
        labelContraseña.setGeometry(9,125, 200, 40)
        labelContraseña.setAlignment(Qt.AlignCenter)
        labelContraseña.setFont(QFont("Stencil", 10))
        labelContraseña.setStyleSheet("color:black")
        #=========================Atributos label Registro de Usuario ==========================
        labelNombre=QLabel("N o m b r e ", self)
        labelNombre.setGeometry(39,200, 100, 40)
        labelNombre.setAlignment(Qt.AlignCenter)
        labelNombre.setFont(QFont("Stencil", 10))
        labelNombre.setStyleSheet("color:black")
        #=========================Atributos label Registro de contrseña ==========================
        labelApellido=QLabel("A p e l l i d o", self)
        labelApellido.setGeometry(2,200+75, 180, 40)
        labelApellido.setAlignment(Qt.AlignCenter)
        labelApellido.setFont(QFont("Stencil", 10))
        labelApellido.setStyleSheet("color:black")
        #=========================Atributos label Registro de Email ========================== 
        labelEmail=QLabel("E m a i l", self)
        labelEmail.setGeometry(30,200+150, 100, 40)
        labelEmail.setAlignment(Qt.AlignCenter)
        labelEmail.setFont(QFont("Stencil", 10))
        labelEmail.setStyleSheet("color:black")
        #=========================Atributos label Registro de Cédula ==========================
        labelCedula=QLabel("C é d u l a", self)
        labelCedula.setGeometry(40,200+150+75, 100, 40)
        labelCedula.setAlignment(Qt.AlignCenter)
        labelCedula.setFont(QFont("Stencil", 10))
        labelCedula.setStyleSheet("color:black")
        #==========================Atributos de ingreso de Usuario==========================
        self.cajaUsuario=QLineEdit(self)
        self.cajaUsuario.setGeometry(60,85, 300, 30)
        self.cajaUsuario.setTextMargins(20, 0, 4, 1)
        self.cajaUsuario.setFont(QFont("Bookman Old Style", 10))
        self.cajaUsuario.setStyleSheet("border-radius:10px; border:1px solid #D1A5A5;")
        self.cajaUsuario.setToolTip("Ingrese su usuario")
        #==========================Atributos de ingreso de Contraseña==========================
        self.cajaContraseña=QLineEdit(self)
        self.cajaContraseña.setGeometry(60,160, 300, 30)
        self.cajaContraseña.setTextMargins(20, 0, 4, 1)
        self.cajaContraseña.setFont(QFont("Bookman Old Style", 10))
        self.cajaContraseña.setStyleSheet("border-radius:10px; border:1px solid #D1A5A5;")
        self.cajaContraseña.setToolTip("Ingrese su constraseña")
        #==========================Atributos de ingreso de Nombre==========================
        self.cajaNombre=QLineEdit(self)
        self.cajaNombre.setGeometry(60,235, 300, 30)
        self.cajaNombre.setTextMargins(20, 0, 4, 1)
        self.cajaNombre.setFont(QFont("Bookman Old Style", 10))
        self.cajaNombre.setStyleSheet("border-radius:10px; border:1px solid #D1A5A5;")
        self.cajaNombre.setToolTip("Ingrese su nombre")
        #==========================Atributos de ingreso de Apellido==========================
        self.cajaApellido=QLineEdit(self)
        self.cajaApellido.setGeometry(60,235+75, 300, 30)
        self.cajaApellido.setTextMargins(20, 0, 4, 1)
        self.cajaApellido.setFont(QFont("Bookman Old Style", 10))
        self.cajaApellido.setStyleSheet("border-radius:10px; border:1px solid #D1A5A5;")
        self.cajaApellido.setToolTip("Ingrese su Apellido")
        #==========================Atributos de ingreso de Email==========================
        self.cajaEmail=QLineEdit(self)
        self.cajaEmail.setGeometry(60,235+75+75, 300, 30)
        self.cajaEmail.setTextMargins(20, 0, 4, 1)
        self.cajaEmail.setFont(QFont("Bookman Old Style", 10))
        self.cajaEmail.setStyleSheet("border-radius:10px; border:1px solid #D1A5A5;")
        self.cajaEmail.setToolTip("Ingrese su Email")
        #==========================Atributos de ingreso de Cédula==========================
        self.cajaCedula=QLineEdit(self)
        self.cajaCedula.setGeometry(60,235+75+75+75, 300, 30)
        self.cajaCedula.setTextMargins(20, 0, 4, 1)
        self.cajaCedula.setFont(QFont("Bookman Old Style", 10))
        self.cajaCedula.setStyleSheet("border-radius:10px; border:1px solid #D1A5A5;")
        self.cajaCedula.setToolTip("Ingrese su cédula")
        #=========================Propiedades del botón Iniciar Sesión==========================
        iniciarSesion=QPushButton("Iniciar Sesion", self)
        iniciarSesion.setGeometry(90,550, 220, 40)
        iniciarSesion.setFont(QFont("Stencil", 10))
        iniciarSesion.setStyleSheet("""QPushButton {background:#EC3333;color:#fff; border-radius:10px; }QPushButton:hover {background:#D90808; color:black;}""")
        #=========================Propiedades del botón registrar==========================
        registrarse=QPushButton("Registrarse", self)
        registrarse.setGeometry(90,600, 220, 40)
        registrarse.setFont(QFont("Stencil", 10))
        registrarse.setStyleSheet("""QPushButton {background:#EC3333;color:#fff; border-radius:10px; }QPushButton:hover {background:#D90808; color:black;}""")
        #=========================Acciones de los botones==========================
        registrarse.clicked.connect(self.registroInterfaz)
        iniciarSesion.clicked.connect(self.Volverlogin)
    def Volverlogin(self):
        '''
        def Volverlogin(self):
            Slot para volver a la interfaz de login
        '''
        self.app= QApplication([])
        self.windows=MainApp3()
        self.windows.show()
        self.app.exec_()
        self.close()
    def registroInterfaz(self):
        '''
        Def registroInterfaz(self):
            Slot para registrar un nuevo usuario, obteniendo los datos de los campos de texto ingresados mediante la interfaz y almacennado en 
            una variable cada tipo de dato, al cual servirá pasarlo como parámetro al objeto usuarioNuevo
        '''
        usuario=self.cajaUsuario.text()
        contraseña=self.cajaContraseña.text()
        nombre=self.cajaNombre.text()
        apellido=self.cajaApellido.text()
        email=self.cajaEmail.text()
        cedula=self.cajaCedula.text()
        '''
        Instanciamiento de la clase  Usuario, para crear un objeto de usuario de tipo Usuarios
        Parametros:
        -------------------------------
            usuario: nombre de usuario
            contraseña: contraseña del usuario
            nombre: nombre del usuario
            apellido: apellido del usuario
            email: email del usuario
            cedula: cedula del usuario            
        '''
        usuarioNuevo=Usuarios(usuario,contraseña, nombre, apellido, email, cedula)
        documentoRegistro={"usuario":usuarioNuevo.usuario, "contraseña":usuarioNuevo.contraseña, "nombre":usuarioNuevo.nombre, "apellido":usuarioNuevo.apellido, "email":usuarioNuevo.email, "cedula":usuarioNuevo.cedula}
        guardarEnColeccion(documentoRegistro)
        print("===================================================")
        print("Usuario Registrado Correctamente")
        print("===================================================")