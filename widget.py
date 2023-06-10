# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QMainWindow
from PySide6.QtUiTools import QUiLoader


from PySide6 import QtWidgets, QtGui
import mysql.connector as mc
import xlrd
import pandas as pd
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.btn_login.clicked.connect(self.login)
        self.ui.btn_exit.clicked.connect(self.close)

    def login(self):
        username = self.ui.edit_username.text()
        password = self.ui.edit_password_2.text()

        db = mc.connect(
        host="localhost",
        user="root",
        password="",
        database="pemdesk"
        )
        cursor = db.cursor()

        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        values = (username, password)
        cursor.execute(query, values)
        result = cursor.fetchone()

        if result is not None:
            for i in result:
#                QMessageBox.information(self, "Login successful", "Welcome to the dashboard!")
                self.close()
                self.halo()
                break
        else:
            QMessageBox.warning(self, "Login error", "Invalid username or password")

    def halo(self):
        """Open a dialog for creating a new account."""
        self.create_new_user_window = Ui_mainwindow()
        self.create_new_user_window.show()

class Ui_mainwindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        loader = QUiLoader()
        self.ui = loader.load("mainwindow.ui")
        self.setCentralWidget(self.ui)

        self.ui.btn_data.clicked.connect(self.data)
        self.ui.btn_exit.clicked.connect(self.close)


    def data(self):
        """Open a dialog for creating a new account."""
        self.create_new_user_window = Ui_data()
        self.create_new_user_window.show()
        self.close()

class Ui_data(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
           super().__init__(parent)
           loader = QUiLoader()
           self.ui = loader.load("coba.ui")
           self.setCentralWidget(self.ui)

           self.ui.btn_exit.clicked.connect(self.close)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())