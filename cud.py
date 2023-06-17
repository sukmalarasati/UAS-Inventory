from PyQt6.QtWidgets import QDialog
from PyQt6 import QtGui, uic
import mysql.connector
from ui import CUD_UI

class CudDialog(QDialog):
    def __init__(self, db, cursor, kode_barang=None):
        super().__init__()

        uic.loadUi(CUD_UI, self)

        self.db = db
        self.cursor = cursor

        if kode_barang:
            self.kode_barang = kode_barang
            self.load_barang()
        else:
            self.kode_barang = None
            self.setWindowTitle('Tambah Barang')

        self.save_button.clicked.connect(self.save_barang)
        self.delete_button.clicked.connect(self.delete_barang)

    def load_barang(self):
        self.cursor.execute("SELECT id, kode_barang, nama_barang, jumlah_barang, harga_barang, keuntungan FROM barang WHERE kode_barang=%s", (self.kode_barang,))
        barang = self.cursor.fetchone()
        self.setWindowTitle('Edit Barang [%s]' % barang[1])
        self.kode_barang_field.setText(barang[1])
        self.nama_barang_field.setText(barang[2])
        self.jumlah_barang_field.setText(str(barang[3]))
        self.harga_barang_field.setText(str(barang[4]))
        self.keuntungan_barang_field.setText(str(barang[5]))

    def save_barang(self):
        if self.kode_barang:
            self.cursor.execute("UPDATE barang SET nama_barang=%s, kode_barang=%s, jumlah_barang=%s, harga_barang=%s, keuntungan=%s WHERE kode_barang=%s", (
                self.nama_barang_field.text(),
                self.kode_barang_field.text(),
                self.jumlah_barang_field.text(),
                self.harga_barang_field.text(),
                self.keuntungan_barang_field.text(),
                self.kode_barang,
            ))
        else:
            self.cursor.execute("INSERT INTO barang (nama_barang, kode_barang, jumlah_barang, harga_barang, keuntungan) VALUES (%s, %s, %s, %s, %s)", (
                self.nama_barang_field.text(),
                self.kode_barang_field.text(),
                self.jumlah_barang_field.text(),
                self.harga_barang_field.text(),
                self.keuntungan_barang_field.text(),
            ))
        self.db.commit()
        self.close()

    def delete_barang(self):
        if self.kode_barang:
            self.cursor.execute("DELETE FROM barang WHERE kode_barang=%s", (self.kode_barang,))
            self.db.commit()
        self.close()
