# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'barang_window.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"background-color: #006494;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.table = QTableWidget(self.centralwidget)
        self.table.setObjectName(u"table")
        self.table.setGeometry(QRect(20, 69, 760, 421))
        self.table.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.add_button = QPushButton(self.centralwidget)
        self.add_button.setObjectName(u"add_button")
        self.add_button.setGeometry(QRect(60, 520, 171, 51))
        self.add_button.setStyleSheet(u"color: #006494;\n"
"font: 700 11pt \"Segoe UI\";\n"
"background-color: ;\n"
"background-color: ;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.edit_button = QPushButton(self.centralwidget)
        self.edit_button.setObjectName(u"edit_button")
        self.edit_button.setGeometry(QRect(250, 520, 151, 51))
        self.edit_button.setStyleSheet(u"color: #006494;\n"
"font: 700 11pt \"Segoe UI\";\n"
"background-color: ;\n"
"background-color: ;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.delete_button = QPushButton(self.centralwidget)
        self.delete_button.setObjectName(u"delete_button")
        self.delete_button.setGeometry(QRect(420, 520, 151, 51))
        self.delete_button.setStyleSheet(u"color: #006494;\n"
"font: 700 11pt \"Segoe UI\";\n"
"background-color: ;\n"
"background-color: ;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.export_button = QPushButton(self.centralwidget)
        self.export_button.setObjectName(u"export_button")
        self.export_button.setGeometry(QRect(590, 520, 151, 51))
        self.export_button.setStyleSheet(u"color: #006494;\n"
"font: 700 11pt \"Segoe UI\";\n"
"background-color: ;\n"
"background-color: ;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(310, 10, 175, 51))
        font = QFont()
        font.setPointSize(23)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Daftar Barang", None))
        self.add_button.setText(QCoreApplication.translate("MainWindow", u"Tambah Barang", None))
        self.edit_button.setText(QCoreApplication.translate("MainWindow", u"Edit Barang", None))
        self.delete_button.setText(QCoreApplication.translate("MainWindow", u"Hapus Barang", None))
        self.export_button.setText(QCoreApplication.translate("MainWindow", u"Export ke Excel", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Inventory", None))
    # retranslateUi

