from PySide6.QtWidgets import QMainWindow, QApplication,QWidget
from interfaces.ui_login import Ui_Form
from interfaces.ui_main import Ui_MainWindow
import sys
class Login(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #Buttons configuration
        self.pushButton.clicked.connect(self.close)
        self.switchButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.register_2))
        self.switchButton_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.login))
class Home(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #Configuración de boton-pantalla barra lateral 1
        self.pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.vender))
        self.pushButton_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.devolver))
        self.pushButton_3.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Inventario))
        self.pushButton_4.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.estadistica))
        #Configuración de boton-pantalla sub barra lateral (Inventario)
        self.pushButton_8.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.agregar))
        self.pushButton_15.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.modificar))
        self.pushButton_17.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.eliminar))
        self.pushButton_18.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.ConsultarProducto))
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Home()
    window.show()
    sys.exit(app.exec())