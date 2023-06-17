# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"background-color: rgb(33, 33, 33);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.bg = QWidget(self.centralwidget)
        self.bg.setObjectName(u"bg")
        self.bg.setGeometry(QRect(20, 20, 761, 561))
        self.bg.setStyleSheet(u"background-color: #006494;\n"
"border-radius: 20px;")
        self.label_3 = QLabel(self.bg)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(260, 50, 222, 51))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Segoe UI Semibold"])
        font.setPointSize(23)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255)")
        self.label_2 = QLabel(self.bg)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(170, 300, 90, 30))
        font1 = QFont()
        font1.setPointSize(13)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255)")
        self.label = QLabel(self.bg)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(170, 220, 98, 30))
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255)")
        self.username_field = QLineEdit(self.bg)
        self.username_field.setObjectName(u"username_field")
        self.username_field.setGeometry(QRect(330, 220, 291, 41))
        self.username_field.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px")
        self.password_field = QLineEdit(self.bg)
        self.password_field.setObjectName(u"password_field")
        self.password_field.setGeometry(QRect(330, 300, 291, 41))
        self.password_field.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px")
        self.login_button = QPushButton(self.bg)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setGeometry(QRect(280, 440, 191, 61))
        self.login_button.setStyleSheet(u"color: #006494;\n"
"font: 700 13pt \"Segoe UI\";\n"
"background-color: ;\n"
"background-color: ;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.login_button.setIconSize(QSize(20, 20))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Login Admin", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.login_button.setText(QCoreApplication.translate("MainWindow", u"Login", None))
    # retranslateUi

