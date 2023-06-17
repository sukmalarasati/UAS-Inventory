# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cud.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(800, 600)
        Dialog.setStyleSheet(u"background-color: #006494;")
        self.kode_barang_field = QLineEdit(Dialog)
        self.kode_barang_field.setObjectName(u"kode_barang_field")
        self.kode_barang_field.setGeometry(QRect(330, 40, 340, 50))
        self.kode_barang_field.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px")
        self.nama_barang_field = QLineEdit(Dialog)
        self.nama_barang_field.setObjectName(u"nama_barang_field")
        self.nama_barang_field.setGeometry(QRect(330, 130, 340, 50))
        self.nama_barang_field.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px")
        self.jumlah_barang_field = QLineEdit(Dialog)
        self.jumlah_barang_field.setObjectName(u"jumlah_barang_field")
        self.jumlah_barang_field.setGeometry(QRect(330, 220, 340, 50))
        self.jumlah_barang_field.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px")
        self.harga_barang_field = QLineEdit(Dialog)
        self.harga_barang_field.setObjectName(u"harga_barang_field")
        self.harga_barang_field.setGeometry(QRect(330, 310, 340, 50))
        self.harga_barang_field.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px")
        self.keuntungan_barang_field = QLineEdit(Dialog)
        self.keuntungan_barang_field.setObjectName(u"keuntungan_barang_field")
        self.keuntungan_barang_field.setGeometry(QRect(330, 400, 340, 50))
        self.keuntungan_barang_field.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px")
        self.save_button = QPushButton(Dialog)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setGeometry(QRect(220, 510, 141, 51))
        self.save_button.setStyleSheet(u"color: #006494;\n"
"font: 700 13pt \"Segoe UI\";\n"
"background-color: ;\n"
"background-color: ;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.delete_button = QPushButton(Dialog)
        self.delete_button.setObjectName(u"delete_button")
        self.delete_button.setGeometry(QRect(460, 510, 141, 51))
        self.delete_button.setStyleSheet(u"color: #006494;\n"
"font: 700 13pt \"Segoe UI\";\n"
"background-color: ;\n"
"background-color: ;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 50, 124, 30))
        font = QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(110, 140, 131, 30))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(110, 230, 141, 30))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(110, 320, 133, 30))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(110, 410, 116, 30))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Tambah/Ubah/Hapus Barang", None))
        self.save_button.setText(QCoreApplication.translate("Dialog", u"Simpan", None))
        self.delete_button.setText(QCoreApplication.translate("Dialog", u"Hapus", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Kode Barang", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Nama Barang", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Jumlah Barang", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Harga Barang", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Keuntungan", None))
    # retranslateUi

