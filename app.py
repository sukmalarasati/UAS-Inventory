from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit, QMessageBox
from PyQt6 import uic, QtGui
import sys
import mysql.connector
from barang_window import BarangWindow
import ui

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi(ui.APP_UI(), self)
        self.setWindowIcon(QtGui.QIcon(ui.STOCK_ICO()))

        self.login_button = self.findChild(QPushButton, 'login_button')
        self.login_button.clicked.connect(self.login)

        self.username_field = self.findChild(QLineEdit, 'username_field')
        self.password_field = self.findChild(QLineEdit, 'password_field')

    def login(self):
        username = self.username_field.text()
        password = self.password_field.text()

        db = mysql.connector.connect(
            host=ui.HOST,
            user=ui.USERNAME,
            password=ui.PASSWORD,
            database=ui.DATABASE
        )
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password,))
        result = cursor.fetchone()

        if result:
            self.barang_window = BarangWindow()
            self.barang_window.show()
            self.close()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setText("Username atau password salah")
            msg.setWindowTitle("Login Gagal")
            msg.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyApp()
    window.show()

    sys.exit(app.exec())
