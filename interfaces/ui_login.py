# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginzuHUTG.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QStackedWidget, QWidget)
import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1024, 700)
        Form.setStyleSheet(u"/*-----QWidget-----*/\n"
"QWidget\n"
"{\n"
"	background-color: #fff;\n"
"	color: red;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLabel-----*/\n"
"QLabel\n"
"{\n"
"	background-color: transparent;\n"
"	color: #454544;\n"
"	font-weight: bold;\n"
"	font-size: 13px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QPushButton-----*/\n"
"QPushButton\n"
"{\n"
"	background-color: #1b3cbd;\n"
"	color: #fff;\n"
"	font-size: 13px;\n"
"	font-weight: bold;\n"
"	border-top-right-radius: 15px;\n"
"	border-top-left-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"	border-bottom-left-radius: 15px;\n"
"	padding: 10px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::disabled\n"
"{\n"
"	background-color: #1b3cbd;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::hover\n"
"{\n"
"	background-color: #254de8;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"	background-color: #1b3cbd;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QCheckBox-----*/\n"
"QCheckBox\n"
"{\n"
"	background-color: transparent;\n"
"	color: #5c55e9;\n"
"	font-size: 10px;\n"
"	font-weight: bold;\n"
"	border: no"
                        "ne;\n"
"	border-radius: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QCheckBox-----*/\n"
"QCheckBox::indicator\n"
"{\n"
"    background-color: #323232;\n"
"    border: 1px solid darkgray;\n"
"    width: 12px;\n"
"    height: 12px;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image:url(\"./ressources/check.png\");\n"
"	background-color: #5c55e9;\n"
"    border: 1px solid #5c55e9;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:unchecked:hover\n"
"{\n"
"    border: 1px solid #5c55e9;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::disabled\n"
"{\n"
"	color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:disabled\n"
"{\n"
"	background-color: #656565;\n"
"	color: #656565;\n"
"    border: 1px solid #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLineEdit-----*/\n"
"QLineEdit\n"
"{\n"
"	background-color: #c2c7d5;\n"
"	color: #2a547f;\n"
"	border: none;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QListView-----*/\n"
"QListView\n"
"{\n"
"	background-color: #5c55e9;\n"
"	color: #fff;\n"
"	font-size: 14px;\n"
""
                        "	font-weight: bold;\n"
"	show-decoration-selected: 0;\n"
"	border-radius: 4px;\n"
"	padding-left: -15px;\n"
"	padding-right: -15px;\n"
"	padding-top: 5px;\n"
"\n"
"} \n"
"\n"
"\n"
"QListView:disabled \n"
"{\n"
"	background-color: #5c5c5c;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item\n"
"{\n"
"	background-color: #454e5e;\n"
"	border: none;\n"
"	padding: 10px;\n"
"	border-radius: 0px;\n"
"	padding-left : 10px;\n"
"	height: 32px;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:selected\n"
"{\n"
"	color: #000;\n"
"	background-color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:!selected\n"
"{\n"
"	color:white;\n"
"	background-color: transparent;\n"
"	border: none;\n"
"	padding-left : 10px;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:!selected:hover\n"
"{\n"
"	color: #fff;\n"
"	background-color: #5564f2;\n"
"	border: none;\n"
"	padding-left : 10px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QTreeView-----*/\n"
"QTreeView \n"
"{\n"
"	background-color: #fff;\n"
"	show-decoration-selected: 0;\n"
"	color: #454544;\n"
"\n"
"}\n"
"\n"
"\n"
"QT"
                        "reeView:disabled\n"
"{\n"
"	background-color: #242526;\n"
"	show-decoration-selected: 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item \n"
"{\n"
"	border-top-color: transparent;\n"
"	border-bottom-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item:hover \n"
"{\n"
"	background-color: #bcbdbb;\n"
"	color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item:selected \n"
"{\n"
"	background-color: #5c55e9;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item:selected:active\n"
"{\n"
"	background-color: #5c55e9;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item:selected:disabled\n"
"{\n"
"	background-color: #525251;\n"
"	color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed,\n"
"QTreeView::branch:closed:has-children:has-siblings \n"
"{\n"
"	image: url(://tree-closed.png);\n"
"\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings,\n"
"QTreeView::branch:open:has-children:has-siblings  \n"
"{\n"
"	image: url(://tree-open.png);\n"
"\n"
"}\n"
"\n"
"\n"
"/*"
                        "-----QTableView & QTableWidget-----*/\n"
"QTableView\n"
"{\n"
"    background-color: #fff;\n"
"	border: 1px solid gray;\n"
"    color: #454544;\n"
"    gridline-color: gray;\n"
"    outline : 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::disabled\n"
"{\n"
"    background-color: #242526;\n"
"    border: 1px solid #32414B;\n"
"    color: #656565;\n"
"    gridline-color: #656565;\n"
"    outline : 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::item:hover \n"
"{\n"
"    background-color: #bcbdbb;\n"
"    color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::item:selected \n"
"{\n"
"	background-color: #5c55e9;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::item:selected:disabled\n"
"{\n"
"    background-color: #1a1b1c;\n"
"    border: 2px solid #525251;\n"
"    color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableCornerButton::section\n"
"{\n"
"	background-color: #ced5e3;\n"
"	border: none;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section\n"
"{\n"
"	color: #2a547f;\n"
"	border: 0px;\n"
"	background-color: #ce"
                        "d5e3;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:disabled\n"
"{\n"
"    background-color: #525251;\n"
"    color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:checked\n"
"{\n"
"    color: #fff;\n"
"    background-color: #5c55e9;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:checked:disabled\n"
"{\n"
"    color: #656565;\n"
"    background-color: #525251;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::vertical::first,\n"
"QHeaderView::section::vertical::only-one\n"
"{\n"
"    border-top: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::vertical\n"
"{\n"
"    border-top: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::horizontal::first,\n"
"QHeaderView::section::horizontal::only-one\n"
"{\n"
"    border-left: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::horizontal\n"
"{\n"
"    border-left: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QScrollBar-----*/\n"
"QScrollBar:horizontal \n"
"{\n"
"    background-color: transpare"
                        "nt;\n"
"    height: 8px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:horizontal \n"
"{\n"
"    border: none;\n"
"	min-width: 100px;\n"
"    background-color: #7e92b7;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal, \n"
"QScrollBar::sub-line:horizontal,\n"
"QScrollBar::add-page:horizontal, \n"
"QScrollBar::sub-page:horizontal \n"
"{\n"
"    width: 0px;\n"
"    background-color: #d8dce6;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical \n"
"{\n"
"    background-color: transparent;\n"
"    width: 8px;\n"
"    margin: 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical \n"
"{\n"
"    border: none;\n"
"	min-height: 100px;\n"
"    background-color: #7e92b7;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical, \n"
"QScrollBar::sub-line:vertical,\n"
"QScrollBar::add-page:vertical, \n"
"QScrollBar::sub-page:vertical \n"
"{\n"
"    height: 0px;\n"
"    background-color: #d8dce6;\n"
"\n"
"}\n"
"")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 512, 700))
        self.widget.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #2b2b2b, stop:1 #3f4042);")
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 10, 41, 31))
        icon = QIcon()
        icon.addFile(u":/login/assets/login/circulo-marca-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(30, 30))
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(40, 320, 411, 301))
        self.widget_3.setStyleSheet(u"image: url(:/login/assets/login/cohete.png);")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 120, 511, 101))
        font = QFont()
        font.setFamilies([u"Rockwell"])
        font.setBold(True)
        self.label.setFont(font)
        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(512, 0, 512, 700))
        self.stackedWidget.setStyleSheet(u"background-color: #ffffff;\n"
"color: #ffffff")
        self.login = QWidget()
        self.login.setObjectName(u"login")
        self.switchButton = QPushButton(self.login)
        self.switchButton.setObjectName(u"switchButton")
        self.switchButton.setGeometry(QRect(420, 20, 81, 31))
        self.switchButton.setStyleSheet(u"QPushButton#switchButton {\n"
"    background-color: #2b2b2b; /* Color cuando est\u00e1 apagado */\n"
"    color: white;\n"
"    border: 2px solid #2b2b2b;\n"
"    border-radius: 15px;\n"
"    padding: 5px;\n"
"}\n"
"")
        self.label_2 = QLabel(self.login)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 160, 121, 41))
        self.label_2.setStyleSheet(u"background-color: transparent;")
        self.label_3 = QLabel(self.login)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 240, 91, 31))
        self.label_3.setStyleSheet(u"background-color: transparent;")
        self.lineEdit = QLineEdit(self.login)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(70, 280, 281, 31))
        font1 = QFont()
        font1.setPointSize(10)
        self.lineEdit.setFont(font1)
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"    background-color: transparent; /* Fondo transparente */\n"
"    border: none; /* Sin borde predeterminado */\n"
"    border-bottom: 1px solid #2b2b2b; /* Borde inferior de 1 p\u00edxel, color negro */\n"
"	color: #2b2b2b;\n"
"}")
        self.label_4 = QLabel(self.login)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(70, 340, 91, 31))
        self.label_4.setStyleSheet(u"background-color: transparent;")
        self.lineEdit_2 = QLineEdit(self.login)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(70, 390, 281, 31))
        self.lineEdit_2.setStyleSheet(u"QLineEdit{\n"
"    background-color: transparent; /* Fondo transparente */\n"
"    border: none; /* Sin borde predeterminado */\n"
"    border-bottom: 1px solid #2b2b2b; /* Borde inferior de 1 p\u00edxel, color negro */\n"
"	color: #2b2b2b\n"
"}")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.label_5 = QLabel(self.login)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(70, 450, 171, 31))
        self.label_5.setStyleSheet(u"background-color: transparent;")
        self.switchButton_3 = QPushButton(self.login)
        self.switchButton_3.setObjectName(u"switchButton_3")
        self.switchButton_3.setGeometry(QRect(250, 450, 81, 31))
        self.switchButton_3.setStyleSheet(u"QPushButton {\n"
"    background-color: #2b2b2b; /* Color cuando est\u00e1 apagado */\n"
"    color: white;\n"
"    border: 2px solid #2b2b2b;\n"
"    border-radius: 15px;\n"
"    padding: 5px;\n"
"}\n"
"")
        self.switchButton_4 = QPushButton(self.login)
        self.switchButton_4.setObjectName(u"switchButton_4")
        self.switchButton_4.setGeometry(QRect(70, 500, 81, 31))
        self.switchButton_4.setStyleSheet(u"QPushButton {\n"
"    background-color: #2b2b2b; /* Color cuando est\u00e1 apagado */\n"
"    color: white;\n"
"    border: 2px solid #2b2b2b;\n"
"    border-radius: 15px;\n"
"    padding: 5px;\n"
"}\n"
"")
        self.stackedWidget.addWidget(self.login)
        self.register_2 = QWidget()
        self.register_2.setObjectName(u"register_2")
        self.switchButton_2 = QPushButton(self.register_2)
        self.switchButton_2.setObjectName(u"switchButton_2")
        self.switchButton_2.setGeometry(QRect(420, 20, 81, 31))
        self.switchButton_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #2b2b2b; /* Color cuando est\u00e1 apagado */\n"
"    color: white;\n"
"    border: 2px solid #2b2b2b;\n"
"    border-radius: 15px;\n"
"    padding: 5px;\n"
"}")
        self.label_6 = QLabel(self.register_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(70, 90, 131, 41))
        self.label_6.setStyleSheet(u"background-color: transparent;")
        self.label_7 = QLabel(self.register_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(70, 170, 101, 31))
        self.label_7.setStyleSheet(u"background-color: transparent;")
        self.lineEdit_3 = QLineEdit(self.register_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(70, 210, 281, 31))
        self.lineEdit_3.setStyleSheet(u"QLineEdit{\n"
"    background-color: transparent; /* Fondo transparente */\n"
"    border: none; /* Sin borde predeterminado */\n"
"    border-bottom: 1px solid #2b2b2b; /* Borde inferior de 1 p\u00edxel, color negro */\n"
"	color: #2b2b2b\n"
"}")
        self.label_8 = QLabel(self.register_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(70, 270, 101, 31))
        self.label_8.setStyleSheet(u"background-color: transparent;")
        self.lineEdit_4 = QLineEdit(self.register_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(70, 310, 281, 31))
        self.lineEdit_4.setStyleSheet(u"QLineEdit{\n"
"    background-color: transparent; /* Fondo transparente */\n"
"    border: none; /* Sin borde predeterminado */\n"
"    border-bottom: 1px solid #2b2b2b; /* Borde inferior de 1 p\u00edxel, color negro */\n"
"	color: #2b2b2b\n"
"}")
        self.lineEdit_5 = QLineEdit(self.register_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(70, 410, 281, 31))
        self.lineEdit_5.setStyleSheet(u"QLineEdit{\n"
"    background-color: transparent; /* Fondo transparente */\n"
"    border: none; /* Sin borde predeterminado */\n"
"    border-bottom: 1px solid #2b2b2b; /* Borde inferior de 1 p\u00edxel, color negro */\n"
"	color: #2b2b2b\n"
"}")
        self.lineEdit_5.setEchoMode(QLineEdit.Password)
        self.label_9 = QLabel(self.register_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(70, 370, 101, 31))
        self.label_9.setStyleSheet(u"background-color: transparent;")
        self.lineEdit_6 = QLineEdit(self.register_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(70, 510, 281, 31))
        self.lineEdit_6.setStyleSheet(u"QLineEdit{\n"
"    background-color: transparent; /* Fondo transparente */\n"
"    border: none; /* Sin borde predeterminado */\n"
"    border-bottom: 1px solid #2b2b2b; /* Borde inferior de 1 p\u00edxel, color negro */\n"
"	color: #2b2b2b\n"
"}")
        self.lineEdit_6.setEchoMode(QLineEdit.Password)
        self.label_10 = QLabel(self.register_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(70, 470, 151, 31))
        self.label_10.setStyleSheet(u"background-color: transparent;")
        self.switchButton_5 = QPushButton(self.register_2)
        self.switchButton_5.setObjectName(u"switchButton_5")
        self.switchButton_5.setGeometry(QRect(70, 570, 81, 31))
        self.switchButton_5.setStyleSheet(u"QPushButton {\n"
"    background-color: #2b2b2b; /* Color cuando est\u00e1 apagado */\n"
"    color: white;\n"
"    border: 2px solid #2b2b2b;\n"
"    border-radius: 15px;\n"
"    padding: 5px;\n"
"}")
        self.stackedWidget.addWidget(self.register_2)

        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Rockwell'; font-size:13px; font-weight:700; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#ffffff;\">Aproveche las extraordinarias capacidades<br />de nuestra aplicaci\u00f3n y libere todo su potencial</span></p></body></html>", None))
        self.switchButton.setText(QCoreApplication.translate("Form", u"REGISTER", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:22pt; color:#3f4042;\">LOGIN</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:11pt; color:#3f4042;\">Email</span></p></body></html>", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Ingresar Email", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:11pt; color:#3f4042;\">Password</span></p></body></html>", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"Ingresar Contrase\u00f1a", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:8pt; color:#3f4042;\">\u00bfHas olvidado tu contrase\u00f1a?</span></p></body></html>", None))
        self.switchButton_3.setText(QCoreApplication.translate("Form", u"Recup\u00e9rala", None))
        self.switchButton_4.setText(QCoreApplication.translate("Form", u"LOGIN", None))
        self.switchButton_2.setText(QCoreApplication.translate("Form", u"LOGIN", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:22pt; color:#3f4042;\">REGISTER</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:11pt; color:#3f4042;\">Email</span></p></body></html>", None))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("Form", u"Ingresar Email", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:11pt; color:#3f4042;\">Usuario</span></p></body></html>", None))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("Form", u"Ingresar Username", None))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("Form", u"Ingresar Contrase\u00f1a", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:11pt; color:#3f4042;\">Contrase\u00f1a</span></p></body></html>", None))
        self.lineEdit_6.setText("")
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("Form", u"Confirmar Contrase\u00f1a", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:11pt; color:#3f4042;\">Confirmar Contrase\u00f1a</span></p></body></html>", None))
        self.switchButton_5.setText(QCoreApplication.translate("Form", u"Register", None))
    # retranslateUi

