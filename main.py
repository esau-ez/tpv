from PySide6.QtWidgets import QMainWindow, QApplication,QWidget
from interfaces.ui_login import Ui_Form
from interfaces.ui_main import Ui_MainWindow
from interfaces.ui_dialogo import Ui_Form2
from requests import consulta, add, delete
from dotenv import load_dotenv
import sys
class Dialog(QWidget, Ui_Form2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.close)
class Login(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.home = Home()
        self.dialogo = Dialog()
        #Buttons configuration
        self.pushButton.clicked.connect(self.close)
        self.pushButton_2.clicked.connect(self.login)
    def login(self):
        email = self.lineEdit.text()
        password = self.lineEdit_2.text()
        query=f"SELECT password FROM users WHERE email='{email}'"
        response = consulta(query)
        for tupla in response:
            for a in tupla:
                resultado = a
        if response:
            # Verificar si la contraseña coincide
            if password == resultado:
                query = f"SELECT username FROM users WHERE email='{email}'"
                response = consulta(query)
                for tupla in response:
                    for a in tupla:
                        self.username = a
                global username
                username = self.username
                self.home.label_7.setText(str(email))
                query = f"SELECT username FROM users WHERE email='{email}'"
                response = consulta(query)
                for tupla in response:
                    for a in tupla:
                        self.username = a
                self.home.label_6.setText(self.username)
                self.close()
                self.home.show()
                self.lineEdit.clear()
                self.lineEdit_2.clear()
            else:
                self.dialogo.label.setText("Usuario o contraseña incorrecto")
                self.dialogo.show()
                self.lineEdit.clear()
                self.lineEdit_2.clear()
        else:
            self.dialogo.label.setText("Usuario o contraseña incorrecto")
            self.dialogo.show()
            self.lineEdit.clear()
            self.lineEdit_2.clear()
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
    login = Login()
    login.show()
    sys.exit(app.exec())