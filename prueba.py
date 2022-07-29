from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("Hola mundo")
        self.setFixedSize(400, 200)
        self.button = QPushButton(self, text="Mostrar diálogo")
        self.button.clicked.connect(self.show_dialog)
    def show_dialog(self):
        dialog = Dialog(self)  # self hace referencia al padre
        dialog.show()
class Dialog(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Dialog, self).__init__(*args, **kwargs)
        self.setWindowTitle("Soy un popup")
        self.setFixedSize(200, 100)
if __name__ == "__main__":  
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()