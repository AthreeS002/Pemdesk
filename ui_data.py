# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'data.ui'
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
        Form.resize(705, 478)
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(39, 120, 411, 321))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.edit_id = QLineEdit(self.verticalLayoutWidget)
        self.edit_id.setObjectName(u"edit_id")
        self.edit_id.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout.addWidget(self.edit_id)

        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.edit_nama = QLineEdit(self.verticalLayoutWidget)
        self.edit_nama.setObjectName(u"edit_nama")
        self.edit_nama.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout.addWidget(self.edit_nama)

        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.edit_jumlah = QLineEdit(self.verticalLayoutWidget)
        self.edit_jumlah.setObjectName(u"edit_jumlah")
        self.edit_jumlah.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout.addWidget(self.edit_jumlah)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.edit_status = QLineEdit(self.verticalLayoutWidget)
        self.edit_status.setObjectName(u"edit_status")
        self.edit_status.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout.addWidget(self.edit_status)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.verticalLayoutWidget_2 = QWidget(Form)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(500, 190, 160, 251))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_add = QPushButton(self.verticalLayoutWidget_2)
        self.btn_add.setObjectName(u"btn_add")
        self.btn_add.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setPointSize(12)
        self.btn_add.setFont(font)

        self.verticalLayout_2.addWidget(self.btn_add)

        self.btn_update = QPushButton(self.verticalLayoutWidget_2)
        self.btn_update.setObjectName(u"btn_update")
        self.btn_update.setMaximumSize(QSize(16777215, 50))
        self.btn_update.setFont(font)

        self.verticalLayout_2.addWidget(self.btn_update)

        self.btn_delete = QPushButton(self.verticalLayoutWidget_2)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setMaximumSize(QSize(16777215, 50))
        self.btn_delete.setFont(font)

        self.verticalLayout_2.addWidget(self.btn_delete)

        self.btn_exit = QPushButton(self.verticalLayoutWidget_2)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setMaximumSize(QSize(16777215, 50))
        self.btn_exit.setFont(font)

        self.verticalLayout_2.addWidget(self.btn_exit)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(240, 30, 231, 41))
        font1 = QFont()
        font1.setPointSize(18)
        self.label_5.setFont(font1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"ID Barang", None))
        self.label.setText(QCoreApplication.translate("Form", u"Nama Barang", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Jumlah Barang", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Status Barang", None))
        self.btn_add.setText(QCoreApplication.translate("Form", u"Add Data", None))
        self.btn_update.setText(QCoreApplication.translate("Form", u"Edit Data", None))
        self.btn_delete.setText(QCoreApplication.translate("Form", u"Delete Data", None))
        self.btn_exit.setText(QCoreApplication.translate("Form", u"Exit", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Halaman Data Barang", None))
    # retranslateUi

