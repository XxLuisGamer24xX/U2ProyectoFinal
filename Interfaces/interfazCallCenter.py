from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *
import sys
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


from pip import main
class Ui_MainWindow(object):
    '''
    class Ui_Buscar(object):
        clase que contiene los elementos de la interfaz de buscar
    '''
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 10, 781, 571))
        self.Buscar = QWidget()
        self.Buscar.setObjectName(u"Buscar")
        self.TablaBusqueda = QTableWidget(self.Buscar)
        if (self.TablaBusqueda.columnCount() < 5):
            self.TablaBusqueda.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.TablaBusqueda.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.TablaBusqueda.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.TablaBusqueda.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.TablaBusqueda.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.TablaBusqueda.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.TablaBusqueda.setObjectName(u"TablaBusqueda")
        self.TablaBusqueda.setGeometry(QRect(70, 180, 641, 181))
        font = QFont()
        font.setFamily(u"Tahoma")
        font.setBold(True)
        font.setWeight(75)
        self.TablaBusqueda.setFont(font)
        self.BotonBuscar = QPushButton(self.Buscar)
        self.BotonBuscar.setObjectName(u"BotonBuscar")
        self.BotonBuscar.setGeometry(QRect(270, 460, 231, 31))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.BotonBuscar.setFont(font1)
        self.BotonBuscar.setStyleSheet(u"QPushButton{\n"
"	color:#fff;\n"
"	border-radius:10px;\n"
"	background:#EC3333\n"
"	\n"
"}\n"
"QPushButthon{\n"
"	color:black;\n"
"	background:#D90808\n"
"}")
        self.LabelBuscarNombre = QLabel(self.Buscar)
        self.LabelBuscarNombre.setObjectName(u"LabelBuscarNombre")
        self.LabelBuscarNombre.setGeometry(QRect(80, 70, 131, 31))
        self.LabelBuscarNombre.setFont(font1)
        self.cajaId_2 = QLineEdit(self.Buscar)
        self.cajaId_2.setObjectName(u"cajaId_2")
        self.cajaId_2.setGeometry(QRect(210, 70, 351, 31))
        self.cajaId_2.setFont(font1)
        self.cajaId_2.setStyleSheet(u"QLineEdit{\n"
"	color:red;\n"
"	border-radius:10px;\n"
"	border:1px solid black\n"
"	\n"
"}\n"
"")
        self.NombreAdmin = QLabel(self.Buscar)
        self.NombreAdmin.setObjectName(u"NombreAdmin")
        self.NombreAdmin.setGeometry(QRect(10, 10, 151, 31))
        font2 = QFont()
        font2.setPointSize(9)
        font2.setBold(True)
        font2.setWeight(75)
        self.NombreAdmin.setFont(font2)
        self.NombreAdmin_2 = QLabel(self.Buscar)
        self.NombreAdmin_2.setObjectName(u"NombreAdmin_2")
        self.NombreAdmin_2.setGeometry(QRect(170, 10, 111, 31))
        self.NombreAdmin_2.setFont(font2)
        self.NombreAdmin_2.setStyleSheet(u"QLineEdit{\n"
"	color:red;\n"
"	border-radius:10px;\n"
"	border:1px solid black\n"
"	\n"
"}\n"
"")
        self.IAdmin = QLabel(self.Buscar)
        self.IAdmin.setObjectName(u"IAdmin")
        self.IAdmin.setGeometry(QRect(440, 10, 201, 31))
        self.IAdmin.setFont(font2)
        self.IAdmin.setStyleSheet(u"QLineEdit{\n"
"	color:red;\n"
"	border-radius:10px;\n"
"	border:1px solid black\n"
"	\n"
"}\n"
"")
        self.IdAdministrador = QLabel(self.Buscar)
        self.IdAdministrador.setObjectName(u"IdAdministrador")
        self.IdAdministrador.setGeometry(QRect(310, 10, 121, 31))
        self.IdAdministrador.setFont(font2)
        self.tabWidget.addTab(self.Buscar, "")
        self.aniadir = QWidget()
        self.aniadir.setObjectName(u"aniadir")
        self.BotonSituacion = QPushButton(self.aniadir)
        self.BotonSituacion.setObjectName(u"BotonSituacion")
        self.BotonSituacion.setGeometry(QRect(290, 440, 231, 31))
        self.BotonSituacion.setFont(font1)
        self.BotonSituacion.setStyleSheet(u"QPushButton{\n"
"	color:#fff;\n"
"	border-radius:10px;\n"
"	background:#EC3333\n"
"	\n"
"}\n"
"QPushButthon{\n"
"	color:black;\n"
"	background:#D90808\n"
"}")
        self.label = QLabel(self.aniadir)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 30, 91, 41))
        self.label.setFont(font1)
        self.label_2 = QLabel(self.aniadir)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(140, 80, 91, 41))
        self.label_2.setFont(font1)
        self.label_3 = QLabel(self.aniadir)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(140, 130, 91, 41))
        self.label_3.setFont(font1)
        self.label_4 = QLabel(self.aniadir)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(140, 180, 91, 41))
        self.label_4.setFont(font1)
        self.label_5 = QLabel(self.aniadir)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(140, 230, 81, 41))
        self.label_5.setFont(font1)
        self.cajaApellido = QLineEdit(self.aniadir)
        self.cajaApellido.setObjectName(u"cajaApellido")
        self.cajaApellido.setGeometry(QRect(240, 90, 351, 31))
        self.cajaApellido.setStyleSheet(u"QLineEdit{\n"
"	color:red;\n"
"	border-radius:10px;\n"
"	border:1px solid black\n"
"	\n"
"}\n"
"")
        self.cajaNombre = QLineEdit(self.aniadir)
        self.cajaNombre.setObjectName(u"cajaNombre")
        self.cajaNombre.setGeometry(QRect(240, 140, 351, 31))
        self.cajaNombre.setStyleSheet(u"QLineEdit{\n"
"	color:red;\n"
"	border-radius:10px;\n"
"	border:1px solid black\n"
"	\n"
"}\n"
"")
        self.cajaTelefono = QLineEdit(self.aniadir)
        self.cajaTelefono.setObjectName(u"cajaTelefono")
        self.cajaTelefono.setGeometry(QRect(240, 190, 351, 31))
        self.cajaTelefono.setStyleSheet(u"QLineEdit{\n"
"	color:red;\n"
"	border-radius:10px;\n"
"	border:1px solid black\n"
"	\n"
"}\n"
"")
        self.cajaDireccion = QLineEdit(self.aniadir)
        self.cajaDireccion.setObjectName(u"cajaDireccion")
        self.cajaDireccion.setGeometry(QRect(240, 240, 351, 31))
        self.cajaDireccion.setStyleSheet(u"QLineEdit{\n"
"	color:red;\n"
"	border-radius:10px;\n"
"	border:1px solid black\n"
"	\n"
"}\n"
"")
        self.label_6 = QLabel(self.aniadir)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(140, 280, 81, 41))
        self.label_6.setFont(font1)
        self.cajaSituacion = QLineEdit(self.aniadir)
        self.cajaSituacion.setObjectName(u"cajaSituacion")
        self.cajaSituacion.setGeometry(QRect(240, 290, 351, 31))
        self.cajaSituacion.setStyleSheet(u"QLineEdit{\n"
"	color:red;\n"
"	border-radius:10px;\n"
"	border:1px solid black\n"
"	\n"
"}\n"
"")
        self.cajaId = QLineEdit(self.aniadir)
        self.cajaId.setObjectName(u"cajaId")
        self.cajaId.setGeometry(QRect(240, 40, 351, 31))
        self.cajaId.setFont(font1)
        self.cajaId.setStyleSheet(u"QLineEdit{\n"
"	color:red;\n"
"	border-radius:10px;\n"
"	border:1px solid black\n"
"	\n"
"}\n"
"")
        self.tabWidget.addTab(self.aniadir, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Menu Administradores", None))
        ___qtablewidgetitem = self.TablaBusqueda.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem1 = self.TablaBusqueda.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem2 = self.TablaBusqueda.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Apellido", None));
        ___qtablewidgetitem3 = self.TablaBusqueda.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Telefono", None));
        ___qtablewidgetitem4 = self.TablaBusqueda.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Direccion", None));
        self.BotonBuscar.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.LabelBuscarNombre.setText(QCoreApplication.translate("MainWindow", u"Buscar por Nombre:", None))
        self.NombreAdmin.setText(QCoreApplication.translate("MainWindow", u"Nombre Administrador", None))
        self.NombreAdmin_2.setText("hola")
        self.IAdmin.setText(QCoreApplication.translate("MainWindow", u"asd", None))
        self.IdAdministrador.setText(QCoreApplication.translate("MainWindow", u"ID Administrador:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Buscar), QCoreApplication.translate("MainWindow", u"Buscar Usuario", None))
        self.BotonSituacion.setText("Buscar")

        self.label.setText(QCoreApplication.translate("MainWindow", u"ID/ C\u00e9dula", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Apellido", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Telefono", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Direcci\u00f3n", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Situaci\u00f3n", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.aniadir), QCoreApplication.translate("MainWindow", u"A\u00f1adir Informe", None))
        #======================================Acciones de los botones========================================================
        self.BotonSituacion.clicked.connect(self.buscarSituacion)
    def buscarSituacion(self):
        print("hola")
        id=int(self.cajaId.text())
        print(id)
        self.cajaApellido.setText(buscarId(id)[0]['nombre'])
        self.cajaNombre.setText(buscarId(id)[0]['apellido'])
        self.cajaTelefono.setText(buscarId(id)[0]['telefono'])
        self.cajaDireccion.setText(buscarId(id)[0]['direccion'])
        
def mainCallCenter():
    app3 = QApplication(sys.argv)
    MainWindow4 = QMainWindow()
    ventana4 = Ui_MainWindow()
    ventana4.setupUi(MainWindow4)
    MainWindow4.show()
    app3.exec_()
mainCallCenter()


