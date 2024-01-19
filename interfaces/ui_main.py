# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainmcgwpu.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStackedWidget, QTableWidget, QTableWidgetItem, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1100, 700)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget_5 = QWidget(self.centralwidget)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(0, 0, 331, 700))
        self.widget_5.setStyleSheet(u"background-color: #2b2b2b;\n"
"")
        self.label = QLabel(self.widget_5)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 40, 191, 31))
        font = QFont()
        font.setFamilies([u"Rockwell"])
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.widget_2 = QWidget(self.widget_5)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(30, 20, 61, 61))
        self.widget_2.setStyleSheet(u"image: url(:/login/assets/login/cohete.png);")
        self.pushButton = QPushButton(self.widget_5)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 130, 51, 51))
        self.pushButton.setStyleSheet(u"background-color: #3f4042;")
        icon = QIcon()
        icon.addFile(u":/interfaz /assets/interfaz principal/barra lateral/carro-de-compras-rapido.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(25, 25))
        self.label_2 = QLabel(self.widget_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(90, 140, 191, 31))
        font1 = QFont()
        font1.setFamilies([u"Rockwell"])
        font1.setPointSize(13)
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_2 = QPushButton(self.widget_5)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(30, 210, 51, 51))
        self.pushButton_2.setStyleSheet(u"background-color: #3f4042;")
        icon1 = QIcon()
        icon1.addFile(u":/interfaz /assets/interfaz principal/barra lateral/devolucion-de-dinero.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(40, 40))
        self.label_3 = QLabel(self.widget_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(90, 220, 191, 31))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_3 = QPushButton(self.widget_5)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(30, 290, 51, 51))
        self.pushButton_3.setStyleSheet(u"background-color: #3f4042;")
        icon2 = QIcon()
        icon2.addFile(u":/interfaz /assets/interfaz principal/barra lateral/inventario-disponible.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QSize(30, 30))
        self.label_4 = QLabel(self.widget_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(90, 300, 191, 31))
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_4 = QPushButton(self.widget_5)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(30, 370, 51, 51))
        self.pushButton_4.setStyleSheet(u"background-color: #3f4042;")
        icon3 = QIcon()
        icon3.addFile(u":/interfaz /assets/interfaz principal/barra lateral/tendencia.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QSize(30, 30))
        self.label_5 = QLabel(self.widget_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(90, 380, 191, 31))
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.widget_4 = QWidget(self.widget_5)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(60, 620, 41, 41))
        self.widget_4.setStyleSheet(u"image: url(:/interfaz /assets/interfaz principal/barra lateral/usuario.png);")
        self.label_6 = QLabel(self.widget_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(110, 620, 141, 31))
        font2 = QFont()
        font2.setFamilies([u"Rockwell"])
        font2.setPointSize(11)
        font2.setBold(True)
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_7 = QLabel(self.widget_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(110, 635, 141, 31))
        font3 = QFont()
        font3.setFamilies([u"Rockwell"])
        font3.setPointSize(9)
        font3.setBold(True)
        self.label_7.setFont(font3)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: transparent;")
        self.pushButton_5 = QPushButton(self.widget_5)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(70, 670, 21, 21))
        self.pushButton_5.setStyleSheet(u"background-color: #3f4042;\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/login/assets/login/circulo-marca-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setIconSize(QSize(30, 30))
        self.label_8 = QLabel(self.widget_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(100, 665, 141, 31))
        self.label_8.setFont(font3)
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: transparent;")
        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(289, 0, 811, 700))
        self.widget_3.setStyleSheet(u"background-color: #fafafa;\n"
"border-radius: 40px;")
        self.stackedWidget = QStackedWidget(self.widget_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(40, 29, 741, 641))
        self.stackedWidget.setStyleSheet(u"color: #ffffff;")
        self.vender = QWidget()
        self.vender.setObjectName(u"vender")
        self.lineEdit = QLineEdit(self.vender)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 11, 581, 31))
        self.lineEdit.setStyleSheet(u"background-color: #3f4042;\n"
"color: #ffffff;\n"
"border-radius: 10px;\n"
"padding: 10px;")
        self.lineEdit.setMaxLength(13)
        self.pushButton_6 = QPushButton(self.vender)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(610, 11, 101, 31))
        font4 = QFont()
        font4.setFamilies([u"Rockwell"])
        font4.setPointSize(8)
        font4.setBold(True)
        self.pushButton_6.setFont(font4)
        self.pushButton_6.setStyleSheet(u"background-color: #3f4042;\n"
"border-radius: 10px;")
        self.widget = QWidget(self.vender)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(470, 290, 261, 331))
        self.widget.setStyleSheet(u"background-color: #2b2b2b;\n"
"border-radius: 20px;")
        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 20, 221, 31))
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"background-color: transparent;")
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(30, 80, 101, 31))
        font5 = QFont()
        font5.setFamilies([u"Rockwell"])
        font5.setPointSize(12)
        font5.setBold(True)
        self.label_10.setFont(font5)
        self.label_10.setStyleSheet(u"background-color: transparent;")
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_11 = QLabel(self.widget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(40, 130, 61, 31))
        self.label_11.setFont(font5)
        self.label_11.setStyleSheet(u"background-color: transparent;")
        self.label_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_12 = QLabel(self.widget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(130, 80, 101, 31))
        self.label_12.setFont(font5)
        self.label_12.setStyleSheet(u"background-color: transparent;")
        self.label_12.setAlignment(Qt.AlignCenter)
        self.label_13 = QLabel(self.widget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(100, 130, 101, 31))
        self.label_13.setFont(font5)
        self.label_13.setStyleSheet(u"background-color: transparent;")
        self.label_13.setAlignment(Qt.AlignCenter)
        self.pushButton_7 = QPushButton(self.widget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(50, 280, 161, 24))
        font6 = QFont()
        font6.setFamilies([u"Rockwell"])
        font6.setPointSize(10)
        font6.setBold(True)
        self.pushButton_7.setFont(font6)
        self.pushButton_7.setStyleSheet(u"background-color: #3f4042;")
        self.pushButton_9 = QPushButton(self.widget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(50, 240, 161, 24))
        self.pushButton_9.setFont(font6)
        self.pushButton_9.setStyleSheet(u"background-color: #3f4042;")
        self.label_26 = QLabel(self.widget)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(100, 180, 101, 31))
        self.label_26.setFont(font5)
        self.label_26.setStyleSheet(u"background-color: transparent;")
        self.label_26.setAlignment(Qt.AlignCenter)
        self.label_27 = QLabel(self.widget)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(40, 180, 61, 31))
        self.label_27.setFont(font5)
        self.label_27.setStyleSheet(u"background-color: transparent;")
        self.label_27.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.tableWidget = QTableWidget(self.vender)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tableWidget.rowCount() < 38):
            self.tableWidget.setRowCount(38)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(0, 0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(0, 1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(0, 2, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(25, 71, 701, 211))
        self.tableWidget.setStyleSheet(u"QTableWidget {\n"
"    background-color: #2b2b2b;\n"
"	border-radius: 0px;\n"
"    color: white;\n"
"}\n"
"\n"
"QTableWidget QHeaderView::section {\n"
"    background-color: #2b2b2b;\n"
"    color: white;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"}\n"
"QScrollBar:vertical,\n"
"QScrollBar:horizontal {\n"
"    background-color: #2b2b2b;  /* Color del scrollbar */  /* Borde del scrollbar */\n"
"}\n"
"\n"
"QScrollBar::handle:vertical,\n"
"QScrollBar::handle:horizontal {\n"
"    background-color: #3f4042;  /* Color del \u00e1rea desplazable */\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical,\n"
"QScrollBar::add-line:horizontal,\n"
"QScrollBar::sub-line:horizontal {\n"
"    background-color: #2b2b2b;  /* Color de las \u00e1reas de botones (arriba/abajo o izquierda/derecha) */\n"
"}")
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget.setProperty("showDropIndicator", True)
        self.tableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setRowCount(38)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(234)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", False)
        self.label_14 = QLabel(self.vender)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(130, 291, 221, 31))
        self.label_14.setFont(font1)
        self.label_14.setStyleSheet(u"background-color: transparent;\n"
"color: #2b2b2b;")
        self.label_14.setAlignment(Qt.AlignCenter)
        self.tableWidget_2 = QTableWidget(self.vender)
        if (self.tableWidget_2.columnCount() < 3):
            self.tableWidget_2.setColumnCount(3)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        if (self.tableWidget_2.rowCount() < 38):
            self.tableWidget_2.setRowCount(38)
        font7 = QFont()
        font7.setBold(False)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem9.setFont(font7);
        self.tableWidget_2.setItem(0, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setItem(0, 1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setItem(0, 2, __qtablewidgetitem11)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(30, 331, 431, 291))
        self.tableWidget_2.setStyleSheet(u"QTableWidget {\n"
"    background-color: #2b2b2b;\n"
"	border-radius: 10px;\n"
"    color: white;\n"
"}\n"
"\n"
"QTableWidget QHeaderView::section {\n"
"    background-color: #2b2b2b;\n"
"    color: white;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"}\n"
"QScrollBar:vertical,\n"
"QScrollBar:horizontal {\n"
"    background-color: #2b2b2b;  /* Color del scrollbar */  /* Borde del scrollbar */\n"
"}\n"
"\n"
"QScrollBar::handle:vertical,\n"
"QScrollBar::handle:horizontal {\n"
"    background-color: #3f4042;  /* Color del \u00e1rea desplazable */\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical,\n"
"QScrollBar::add-line:horizontal,\n"
"QScrollBar::sub-line:horizontal {\n"
"    background-color: #2b2b2b;  /* Color de las \u00e1reas de botones (arriba/abajo o izquierda/derecha) */\n"
"}")
        self.tableWidget_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_2.setProperty("showDropIndicator", True)
        self.tableWidget_2.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget_2.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tableWidget_2.setShowGrid(False)
        self.tableWidget_2.setRowCount(38)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(144)
        self.tableWidget_2.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setProperty("showSortIndicator", False)
        self.stackedWidget.addWidget(self.vender)
        self.devolver = QWidget()
        self.devolver.setObjectName(u"devolver")
        self.widget_6 = QWidget(self.devolver)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setGeometry(QRect(475, 290, 261, 331))
        self.widget_6.setStyleSheet(u"background-color: #2b2b2b;\n"
"border-radius: 20px;")
        self.label_21 = QLabel(self.widget_6)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(20, 30, 221, 31))
        self.label_21.setFont(font1)
        self.label_21.setStyleSheet(u"background-color: transparent;")
        self.label_21.setAlignment(Qt.AlignCenter)
        self.label_22 = QLabel(self.widget_6)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(30, 90, 101, 31))
        self.label_22.setFont(font5)
        self.label_22.setStyleSheet(u"background-color: transparent;")
        self.label_22.setAlignment(Qt.AlignCenter)
        self.label_23 = QLabel(self.widget_6)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(40, 140, 61, 31))
        self.label_23.setFont(font5)
        self.label_23.setStyleSheet(u"background-color: transparent;")
        self.label_23.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_24 = QLabel(self.widget_6)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(130, 90, 101, 31))
        self.label_24.setFont(font5)
        self.label_24.setStyleSheet(u"background-color: transparent;")
        self.label_24.setAlignment(Qt.AlignCenter)
        self.label_25 = QLabel(self.widget_6)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(100, 140, 101, 31))
        self.label_25.setFont(font5)
        self.label_25.setStyleSheet(u"background-color: transparent;")
        self.label_25.setAlignment(Qt.AlignCenter)
        self.pushButton_14 = QPushButton(self.widget_6)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setGeometry(QRect(50, 280, 161, 24))
        self.pushButton_14.setFont(font6)
        self.pushButton_14.setStyleSheet(u"background-color: #3f4042;")
        self.pushButton_16 = QPushButton(self.widget_6)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setGeometry(QRect(50, 240, 161, 24))
        self.pushButton_16.setFont(font6)
        self.pushButton_16.setStyleSheet(u"background-color: #3f4042;")
        self.label_28 = QLabel(self.widget_6)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(100, 190, 101, 31))
        self.label_28.setFont(font5)
        self.label_28.setStyleSheet(u"background-color: transparent;")
        self.label_28.setAlignment(Qt.AlignCenter)
        self.label_29 = QLabel(self.widget_6)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(40, 190, 61, 31))
        self.label_29.setFont(font5)
        self.label_29.setStyleSheet(u"background-color: transparent;")
        self.label_29.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_15 = QLabel(self.devolver)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(135, 291, 221, 31))
        self.label_15.setFont(font1)
        self.label_15.setStyleSheet(u"background-color: transparent;\n"
"color: #2b2b2b;")
        self.label_15.setAlignment(Qt.AlignCenter)
        self.tableWidget_4 = QTableWidget(self.devolver)
        if (self.tableWidget_4.columnCount() < 3):
            self.tableWidget_4.setColumnCount(3)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, __qtablewidgetitem14)
        if (self.tableWidget_4.rowCount() < 38):
            self.tableWidget_4.setRowCount(38)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem15.setFont(font7);
        self.tableWidget_4.setItem(0, 0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_4.setItem(0, 1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_4.setItem(0, 2, __qtablewidgetitem17)
        self.tableWidget_4.setObjectName(u"tableWidget_4")
        self.tableWidget_4.setGeometry(QRect(35, 331, 431, 291))
        self.tableWidget_4.setStyleSheet(u"QTableWidget {\n"
"    background-color: #2b2b2b;\n"
"	border-radius: 10px;\n"
"    color: white;\n"
"}\n"
"\n"
"QTableWidget QHeaderView::section {\n"
"    background-color: #2b2b2b;\n"
"    color: white;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"}\n"
"QScrollBar:vertical,\n"
"QScrollBar:horizontal {\n"
"    background-color: #2b2b2b;  /* Color del scrollbar */  /* Borde del scrollbar */\n"
"}\n"
"\n"
"QScrollBar::handle:vertical,\n"
"QScrollBar::handle:horizontal {\n"
"    background-color: #3f4042;  /* Color del \u00e1rea desplazable */\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical,\n"
"QScrollBar::add-line:horizontal,\n"
"QScrollBar::sub-line:horizontal {\n"
"    background-color: #2b2b2b;  /* Color de las \u00e1reas de botones (arriba/abajo o izquierda/derecha) */\n"
"}")
        self.tableWidget_4.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_4.setProperty("showDropIndicator", True)
        self.tableWidget_4.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget_4.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tableWidget_4.setShowGrid(False)
        self.tableWidget_4.setRowCount(38)
        self.tableWidget_4.horizontalHeader().setDefaultSectionSize(144)
        self.tableWidget_4.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_4.verticalHeader().setVisible(False)
        self.tableWidget_4.verticalHeader().setProperty("showSortIndicator", False)
        self.pushButton_10 = QPushButton(self.devolver)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(610, 11, 101, 31))
        self.pushButton_10.setFont(font4)
        self.pushButton_10.setStyleSheet(u"background-color: #3f4042;\n"
"border-radius: 10px;")
        self.lineEdit_3 = QLineEdit(self.devolver)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(20, 11, 581, 31))
        self.lineEdit_3.setStyleSheet(u"background-color: #3f4042;\n"
"color: #ffffff;\n"
"border-radius: 10px;\n"
"padding: 10px;")
        self.lineEdit_3.setMaxLength(13)
        self.tableWidget_3 = QTableWidget(self.devolver)
        if (self.tableWidget_3.columnCount() < 3):
            self.tableWidget_3.setColumnCount(3)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem20)
        if (self.tableWidget_3.rowCount() < 38):
            self.tableWidget_3.setRowCount(38)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_3.setItem(0, 0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_3.setItem(0, 1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_3.setItem(0, 2, __qtablewidgetitem23)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setGeometry(QRect(30, 71, 701, 211))
        self.tableWidget_3.setStyleSheet(u"QTableWidget {\n"
"    background-color: #2b2b2b;\n"
"	border-radius: 0px;\n"
"    color: white;\n"
"}\n"
"\n"
"QTableWidget QHeaderView::section {\n"
"    background-color: #2b2b2b;\n"
"    color: white;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"}\n"
"QScrollBar:vertical,\n"
"QScrollBar:horizontal {\n"
"    background-color: #2b2b2b;  /* Color del scrollbar */  /* Borde del scrollbar */\n"
"}\n"
"\n"
"QScrollBar::handle:vertical,\n"
"QScrollBar::handle:horizontal {\n"
"    background-color: #3f4042;  /* Color del \u00e1rea desplazable */\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical,\n"
"QScrollBar::add-line:horizontal,\n"
"QScrollBar::sub-line:horizontal {\n"
"    background-color: #2b2b2b;  /* Color de las \u00e1reas de botones (arriba/abajo o izquierda/derecha) */\n"
"}")
        self.tableWidget_3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_3.setProperty("showDropIndicator", True)
        self.tableWidget_3.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget_3.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tableWidget_3.setShowGrid(False)
        self.tableWidget_3.setRowCount(38)
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(234)
        self.tableWidget_3.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_3.verticalHeader().setVisible(False)
        self.tableWidget_3.verticalHeader().setProperty("showSortIndicator", False)
        self.stackedWidget.addWidget(self.devolver)
        self.Inventario = QWidget()
        self.Inventario.setObjectName(u"Inventario")
        self.widget_7 = QWidget(self.Inventario)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setGeometry(QRect(10, 0, 211, 641))
        self.widget_7.setStyleSheet(u"background-color: #2b2b2b;\n"
"color:#ffffff")
        self.pushButton_8 = QPushButton(self.widget_7)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(10, 110, 51, 51))
        self.pushButton_8.setStyleSheet(u"background-color: #3f4042;")
        icon5 = QIcon()
        icon5.addFile(u":/interfaz /assets/interfaz principal/segunda barra lateral/agregar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon5)
        self.pushButton_8.setIconSize(QSize(25, 25))
        self.label_30 = QLabel(self.widget_7)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(70, 120, 131, 31))
        self.label_30.setFont(font6)
        self.label_30.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: transparent;")
        self.pushButton_15 = QPushButton(self.widget_7)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setGeometry(QRect(10, 220, 51, 51))
        self.pushButton_15.setStyleSheet(u"background-color: #3f4042;")
        icon6 = QIcon()
        icon6.addFile(u":/interfaz /assets/interfaz principal/segunda barra lateral/archivo-de-edicion.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_15.setIcon(icon6)
        self.pushButton_15.setIconSize(QSize(25, 25))
        self.label_31 = QLabel(self.widget_7)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(70, 230, 131, 31))
        self.label_31.setFont(font6)
        self.label_31.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: transparent;")
        self.pushButton_17 = QPushButton(self.widget_7)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setGeometry(QRect(10, 330, 51, 51))
        self.pushButton_17.setStyleSheet(u"background-color: #3f4042;")
        icon7 = QIcon()
        icon7.addFile(u":/interfaz /assets/interfaz principal/segunda barra lateral/basura.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_17.setIcon(icon7)
        self.pushButton_17.setIconSize(QSize(25, 25))
        self.label_32 = QLabel(self.widget_7)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(70, 340, 131, 31))
        self.label_32.setFont(font6)
        self.label_32.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: transparent;")
        self.label_33 = QLabel(self.widget_7)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(70, 450, 141, 31))
        self.label_33.setFont(font6)
        self.label_33.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: transparent;")
        self.pushButton_18 = QPushButton(self.widget_7)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setGeometry(QRect(10, 440, 51, 51))
        self.pushButton_18.setStyleSheet(u"background-color: #3f4042;")
        icon8 = QIcon()
        icon8.addFile(u":/interfaz /assets/interfaz principal/segunda barra lateral/buscar-alt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_18.setIcon(icon8)
        self.pushButton_18.setIconSize(QSize(25, 25))
        self.stackedWidget_2 = QStackedWidget(self.Inventario)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setGeometry(QRect(230, 0, 511, 631))
        self.agregar = QWidget()
        self.agregar.setObjectName(u"agregar")
        self.lineEdit_5 = QLineEdit(self.agregar)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(150, 110, 361, 31))
        self.lineEdit_5.setStyleSheet(u"background-color: #3f4042;\n"
"color: #ffffff;\n"
"border-radius: 10px;\n"
"padding: 10px;")
        self.lineEdit_5.setMaxLength(13)
        self.pushButton_20 = QPushButton(self.agregar)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setGeometry(QRect(140, 560, 251, 31))
        self.pushButton_20.setFont(font4)
        self.pushButton_20.setStyleSheet(u"background-color: #3f4042;\n"
"border-radius: 10px;")
        self.label_35 = QLabel(self.agregar)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(10, 110, 141, 31))
        self.label_35.setFont(font1)
        self.label_35.setStyleSheet(u"background-color: transparent;\n"
"color: #2b2b2b;")
        self.label_35.setAlignment(Qt.AlignCenter)
        self.label_36 = QLabel(self.agregar)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(160, 40, 191, 31))
        self.label_36.setFont(font1)
        self.label_36.setStyleSheet(u"background-color: transparent;\n"
"color: #2b2b2b;")
        self.label_36.setAlignment(Qt.AlignCenter)
        self.lineEdit_6 = QLineEdit(self.agregar)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(150, 300, 361, 31))
        self.lineEdit_6.setStyleSheet(u"background-color: #3f4042;\n"
"color: #ffffff;\n"
"border-radius: 10px;\n"
"padding: 10px;")
        self.lineEdit_6.setMaxLength(13)
        self.label_37 = QLabel(self.agregar)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(10, 300, 141, 31))
        self.label_37.setFont(font1)
        self.label_37.setStyleSheet(u"background-color: transparent;\n"
"color: #2b2b2b;")
        self.label_37.setAlignment(Qt.AlignCenter)
        self.lineEdit_7 = QLineEdit(self.agregar)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(150, 390, 361, 31))
        self.lineEdit_7.setStyleSheet(u"background-color: #3f4042;\n"
"color: #ffffff;\n"
"border-radius: 10px;\n"
"padding: 10px;")
        self.lineEdit_7.setMaxLength(13)
        self.label_38 = QLabel(self.agregar)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(10, 390, 141, 31))
        self.label_38.setFont(font1)
        self.label_38.setStyleSheet(u"background-color: transparent;\n"
"color: #2b2b2b;")
        self.label_38.setAlignment(Qt.AlignCenter)
        self.label_39 = QLabel(self.agregar)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(10, 470, 141, 31))
        self.label_39.setFont(font1)
        self.label_39.setStyleSheet(u"background-color: transparent;\n"
"color: #2b2b2b;")
        self.label_39.setAlignment(Qt.AlignCenter)
        self.lineEdit_8 = QLineEdit(self.agregar)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(150, 470, 361, 31))
        self.lineEdit_8.setStyleSheet(u"background-color: #3f4042;\n"
"color: #ffffff;\n"
"border-radius: 10px;\n"
"padding: 10px;")
        self.lineEdit_8.setMaxLength(13)
        self.lineEdit_19 = QLineEdit(self.agregar)
        self.lineEdit_19.setObjectName(u"lineEdit_19")
        self.lineEdit_19.setGeometry(QRect(150, 200, 361, 31))
        self.lineEdit_19.setStyleSheet(u"background-color: #3f4042;\n"
"color: #ffffff;\n"
"border-radius: 10px;\n"
"padding: 10px;")
        self.lineEdit_19.setMaxLength(13)
        self.label_50 = QLabel(self.agregar)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(10, 200, 141, 31))
        self.label_50.setFont(font1)
        self.label_50.setStyleSheet(u"background-color: transparent;\n"
"color: #2b2b2b;")
        self.label_50.setAlignment(Qt.AlignCenter)
        self.stackedWidget_2.addWidget(self.agregar)
        self.modificar = QWidget()
        self.modificar.setObjectName(u"modificar")
        self.lineEdit_9 = QLineEdit(self.modificar)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setGeometry(QRect(150, 510, 361, 31))
        self.lineEdit_9.setStyleSheet(u"background-color: #3f4042;\n"
"color: #ffffff;\n"
"border-radius: 10px;\n"
"padding: 10px;")
        self.lineEdit_9.setMaxLength(13)
        self.label_40 = QLabel(self.modificar)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(10, 510, 141, 31))
        self.label_40.setFont(font1)
        self.label_40.setStyleSheet(u"background-color: transparent;\n"
"color: #2b2b2b;")
        self.label_40.setAlignment(Qt.AlignCenter)
        self.lineEdit_10 = QLineEdit(self.modificar)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setGeometry(QRect(150, 290, 361, 31))
        self.lineEdit_10.setStyleSheet(u"background-color: #3f4042;\n"
"color: #ffffff;\n"
"border-radius: 10px;\n"
"padding: 10px;")
        self.lineEdit_10.setMaxLength(13)
        self.lineEdit_11 = QLineEdit(self.modificar)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setGeometry(QRect(150, 180, 361, 31))
        self.lineEdit_11.setStyleSheet(u"background-color: #3f4042;\n"
"color: #ffffff;\n"
"border-radius: 10px;\n"
"padding: 10px;")
        self.lineEdit_11.setMaxLength(13)
        self.label_41 = QLabel(self.modificar)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(10, 180, 141, 31))
        self.label_41.setFont(font1)
        self.label_41.setStyleSheet(u"background-color: transparent;\n"
"color: #2b2b2b;")
        self.label_41.setAlignment(Qt.AlignCenter)
        self.pushButton_21 = QPushButton(self.modificar)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setGeometry(QRect(140, 580, 251, 31))
        self.pushButton_21.setFont(font4)
        self.pushButton_21.setStyleSheet(u"background-color: #3f4042;\n"
"border-radius: 10px;")
        self.label_42 = QLabel(self.modificar)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(10, 400, 141, 31))
        self.label_42.setFont(font1)
        self.label_42.setStyleSheet(u"background-color: transparent;\n"
"color: #2b2b2b;")
        self.label_42.setAlignment(Qt.AlignCenter)
        self.lineEdit_12 = QLineEdit(self.modificar)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setGeometry(QRect(150, 400, 361, 31))
        self.lineEdit_12.setStyleSheet(u"background-color: #3f4042;\n"
"color: #ffffff;\n"
"border-radius: 10px;\n"
"padding: 10px;")
        self.lineEdit_12.setMaxLength(13)
        self.label_43 = QLabel(self.modificar)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(160, 20, 191, 31))
        self.label_43.setFont(font1)
        self.label_43.setStyleSheet(u"background-color: transparent;\n"
"color: #2b2b2b;")
        self.label_43.setAlignment(Qt.AlignCenter)
        self.label_44 = QLabel(self.modificar)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(10, 290, 141, 31))
        self.label_44.setFont(font1)
        self.label_44.setStyleSheet(u"background-color: transparent;\n"
"color: #2b2b2b;")
        self.label_44.setAlignment(Qt.AlignCenter)
        self.pushButton_22 = QPushButton(self.modificar)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setGeometry(QRect(400, 80, 101, 31))
        self.pushButton_22.setFont(font4)
        self.pushButton_22.setStyleSheet(u"background-color: #3f4042;\n"
"border-radius: 10px;")
        self.lineEdit_13 = QLineEdit(self.modificar)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setGeometry(QRect(50, 80, 341, 31))
        self.lineEdit_13.setStyleSheet(u"background-color: #3f4042;\n"
"color: #ffffff;\n"
"border-radius: 10px;\n"
"padding: 10px;")
        self.lineEdit_13.setMaxLength(13)
        self.stackedWidget_2.addWidget(self.modificar)
        self.eliminar = QWidget()
        self.eliminar.setObjectName(u"eliminar")
        self.lineEdit_14 = QLineEdit(self.eliminar)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setGeometry(QRect(50, 70, 341, 31))
        self.lineEdit_14.setStyleSheet(u"background-color: #3f4042;\n"
"color: #ffffff;\n"
"border-radius: 10px;\n"
"padding: 10px;")
        self.lineEdit_14.setMaxLength(13)
        self.lineEdit_15 = QLineEdit(self.eliminar)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        self.lineEdit_15.setGeometry(QRect(150, 390, 361, 31))
        self.lineEdit_15.setStyleSheet(u"background-color: #3f4042;\n"
"color: #ffffff;\n"
"border-radius: 10px;\n"
"padding: 10px;")
        self.lineEdit_15.setMaxLength(13)
        self.lineEdit_15.setReadOnly(True)
        self.label_45 = QLabel(self.eliminar)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(10, 170, 141, 31))
        self.label_45.setFont(font1)
        self.label_45.setStyleSheet(u"background-color: transparent;\n"
"color: #2b2b2b;")
        self.label_45.setAlignment(Qt.AlignCenter)
        self.pushButton_23 = QPushButton(self.eliminar)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setGeometry(QRect(140, 570, 251, 31))
        self.pushButton_23.setFont(font4)
        self.pushButton_23.setStyleSheet(u"background-color: #3f4042;\n"
"border-radius: 10px;")
        self.label_46 = QLabel(self.eliminar)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(10, 390, 141, 31))
        self.label_46.setFont(font1)
        self.label_46.setStyleSheet(u"background-color: transparent;\n"
"color: #2b2b2b;")
        self.label_46.setAlignment(Qt.AlignCenter)
        self.label_47 = QLabel(self.eliminar)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(10, 500, 141, 31))
        self.label_47.setFont(font1)
        self.label_47.setStyleSheet(u"background-color: transparent;\n"
"color: #2b2b2b;")
        self.label_47.setAlignment(Qt.AlignCenter)
        self.lineEdit_16 = QLineEdit(self.eliminar)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        self.lineEdit_16.setGeometry(QRect(150, 170, 361, 31))
        self.lineEdit_16.setStyleSheet(u"background-color: #3f4042;\n"
"color: #ffffff;\n"
"border-radius: 10px;\n"
"padding: 10px;")
        self.lineEdit_16.setMaxLength(13)
        self.lineEdit_16.setReadOnly(True)
        self.lineEdit_17 = QLineEdit(self.eliminar)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        self.lineEdit_17.setGeometry(QRect(150, 500, 361, 31))
        self.lineEdit_17.setStyleSheet(u"background-color: #3f4042;\n"
"color: #ffffff;\n"
"border-radius: 10px;\n"
"padding: 10px;")
        self.lineEdit_17.setMaxLength(13)
        self.lineEdit_17.setReadOnly(True)
        self.pushButton_24 = QPushButton(self.eliminar)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setGeometry(QRect(400, 70, 101, 31))
        self.pushButton_24.setFont(font4)
        self.pushButton_24.setStyleSheet(u"background-color: #3f4042;\n"
"border-radius: 10px;")
        self.label_48 = QLabel(self.eliminar)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(160, 10, 191, 31))
        self.label_48.setFont(font1)
        self.label_48.setStyleSheet(u"background-color: transparent;\n"
"color: #2b2b2b;")
        self.label_48.setAlignment(Qt.AlignCenter)
        self.lineEdit_18 = QLineEdit(self.eliminar)
        self.lineEdit_18.setObjectName(u"lineEdit_18")
        self.lineEdit_18.setGeometry(QRect(150, 280, 361, 31))
        self.lineEdit_18.setStyleSheet(u"background-color: #3f4042;\n"
"color: #ffffff;\n"
"border-radius: 10px;\n"
"padding: 10px;")
        self.lineEdit_18.setMaxLength(13)
        self.lineEdit_18.setReadOnly(True)
        self.label_49 = QLabel(self.eliminar)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(10, 280, 141, 31))
        self.label_49.setFont(font1)
        self.label_49.setStyleSheet(u"background-color: transparent;\n"
"color: #2b2b2b;")
        self.label_49.setAlignment(Qt.AlignCenter)
        self.stackedWidget_2.addWidget(self.eliminar)
        self.ConsultarProducto = QWidget()
        self.ConsultarProducto.setObjectName(u"ConsultarProducto")
        self.tableWidget_5 = QTableWidget(self.ConsultarProducto)
        if (self.tableWidget_5.columnCount() < 4):
            self.tableWidget_5.setColumnCount(4)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(2, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(3, __qtablewidgetitem27)
        if (self.tableWidget_5.rowCount() < 38):
            self.tableWidget_5.setRowCount(38)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_5.setItem(0, 0, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_5.setItem(0, 1, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_5.setItem(0, 2, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_5.setItem(0, 3, __qtablewidgetitem31)
        self.tableWidget_5.setObjectName(u"tableWidget_5")
        self.tableWidget_5.setGeometry(QRect(0, 150, 511, 471))
        self.tableWidget_5.setStyleSheet(u"QTableWidget {\n"
"    background-color: #2b2b2b;\n"
"	border-radius: 0px;\n"
"    color: white;\n"
"}\n"
"\n"
"QTableWidget QHeaderView::section {\n"
"    background-color: #2b2b2b;\n"
"    color: white;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"}\n"
"QScrollBar:vertical,\n"
"QScrollBar:horizontal {\n"
"    background-color: #2b2b2b;  /* Color del scrollbar */  /* Borde del scrollbar */\n"
"}\n"
"\n"
"QScrollBar::handle:vertical,\n"
"QScrollBar::handle:horizontal {\n"
"    background-color: #3f4042;  /* Color del \u00e1rea desplazable */\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical,\n"
"QScrollBar::add-line:horizontal,\n"
"QScrollBar::sub-line:horizontal {\n"
"    background-color: #2b2b2b;  /* Color de las \u00e1reas de botones (arriba/abajo o izquierda/derecha) */\n"
"}")
        self.tableWidget_5.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_5.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_5.setProperty("showDropIndicator", True)
        self.tableWidget_5.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget_5.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tableWidget_5.setShowGrid(False)
        self.tableWidget_5.setRowCount(38)
        self.tableWidget_5.horizontalHeader().setDefaultSectionSize(128)
        self.tableWidget_5.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_5.verticalHeader().setVisible(False)
        self.tableWidget_5.verticalHeader().setProperty("showSortIndicator", False)
        self.pushButton_19 = QPushButton(self.ConsultarProducto)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setGeometry(QRect(390, 40, 101, 31))
        self.pushButton_19.setFont(font4)
        self.pushButton_19.setStyleSheet(u"background-color: #3f4042;\n"
"border-radius: 10px;")
        self.lineEdit_2 = QLineEdit(self.ConsultarProducto)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(0, 40, 381, 31))
        self.lineEdit_2.setStyleSheet(u"background-color: #3f4042;\n"
"color: #ffffff;\n"
"border-radius: 10px;\n"
"padding: 10px;")
        self.lineEdit_2.setMaxLength(13)
        self.label_34 = QLabel(self.ConsultarProducto)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(150, 100, 221, 31))
        self.label_34.setFont(font1)
        self.label_34.setStyleSheet(u"background-color: transparent;\n"
"color: #2b2b2b;")
        self.label_34.setAlignment(Qt.AlignCenter)
        self.stackedWidget_2.addWidget(self.ConsultarProducto)
        self.stackedWidget.addWidget(self.Inventario)
        self.estadistica = QWidget()
        self.estadistica.setObjectName(u"estadistica")
        self.label_51 = QLabel(self.estadistica)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setGeometry(QRect(30, 40, 221, 31))
        self.label_51.setFont(font1)
        self.label_51.setStyleSheet(u"background-color: transparent;\n"
"color: #2b2b2b;")
        self.label_51.setAlignment(Qt.AlignCenter)
        self.widget_8 = QWidget(self.estadistica)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setGeometry(QRect(60, 80, 171, 211))
        self.widget_8.setStyleSheet(u"background-color: rgb(239, 239, 239);\n"
"border-color:#2b2b2b;\n"
"border: 1px;")
        self.label_52 = QLabel(self.widget_8)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setGeometry(QRect(20, 30, 51, 31))
        font8 = QFont()
        font8.setFamilies([u"Rockwell"])
        font8.setPointSize(16)
        font8.setBold(True)
        self.label_52.setFont(font8)
        self.label_52.setStyleSheet(u"background-color: transparent;\n"
"color: #2b2b2b;")
        self.label_52.setAlignment(Qt.AlignCenter)
        self.label_53 = QLabel(self.widget_8)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setGeometry(QRect(20, 0, 131, 31))
        self.label_53.setFont(font6)
        self.label_53.setStyleSheet(u"background-color: transparent;\n"
"color: #2b2b2b;")
        self.label_53.setAlignment(Qt.AlignCenter)
        self.label_54 = QLabel(self.widget_8)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setGeometry(QRect(20, 60, 131, 31))
        self.label_54.setFont(font6)
        self.label_54.setStyleSheet(u"background-color: transparent;\n"
"color: #2b2b2b;")
        self.label_54.setAlignment(Qt.AlignCenter)
        self.label_55 = QLabel(self.widget_8)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setGeometry(QRect(20, 90, 51, 31))
        self.label_55.setFont(font8)
        self.label_55.setStyleSheet(u"background-color: transparent;\n"
"color: #2b2b2b;")
        self.label_55.setAlignment(Qt.AlignCenter)
        self.label_56 = QLabel(self.widget_8)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setGeometry(QRect(20, 150, 51, 31))
        self.label_56.setFont(font8)
        self.label_56.setStyleSheet(u"background-color: transparent;\n"
"color: #2b2b2b;")
        self.label_56.setAlignment(Qt.AlignCenter)
        self.label_57 = QLabel(self.widget_8)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setGeometry(QRect(20, 120, 131, 31))
        self.label_57.setFont(font6)
        self.label_57.setStyleSheet(u"background-color: transparent;\n"
"color: #2b2b2b;")
        self.label_57.setAlignment(Qt.AlignCenter)
        self.widget_9 = QWidget(self.estadistica)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setGeometry(QRect(300, 80, 171, 211))
        self.widget_9.setStyleSheet(u"background-color: rgb(239, 239, 239);\n"
"border-color:#2b2b2b;\n"
"border: 1px;")
        self.label_70 = QLabel(self.widget_9)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setGeometry(QRect(60, 30, 51, 31))
        self.label_70.setFont(font5)
        self.label_70.setStyleSheet(u"background-color: transparent;\n"
"color: #4caa99;")
        self.label_70.setAlignment(Qt.AlignCenter)
        self.label_71 = QLabel(self.widget_9)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setGeometry(QRect(30, 0, 121, 31))
        self.label_71.setFont(font6)
        self.label_71.setStyleSheet(u"background-color: transparent;\n"
"color: #2b2b2b;")
        self.label_71.setAlignment(Qt.AlignCenter)
        self.label_72 = QLabel(self.widget_9)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setGeometry(QRect(10, 60, 131, 31))
        self.label_72.setFont(font6)
        self.label_72.setStyleSheet(u"background-color: transparent;\n"
"color: #2b2b2b;")
        self.label_72.setAlignment(Qt.AlignCenter)
        self.label_73 = QLabel(self.widget_9)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setGeometry(QRect(20, 90, 51, 31))
        self.label_73.setFont(font5)
        self.label_73.setStyleSheet(u"background-color: transparent;\n"
"color: #4caa99;")
        self.label_73.setAlignment(Qt.AlignCenter)
        self.label_74 = QLabel(self.widget_9)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setGeometry(QRect(20, 150, 51, 31))
        self.label_74.setFont(font5)
        self.label_74.setStyleSheet(u"background-color: transparent;\n"
"color: #4caa99;")
        self.label_74.setAlignment(Qt.AlignCenter)
        self.label_75 = QLabel(self.widget_9)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setGeometry(QRect(10, 120, 131, 31))
        self.label_75.setFont(font6)
        self.label_75.setStyleSheet(u"background-color: transparent;\n"
"color: #2b2b2b;")
        self.label_75.setAlignment(Qt.AlignCenter)
        self.widget_10 = QWidget(self.estadistica)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setGeometry(QRect(540, 80, 171, 211))
        self.widget_10.setStyleSheet(u"background-color: rgb(239, 239, 239);\n"
"border-color:#2b2b2b;\n"
"border: 1px;")
        self.label_76 = QLabel(self.widget_10)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setGeometry(QRect(20, 30, 51, 31))
        self.label_76.setFont(font5)
        self.label_76.setStyleSheet(u"background-color: transparent;\n"
"color: #2b2b2b;")
        self.label_76.setAlignment(Qt.AlignCenter)
        self.label_77 = QLabel(self.widget_10)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setGeometry(QRect(20, 0, 131, 31))
        self.label_77.setFont(font6)
        self.label_77.setStyleSheet(u"background-color: transparent;\n"
"color: #2b2b2b;")
        self.label_77.setAlignment(Qt.AlignCenter)
        self.label_78 = QLabel(self.widget_10)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setGeometry(QRect(20, 60, 131, 31))
        self.label_78.setFont(font6)
        self.label_78.setStyleSheet(u"background-color: transparent;\n"
"color: #2b2b2b;")
        self.label_78.setAlignment(Qt.AlignCenter)
        self.label_79 = QLabel(self.widget_10)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setGeometry(QRect(20, 90, 51, 31))
        self.label_79.setFont(font5)
        self.label_79.setStyleSheet(u"background-color: transparent;\n"
"color: #2b2b2b;")
        self.label_79.setAlignment(Qt.AlignCenter)
        self.label_80 = QLabel(self.widget_10)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setGeometry(QRect(30, 150, 71, 31))
        self.label_80.setFont(font5)
        self.label_80.setStyleSheet(u"background-color: transparent;\n"
"color: #2b2b2b;")
        self.label_80.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_81 = QLabel(self.widget_10)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setGeometry(QRect(20, 120, 131, 31))
        self.label_81.setFont(font6)
        self.label_81.setStyleSheet(u"background-color: transparent;\n"
"color: #2b2b2b;")
        self.label_81.setAlignment(Qt.AlignCenter)
        self.widget_11 = QWidget(self.estadistica)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setGeometry(QRect(50, 350, 371, 291))
        self.widget_11.setStyleSheet(u"background-color:#2b2b2b;")
        self.label_82 = QLabel(self.estadistica)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setGeometry(QRect(110, 310, 261, 31))
        self.label_82.setFont(font1)
        self.label_82.setStyleSheet(u"background-color: transparent;\n"
"color: #2b2b2b;")
        self.label_82.setAlignment(Qt.AlignCenter)
        self.widget_12 = QWidget(self.estadistica)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setGeometry(QRect(440, 400, 291, 81))
        self.widget_12.setStyleSheet(u"background-color: #4caa99;")
        self.pushButton_25 = QPushButton(self.widget_12)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setGeometry(QRect(40, 15, 51, 51))
        self.pushButton_25.setStyleSheet(u"background-color: #4f7e7c;\n"
"border-radius: 25px;")
        self.pushButton_25.setIcon(icon2)
        self.pushButton_25.setIconSize(QSize(30, 30))
        self.label_84 = QLabel(self.widget_12)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setGeometry(QRect(100, 25, 161, 31))
        self.label_84.setFont(font2)
        self.label_84.setStyleSheet(u"background-color: transparent;\n"
"color: #ffffff;")
        self.label_84.setAlignment(Qt.AlignCenter)
        self.label_83 = QLabel(self.estadistica)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setGeometry(QRect(450, 340, 261, 31))
        self.label_83.setFont(font1)
        self.label_83.setStyleSheet(u"background-color: transparent;\n"
"color: #2b2b2b;")
        self.label_83.setAlignment(Qt.AlignCenter)
        self.widget_13 = QWidget(self.estadistica)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setGeometry(QRect(440, 510, 291, 81))
        self.widget_13.setStyleSheet(u"background-color: #2b2b2b;")
        self.pushButton_26 = QPushButton(self.widget_13)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setGeometry(QRect(40, 15, 51, 51))
        self.pushButton_26.setStyleSheet(u"background-color: #3f4042;\n"
"border-radius: 25px;")
        self.pushButton_26.setIcon(icon2)
        self.pushButton_26.setIconSize(QSize(30, 30))
        self.label_85 = QLabel(self.widget_13)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setGeometry(QRect(100, 25, 171, 31))
        self.label_85.setFont(font2)
        self.label_85.setStyleSheet(u"background-color: transparent;\n"
"color: #ffffff;")
        self.label_85.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.estadistica)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TPV Software", None))
        self.pushButton.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Vender Productos", None))
        self.pushButton_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Devolver Productos", None))
        self.pushButton_3.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Inventario de Tienda", None))
        self.pushButton_4.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Estad\u00edstica de venta", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Usuario@", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Administrador", None))
        self.pushButton_5.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Cerrar Sesi\u00f3n", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar Producto", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir Producto", None))
#if QT_CONFIG(shortcut)
        self.pushButton_6.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Resumen de Venta", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"SUBTOTAL", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"TOTAL", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"0\u20ac", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"0\u20ac", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Confirmar Compra", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Eliminar Venta actual", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"0\u20ac", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"IVA", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Precio", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Cantidad", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem3 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Compresa de ni\u00f1os", None));
        ___qtablewidgetitem4 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"700\u20ac", None));
        ___qtablewidgetitem5 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"1", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Resumen de Inventario", None))
        ___qtablewidgetitem6 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"ISBN", None));
        ___qtablewidgetitem7 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Stock Actual", None));
        ___qtablewidgetitem8 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Stock PosVenta", None));

        __sortingEnabled1 = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        ___qtablewidgetitem9 = self.tableWidget_2.item(0, 0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"8356326162", None));
        ___qtablewidgetitem10 = self.tableWidget_2.item(0, 1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem11 = self.tableWidget_2.item(0, 2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"0", None));
        self.tableWidget_2.setSortingEnabled(__sortingEnabled1)

        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Resumen de Devoluci\u00f3n", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"SUBTOTAL", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"TOTAL", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"10807\u20ac", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"10807\u20ac", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"Confirmar Devoluci\u00f3n", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"Eliminar devoluci\u00f3n", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"10807\u20ac", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"IVA", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Resumen de Inventario", None))
        ___qtablewidgetitem12 = self.tableWidget_4.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"ISBN", None));
        ___qtablewidgetitem13 = self.tableWidget_4.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Stock Actual", None));
        ___qtablewidgetitem14 = self.tableWidget_4.horizontalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Stock PosVenta", None));

        __sortingEnabled2 = self.tableWidget_4.isSortingEnabled()
        self.tableWidget_4.setSortingEnabled(False)
        ___qtablewidgetitem15 = self.tableWidget_4.item(0, 0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"8356326162", None));
        ___qtablewidgetitem16 = self.tableWidget_4.item(0, 1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem17 = self.tableWidget_4.item(0, 2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"0", None));
        self.tableWidget_4.setSortingEnabled(__sortingEnabled2)

        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Devolver", None))
#if QT_CONFIG(shortcut)
        self.pushButton_10.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.lineEdit_3.setText("")
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar Producto a devolver", None))
        ___qtablewidgetitem18 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem19 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Precio", None));
        ___qtablewidgetitem20 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Cantidad", None));

        __sortingEnabled3 = self.tableWidget_3.isSortingEnabled()
        self.tableWidget_3.setSortingEnabled(False)
        ___qtablewidgetitem21 = self.tableWidget_3.item(0, 0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Compresa de ni\u00f1os", None));
        ___qtablewidgetitem22 = self.tableWidget_3.item(0, 1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"700\u20ac", None));
        ___qtablewidgetitem23 = self.tableWidget_3.item(0, 2)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"1", None));
        self.tableWidget_3.setSortingEnabled(__sortingEnabled3)

        self.pushButton_8.setText("")
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir Producto", None))
        self.pushButton_15.setText("")
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Modificar Producto", None))
        self.pushButton_17.setText("")
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Eliminar Producto", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Consultar Productos", None))
        self.pushButton_18.setText("")
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese el C\u00f3digo", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir Producto", None))
#if QT_CONFIG(shortcut)
        self.pushButton_20.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Detalles del producto", None))
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese el precio", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Precio", None))
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese la cantidad actual", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Stock", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Oferta", None))
        self.lineEdit_8.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese oferta(Si la hay)", None))
        self.lineEdit_19.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese el nombre", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.lineEdit_9.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Oferta", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Oferta", None))
        self.lineEdit_10.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Precio", None))
        self.lineEdit_11.setText("")
        self.lineEdit_11.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"Modificar Producto", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Stock", None))
        self.lineEdit_12.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Stock Actual", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Modificar Producto", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Precio", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"Buscar Producto", None))
#if QT_CONFIG(shortcut)
        self.pushButton_22.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.lineEdit_13.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar Producto", None))
        self.lineEdit_14.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar Producto", None))
        self.lineEdit_15.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Stock Actual", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"Eliminar Producto", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Stock", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Oferta", None))
        self.lineEdit_16.setText("")
        self.lineEdit_16.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.lineEdit_17.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Oferta", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"Buscar Producto", None))
#if QT_CONFIG(shortcut)
        self.pushButton_24.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Eliminar Producto", None))
        self.lineEdit_18.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Precio", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Precio", None))
        ___qtablewidgetitem24 = self.tableWidget_5.horizontalHeaderItem(0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem25 = self.tableWidget_5.horizontalHeaderItem(1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Precio", None));
        ___qtablewidgetitem26 = self.tableWidget_5.horizontalHeaderItem(2)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Stock", None));
        ___qtablewidgetitem27 = self.tableWidget_5.horizontalHeaderItem(3)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Descuento", None));

        __sortingEnabled4 = self.tableWidget_5.isSortingEnabled()
        self.tableWidget_5.setSortingEnabled(False)
        ___qtablewidgetitem28 = self.tableWidget_5.item(0, 0)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Unamuno", None));
        ___qtablewidgetitem29 = self.tableWidget_5.item(0, 1)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"2\u20ac", None));
        ___qtablewidgetitem30 = self.tableWidget_5.item(0, 2)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem31 = self.tableWidget_5.item(0, 3)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"10", None));
        self.tableWidget_5.setSortingEnabled(__sortingEnabled4)

        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"Buscar Producto", None))
#if QT_CONFIG(shortcut)
        self.pushButton_19.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar Producto", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Resultados", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Resumen de ventas", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"108", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"N\u00famero de ventas", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Ventas En efectivo", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"108", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"108", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Ventas con dat\u00e1fono", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"1080\u20ac", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Venta de hoy", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"Total en efectivo", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"1080\u20ac", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"1080\u20ac", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"Total en dat\u00e1fono", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"Productos Vendidos", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"Productos Devueltos", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"Productos en tienda", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"Estad\u00edstica de venta semanal", None))
        self.pushButton_25.setText("")
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"Imprimir estad\u00edstica", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"Operaciones", None))
        self.pushButton_26.setText("")
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"Actualizar Informaci\u00f3n", None))
    # retranslateUi

