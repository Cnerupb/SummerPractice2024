# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'resizeimageactiondialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class Ui_ResizeImageActionDialog(object):
    def setupUi(self, ResizeImageActionDialog):
        if not ResizeImageActionDialog.objectName():
            ResizeImageActionDialog.setObjectName("ResizeImageActionDialog")
        ResizeImageActionDialog.resize(180, 120)

        self.gridLayoutWidget = QWidget(ResizeImageActionDialog)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 180, 121))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)

        self.CancelButton = QPushButton(self.gridLayoutWidget)
        self.CancelButton.setObjectName("CancelButton")

        self.gridLayout.addWidget(self.CancelButton, 2, 1, 1, 1)

        self.WidthLabel = QLabel(self.gridLayoutWidget)
        self.WidthLabel.setObjectName("WidthLabel")

        self.gridLayout.addWidget(self.WidthLabel, 0, 0, 1, 1)

        self.SubmitButton = QPushButton(self.gridLayoutWidget)
        self.SubmitButton.setObjectName("SubmitButton")

        self.gridLayout.addWidget(self.SubmitButton, 2, 0, 1, 1)

        self.WidthLine = QLineEdit(self.gridLayoutWidget)
        self.WidthLine.setObjectName("WidthLine")

        self.gridLayout.addWidget(self.WidthLine, 1, 1, 1, 1)

        self.HeightLabel = QLabel(self.gridLayoutWidget)
        self.HeightLabel.setObjectName("HeightLabel")

        self.gridLayout.addWidget(self.HeightLabel, 1, 0, 1, 1)

        self.HeightLine = QLineEdit(self.gridLayoutWidget)
        self.HeightLine.setObjectName("HeightLine")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HeightLine.sizePolicy().hasHeightForWidth())
        self.HeightLine.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.HeightLine, 0, 1, 1, 1)

        QWidget.setTabOrder(self.WidthLine, self.HeightLine)
        QWidget.setTabOrder(self.HeightLine, self.SubmitButton)
        QWidget.setTabOrder(self.SubmitButton, self.CancelButton)

        self.retranslateUi(ResizeImageActionDialog)

        QMetaObject.connectSlotsByName(ResizeImageActionDialog)

    # setupUi

    def retranslateUi(self, ResizeImageActionDialog):
        ResizeImageActionDialog.setWindowTitle(
            QCoreApplication.translate("ResizeImageActionDialog", "Dialog", None)
        )
        self.CancelButton.setText(
            QCoreApplication.translate("ResizeImageActionDialog", "Cancel", None)
        )
        self.WidthLabel.setText(
            QCoreApplication.translate("ResizeImageActionDialog", "Input Width", None)
        )
        self.SubmitButton.setText(
            QCoreApplication.translate("ResizeImageActionDialog", "Submit", None)
        )
        self.WidthLine.setText("")
        self.HeightLabel.setText(
            QCoreApplication.translate("ResizeImageActionDialog", "Input Height", None)
        )

    # retranslateUi
