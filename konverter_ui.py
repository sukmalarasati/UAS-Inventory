import glob
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QMessageBox
import mysql.connector

def SQL():
    file = open("inventory.sql", "r")
    data = file.read()
    file.close()

    sql = []
    for i in data.split("\n"):
        if not i.strip().startswith("--") and i.strip() != "":
            sql.append(i)

    ret = "\n".join(sql).split(";")
    return ret

def UI():
    data = []
    files = []
    for i in glob.glob("*.ui") + glob.glob("*.ico"):
        file = open(i, "rb")
        data.append(file.read())
        file.close()

        if i.endswith(".ui"):
            files.append([i.replace(".", "_").replace("/", "_").replace("\\", "_").upper(), i])
        else:
            files.append((i.replace(".", "_").replace("/", "_").replace("\\", "_").upper(), i))


    payloads = ["## Dibuat oleh konverter_ui.py ##\nimport io, os\n"]

    for d,f in zip(data, files):
        if type(f) is list:
            payloads.append(f"{f[0]} = lambda: io.BytesIO({repr(d)})")
            print(f"{f[1]} -> ui.{f[0]}()")
        else:
            vn, fn = f
            payloads.append(f"""def {vn}():\n  try:\n    file = open("{fn}", "wb")\n    file.write({repr(d)})\n    file.flush()\n    file.close()\n  except:\n    pass\n  return "{fn}"\n""")
            print(f"{f[1]} -> ui.{f[0]}()")

    file = open("ui.py", "w")
    file.write("\n".join(payloads))
    file.flush()
    file.close()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MySQL Config InventorySukma")
        self.setGeometry(100, 100, 400, 400)

        label1 = QLabel(self)
        label1.setText("Mohon pastikan Anda memiliki MySQL server dan buatkan database untuk program InventorySukma sesuai yang Anda inginkan.")
        label1.setGeometry(50, 50, 300, 50)
        label1.setWordWrap(True)

        label2 = QLabel(self)
        label2.setText("MySQL Host:")
        label2.setGeometry(50, 100, 100, 30)

        self.mysql_host_input = QLineEdit(self)
        self.mysql_host_input.setGeometry(160, 100, 200, 30)

        label3 = QLabel(self)
        label3.setText("MySQL Username:")
        label3.setGeometry(50, 150, 100, 30)

        self.mysql_username_input = QLineEdit(self)
        self.mysql_username_input.setGeometry(160, 150, 200, 30)

        label4 = QLabel(self)
        label4.setText("MySQL Password:")
        label4.setGeometry(50, 200, 100, 30)

        self.mysql_password_input = QLineEdit(self)
        self.mysql_password_input.setGeometry(160, 200, 200, 30)
        self.mysql_password_input.setEchoMode(QLineEdit.EchoMode.Password)

        label5 = QLabel(self)
        label5.setText("MySQL Database:")
        label5.setGeometry(50, 250, 100, 30)

        self.mysql_database_input = QLineEdit(self)
        self.mysql_database_input.setGeometry(160, 250, 200, 30)

        build_button = QPushButton("Build", self)
        build_button.setGeometry(150, 300, 100, 30)
        build_button.clicked.connect(self.build_clicked)

    def build_clicked(self):
        mysql_host = self.mysql_host_input.text()
        mysql_username = self.mysql_username_input.text()
        mysql_password = self.mysql_password_input.text()
        mysql_database = self.mysql_database_input.text()

        try:
            db = mysql.connector.connect(
                host=mysql_host,
                user=mysql_username,
                password=mysql_password,
                database=mysql_database
            )
            cursor = db.cursor()
            for sql in SQL():
                cursor.execute(sql)
            db.commit()
            db.close()

            UI()

            data = [
                "",
                '# MySQL Config',
                f'HOST     = "{mysql_host}"',
                f'USERNAME = "{mysql_username}"',
                f'PASSWORD = "{mysql_password}"',
                f'DATABASE = "{mysql_database}"',
            ]

            file = open("ui.py", "a")
            file.write("\n".join(data))
            file.flush()
            file.close()
            self.close()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setText("Terjadi kesalaan MySQL config:\n" + str(e))
            msg.setWindowTitle("MySQL Error")
            msg.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())