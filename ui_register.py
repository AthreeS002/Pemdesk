# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(499, 347)
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 110, 291, 51))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.edit_username = QLineEdit(self.verticalLayoutWidget)
        self.edit_username.setObjectName(u"edit_username")

        self.verticalLayout.addWidget(self.edit_username)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(190, 20, 151, 51))
        font = QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.verticalLayoutWidget_3 = QWidget(Form)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(320, 100, 160, 121))
        self.verticalLayout_9 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.btn_register = QPushButton(self.verticalLayoutWidget_3)
        self.btn_register.setObjectName(u"btn_register")
        self.btn_register.setMaximumSize(QSize(16777215, 50))
        font1 = QFont()
        font1.setPointSize(12)
        self.btn_register.setFont(font1)

        self.verticalLayout_9.addWidget(self.btn_register)

        self.btn_exit = QPushButton(self.verticalLayoutWidget_3)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setMaximumSize(QSize(16777215, 50))
        self.btn_exit.setFont(font1)

        self.verticalLayout_9.addWidget(self.btn_exit)

        self.verticalLayoutWidget_2 = QWidget(Form)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 230, 291, 48))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.edit_password_2 = QLineEdit(self.verticalLayoutWidget_2)
        self.edit_password_2.setObjectName(u"edit_password_2")

        self.verticalLayout_3.addWidget(self.edit_password_2)

        self.label_password = QLabel(self.verticalLayoutWidget_2)
        self.label_password.setObjectName(u"label_password")

        self.verticalLayout_3.addWidget(self.label_password)

        self.verticalLayoutWidget_4 = QWidget(Form)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(10, 170, 291, 51))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.edit_nama = QLineEdit(self.verticalLayoutWidget_4)
        self.edit_nama.setObjectName(u"edit_nama")

        self.verticalLayout_2.addWidget(self.edit_nama)

        self.label_3 = QLabel(self.verticalLayoutWidget_4)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Username", None))
        self.label.setText(QCoreApplication.translate("Form", u"Register Page", None))
        self.btn_register.setText(QCoreApplication.translate("Form", u"Registrasi", None))
        self.btn_exit.setText(QCoreApplication.translate("Form", u"Exit", None))
        self.label_password.setText(QCoreApplication.translate("Form", u"Password", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Nama", None))
    # retranslateUi

