from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit, QMessageBox
from PyQt6 import uic
import sys
import mysql.connector
from barang_window import BarangWindow

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi('app.ui', self)

        self.login_button = self.findChild(QPushButton, 'login_button')
        self.login_button.clicked.connect(self.login)

        self.username_field = self.findChild(QLineEdit, 'username_field')
        self.password_field = self.findChild(QLineEdit, 'password_field')

    def login(self):
        username = self.username_field.text()
        password = self.password_field.text()

        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="inventory"
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
