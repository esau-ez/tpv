from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QMainWindow, QApplication,QWidget
from PySide6.QtCore import Qt
from interfaces.ui_login import Ui_Form
from interfaces.ui_main import Ui_MainWindow
from interfaces.ui_dialogo import Ui_Form2
from requests import consulta, add, delete
from dotenv import load_dotenv
import sys
import os
import cups
load_dotenv()
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
        self.dialogo = Dialog()
        self.venta_potencial = []
        self.contador_venta = 0
        #Configuración de boton-pantalla barra lateral 1
        self.pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.vender))
        #botones-vender
        self.pushButton_6.clicked.connect(self.venderProductos)
        self.pushButton_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.devolver))
        self.pushButton_3.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Inventario))
        self.pushButton_4.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.estadistica))
        #Configuración de boton-pantalla sub barra lateral (Inventario)
        self.pushButton_8.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.agregar))
        self.pushButton_15.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.modificar))
        self.pushButton_17.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.eliminar))
        self.pushButton_18.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.ConsultarProducto))
    def venderProductos(self):
        def generar_ticket_txt(nombre_archivo, productos):
            ticket= [
                f"{os.getenv('COMPANYNAME')}",
                f"{os.getenv('COMPANYADRESS')}",
                f"{os.getenv('COMPANYCODE')}",
                f"\n"
                f"\n"
                "Productos\n"
                f"{str(productos)}\n",
                f"Total: $45.00",
                f"Metodo de pago: Tarjeta"
                f"\nGRACIAS POR SU COMPRA\n"
                "\n",
                "\n",
                "\n",
                "\n",
            ]

            # Escribir el contenido en un archivo de texto
            with open(nombre_archivo, 'w') as file:
                for linea in ticket:
                    file.write(linea + '\n')

        # Generar el ticket en formato TXT y guardarlo como "ticket.txt"
        productos = "Camarones filadelfinaos 3.45€\nCamarones popurri 5.60€"
        generar_ticket_txt("ticket.txt",productos)
  
        try:
            texto = "ticket.txt"
            conn = cups.Connection()
            impresoras = conn.getPrinters()

            if "Esau" in impresoras:
                impresora_uri = impresoras["Esau"]["device-uri"]
                conn.printFile("Esau", texto, "Test Print", {})
                print(f"El texto se ha enviado a la impresora .")
            else:
                print(f"No se encontró la impresora .")
        except Exception as e:
            print("Error al imprimir:", e)        #Variables generales de la función
        producto_actual = []
        ean = self.lineEdit.text()
        self.lineEdit.clear()
        self.venta_potencial.append(ean)
        cursor = consulta(f"SELECT nombre, precio FROM products WHERE ean = {ean}")
        for producto in cursor:
            nombre = producto[0].title()  # Convertimos el nombre a mayúscula la primera letra
            precio = str(producto[1]).title()  # Convertimos el precio a cadena y lo capitalizamos
            producto_actual.append({'nombre': nombre, 'precio': precio})

        if producto_actual:
            for data in producto_actual:
                self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)  # Agrega una fila a la tabla
                row = self.tableWidget.rowCount() - 1  # Obtén el índice de la fila recién agregada
                item_nombre = QtWidgets.QTableWidgetItem(data['nombre'])
                item_nombre.setTextAlignment(QtCore.Qt.AlignCenter)  # Centrar el texto en la celda
                self.tableWidget.setItem(row, 0, item_nombre)
                item_precio = QtWidgets.QTableWidgetItem(data['precio'])
                item_precio.setTextAlignment(QtCore.Qt.AlignCenter)  # Centrar el texto en la celda
                self.tableWidget.setItem(row, 1, item_precio)
                item_cantidad = QtWidgets.QTableWidgetItem("1")
                item_cantidad.setTextAlignment(QtCore.Qt.AlignCenter)  # Centrar el texto en la celda
                self.tableWidget.setItem(row, 2, item_cantidad)
        else:
            self.dialogo.label.setText("No se ha encontrado el producto")
            self.dialogo.show()
        print(self.venta_potencial)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Home()
    login = Login()
    window.show()
    sys.exit(app.exec())