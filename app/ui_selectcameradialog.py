# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'selectcameradialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class Ui_SelectCameraDialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName("Dialog")
        Dialog.resize(193, 110)
        self.cameraSelectLabel = QLabel(Dialog)
        self.cameraSelectLabel.setObjectName("cameraSelectLabel")
        self.cameraSelectLabel.setGeometry(QRect(10, 10, 151, 20))
        self.cameraSelectComboBox = QComboBox(Dialog)
        self.cameraSelectComboBox.setObjectName("cameraSelectComboBox")
        self.cameraSelectComboBox.setGeometry(QRect(10, 40, 171, 22))
        self.submitButton = QPushButton(Dialog)
        self.submitButton.setObjectName("submitButton")
        self.submitButton.setGeometry(QRect(10, 80, 75, 23))
        self.cancelButton = QPushButton(Dialog)
        self.cancelButton.setObjectName("cancelButton")
        self.cancelButton.setGeometry(QRect(110, 80, 75, 23))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", "Dialog", None))
        self.cameraSelectLabel.setText(
            QCoreApplication.translate(
                "Dialog",
                "\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043a\u0430\u043c\u0435\u0440\u0443",
                None,
            )
        )
        self.submitButton.setText(QCoreApplication.translate("Dialog", "OK", None))
        self.cancelButton.setText(QCoreApplication.translate("Dialog", "Cancel", None))

    # retranslateUi
