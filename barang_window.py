from PyQt6.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QAbstractItemView, QPushButton, QInputDialog, QLineEdit, QMessageBox, QFileDialog
from PyQt6 import uic, QtGui
from cud import CudDialog
import mysql.connector
import pandas as pd
import ui

class BarangWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi(ui.BARANG_WINDOW_UI(), self)
        self.setWindowIcon(QtGui.QIcon(ui.STOCK_ICO()))

        self.db = mysql.connector.connect(
            host=ui.HOST,
            user=ui.USERNAME,
            password=ui.PASSWORD,
            database=ui.DATABASE
        )
        self.cursor = self.db.cursor()

        self.table = self.findChild(QTableWidget, 'table')
        # self.table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        self.add_button = self.findChild(QPushButton, 'add_button')
        self.add_button.clicked.connect(self.add_barang)
        self.edit_button = self.findChild(QPushButton, 'edit_button')
        self.edit_button.clicked.connect(self.edit_barang)
        self.delete_button = self.findChild(QPushButton, 'delete_button')
        self.delete_button.clicked.connect(self.delete_barang)
        self.export_button = self.findChild(QPushButton, 'export_button')
        self.export_button.clicked.connect(self.export_to_excel)

        self.is_set_header = False
        self.load_data()

    def load_data(self):
        self.cursor.execute("SELECT * FROM barang ORDER BY nama_barang")
        result = self.cursor.fetchall()

        self.table.setRowCount(0)

        if not self.is_set_header:
            self.table.setColumnCount(5)
            self.table.setHorizontalHeaderLabels(['Kode Barang', 'Nama Barang', 'Jumlah Barang', 'Harga Barang', 'Keuntungan'])
            self.is_set_header = True

        for i, row in enumerate(result):
            self.table.insertRow(i)
            for j, value in enumerate(row[1:]):
                self.table.setItem(i, j, QTableWidgetItem(str(value)))

    def add_barang(self):
        self.cud_dialog = CudDialog(self.db, self.cursor)
        self.hide()
        self.cud_dialog.exec()
        self.load_data()
        self.show()

    def edit_barang(self):
        row_index = self.table.currentRow()
        if row_index >= 0:
            item = self.table.item(row_index, 0)
            if item is not None:
                kode_barang = item.text()
                self.cud_dialog = CudDialog(self.db, self.cursor, kode_barang)
                self.hide()
                self.cud_dialog.exec()
                self.load_data()
                self.show()

    def delete_barang(self):
        row_index = self.table.currentRow()
        if row_index >= 0:
            item = self.table.item(row_index, 0)
            if item is not None:
                kode_barang = item.text()
                self.cud_dialog = CudDialog(self.db, self.cursor, kode_barang)
                self.cud_dialog.delete_barang()
                self.load_data()

    def export_to_excel(self):
        self.cursor.execute("SELECT * FROM barang")
        result = self.cursor.fetchall()

        # convert result to pandas DataFrame
        df = pd.DataFrame(result, columns=['id', 'kode_barang', 'nama_barang', 'jumlah_barang', 'harga_barang', 'keuntungan'])

        file_path, _ = QFileDialog.getSaveFileName(self, "Export ke Excel", "", "Excel Files (*.xlsx)")

        if file_path:
            df.to_excel(file_path, index=False)
