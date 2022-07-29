
from PyQt5.QtWidgets import* 
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from clases import*
from InterfazLogin import VentanaLogin
from Validaciones.validaciones import *
class ventanaRegistro(QMainWindow):
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
        super(ventanaRegistro, self).__init__(parent=parent, *args, **kwargs, )
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

        self.labelError=QLabel("", self)
        self.labelError.setGeometry(0,235+75+75+75+37, width, 40)
        self.labelError.setAlignment(Qt.AlignCenter)
        self.labelError.setFont(QFont("Stencil", 10))
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
    def registroInterfaz(self):
        '''
        Def registroInterfaz(self):
            Slot para registrar un nuevo usuario, obteniendo los datos de los campos de texto ingresados mediante la interfaz y almacennado en 
            una variable cada tipo de dato, al cual servirá pasarlo como parámetro al objeto usuarioNuevo

        '''   
        #==========================Validación de usuario==========================     
        if validarCaracteres(self.cajaUsuario.text())==True:
            usuario=self.cajaUsuario.text()                
        else:
            self.cajaUsuario.setText("Usuario no valido")
            self.cajaUsuario.setStyleSheet("color:red")
        #==========================Validación de contraseña==========================     
        if validarContraseña(self.cajaContraseña.text())==True:
            contraseña=self.cajaContraseña.text()                
        else:
            self.cajaContraseña.setText("Contraseña no valida")
            self.cajaContraseña.setStyleSheet("color:red")
        #==========================Validación del nombre==========================     
        if validarCaracteres(self.cajaNombre.text())==True:
            nombre=self.cajaNombre.text()                    
        else:
            self.cajaNombre.setText("Nombre no valido")
            self.cajaNombre.setStyleSheet("color:red")
        #==========================Validación del apellido==========================     
        if validarCaracteres(self.cajaApellido.text())==True:
            apellido=self.cajaApellido.text()
        else:
            self.cajaApellido.setText("Apellido no valido")
            self.cajaApellido.setStyleSheet("color:red")
        #==========================Validación del Email==========================     
        if validarEmail(self.cajaEmail.text())==True:
            email=self.cajaEmail.text()
        else:
            self.cajaEmail.setText("Email no valido")
            self.cajaEmail.setStyleSheet("color:red")
        #==========================Validación de la cédula==========================
        if validarNumero(self.cajaCedula.text())==True:
            cedula=self.cajaCedula.text()
        else:
            self.cajaCedula.setText("Cedula no valida")
            self.cajaCedula.setStyleSheet("color:red")
        try:
            '''
            try:
                Se intenta crear un objeto usuarioNuevo, con los datos ingresados en los campos de texto ya validados y guardarlos en la base de datos
            except:
                Si no se puede crear el objeto, se muestra un mensaje de error en la interfaz
            '''
            usuarioNuevo=Usuarios(usuario,contraseña,nombre,apellido,email,cedula)
            documentoRegistro={"usuario":usuarioNuevo.usuario, "contraseña":usuarioNuevo.contraseña, "nombre":usuarioNuevo.nombre, "apellido":usuarioNuevo.apellido, "email":usuarioNuevo.email, "cedula":usuarioNuevo.cedula}
            guardarEnColeccion(documentoRegistro)
            self.labelError.setText("Se  ha  registrado  correctamente")
            self.labelError.setGeometry(0,235+75+75+75+37, 400, 40)
            self.labelError.setAlignment(Qt.AlignCenter)
            self.labelError.setFont(QFont("Stencil", 10))
            self.labelError.setStyleSheet("color:black")
        except:
            self.labelError.setText("No  se  ha  podido  registrar")
            self.labelError.setGeometry(0,235+75+75+75+37, 400, 40)
            self.labelError.setAlignment(Qt.AlignCenter)
            self.labelError.setFont(QFont("Stencil", 10))
            self.labelError.setStyleSheet("color:black") 
    def Volverlogin(self):
        '''
        def Volverlogin(self):
            Slot para volver a la interfaz de login
        '''
        print("VOLVIÓ AL LOGIN")
        self.app3= QApplication([])
        self.window3=VentanaLogin()
        self.window3.show()
        self.app3.exec_()
        self.close()
       
        
        #Llamamos al main para volver a la interfaz de login          
if __name__=="__main__":
    '''
    if __name__=="__main__":
        Main del programa, se encarga de crear la ventana principal, y ejecutar la primera interfaz "Login".
        El cual es la que se encarga de iniciar sesión o registrarse, para los administradores del callcenter.
    '''
           
                
                    
                        
                            



            

