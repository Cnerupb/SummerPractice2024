# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'drawrectdialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class Ui_DrawRectActionDialog(object):
    def setupUi(self, DrawRectActionDialog):
        if not DrawRectActionDialog.objectName():
            DrawRectActionDialog.setObjectName("DrawRectActionDialog")
        DrawRectActionDialog.resize(400, 213)
        self.gridLayoutWidget = QWidget(DrawRectActionDialog)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(-1, -1, 387, 171))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.LeftTopRectPosLabel = QLabel(self.gridLayoutWidget)
        self.LeftTopRectPosLabel.setObjectName("LeftTopRectPosLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.LeftTopRectPosLabel.sizePolicy().hasHeightForWidth()
        )
        self.LeftTopRectPosLabel.setSizePolicy(sizePolicy)
        self.LeftTopRectPosLabel.setBaseSize(QSize(0, 0))
        self.LeftTopRectPosLabel.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter
        )

        self.gridLayout.addWidget(self.LeftTopRectPosLabel, 0, 0, 1, 4)

        self.x2Label = QLabel(self.gridLayoutWidget)
        self.x2Label.setObjectName("x2Label")
        sizePolicy.setHeightForWidth(self.x2Label.sizePolicy().hasHeightForWidth())
        self.x2Label.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.x2Label, 3, 0, 1, 1)

        self.x1Label = QLabel(self.gridLayoutWidget)
        self.x1Label.setObjectName("x1Label")
        sizePolicy.setHeightForWidth(self.x1Label.sizePolicy().hasHeightForWidth())
        self.x1Label.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.x1Label, 1, 0, 1, 1)

        self.y2LineEdit = QLineEdit(self.gridLayoutWidget)
        self.y2LineEdit.setObjectName("y2LineEdit")
        sizePolicy.setHeightForWidth(self.y2LineEdit.sizePolicy().hasHeightForWidth())
        self.y2LineEdit.setSizePolicy(sizePolicy)
        self.y2LineEdit.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.y2LineEdit.setInputMethodHints(Qt.ImhDigitsOnly)

        self.gridLayout.addWidget(self.y2LineEdit, 3, 3, 1, 1)

        self.y1LineEdit = QLineEdit(self.gridLayoutWidget)
        self.y1LineEdit.setObjectName("y1LineEdit")
        sizePolicy.setHeightForWidth(self.y1LineEdit.sizePolicy().hasHeightForWidth())
        self.y1LineEdit.setSizePolicy(sizePolicy)
        self.y1LineEdit.setInputMethodHints(Qt.ImhDigitsOnly)

        self.gridLayout.addWidget(self.y1LineEdit, 1, 3, 1, 1)

        self.x1LineEdit = QLineEdit(self.gridLayoutWidget)
        self.x1LineEdit.setObjectName("x1LineEdit")
        sizePolicy.setHeightForWidth(self.x1LineEdit.sizePolicy().hasHeightForWidth())
        self.x1LineEdit.setSizePolicy(sizePolicy)
        self.x1LineEdit.setInputMethodHints(Qt.ImhDigitsOnly)

        self.gridLayout.addWidget(self.x1LineEdit, 1, 1, 1, 1)

        self.RightBottomRectPosLabel = QLabel(self.gridLayoutWidget)
        self.RightBottomRectPosLabel.setObjectName("RightBottomRectPosLabel")
        sizePolicy.setHeightForWidth(
            self.RightBottomRectPosLabel.sizePolicy().hasHeightForWidth()
        )
        self.RightBottomRectPosLabel.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.RightBottomRectPosLabel, 2, 0, 1, 4)

        self.x2LineEdit = QLineEdit(self.gridLayoutWidget)
        self.x2LineEdit.setObjectName("x2LineEdit")
        sizePolicy.setHeightForWidth(self.x2LineEdit.sizePolicy().hasHeightForWidth())
        self.x2LineEdit.setSizePolicy(sizePolicy)
        self.x2LineEdit.setInputMethodHints(Qt.ImhDigitsOnly)

        self.gridLayout.addWidget(self.x2LineEdit, 3, 1, 1, 1)

        self.y1Label = QLabel(self.gridLayoutWidget)
        self.y1Label.setObjectName("y1Label")
        sizePolicy.setHeightForWidth(self.y1Label.sizePolicy().hasHeightForWidth())
        self.y1Label.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.y1Label, 1, 2, 1, 1)

        self.y2Label = QLabel(self.gridLayoutWidget)
        self.y2Label.setObjectName("y2Label")
        sizePolicy.setHeightForWidth(self.y2Label.sizePolicy().hasHeightForWidth())
        self.y2Label.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.y2Label, 3, 2, 1, 1)

        self.submitButton = QPushButton(DrawRectActionDialog)
        self.submitButton.setObjectName("submitButton")
        self.submitButton.setGeometry(QRect(50, 180, 131, 23))
        self.cancelButton = QPushButton(DrawRectActionDialog)
        self.cancelButton.setObjectName("cancelButton")
        self.cancelButton.setGeometry(QRect(230, 180, 131, 23))

        self.retranslateUi(DrawRectActionDialog)

        QMetaObject.connectSlotsByName(DrawRectActionDialog)

    # setupUi

    def retranslateUi(self, DrawRectActionDialog):
        DrawRectActionDialog.setWindowTitle(
            QCoreApplication.translate("DrawRectActionDialog", "Dialog", None)
        )
        self.LeftTopRectPosLabel.setText(
            QCoreApplication.translate(
                "DrawRectActionDialog",
                "Input coordinates of top left corner (min: 0, max: 16777215)",
                None,
            )
        )
        self.x2Label.setText(
            QCoreApplication.translate("DrawRectActionDialog", "X2", None)
        )
        self.x1Label.setText(
            QCoreApplication.translate("DrawRectActionDialog", "X1", None)
        )
        self.RightBottomRectPosLabel.setText(
            QCoreApplication.translate(
                "DrawRectActionDialog",
                "Input coordinates of bottom right corner (min: 0, max: 16777215)",
                None,
            )
        )
        self.y1Label.setText(
            QCoreApplication.translate("DrawRectActionDialog", "Y1", None)
        )
        self.y2Label.setText(
            QCoreApplication.translate("DrawRectActionDialog", "Y2", None)
        )
        self.submitButton.setText(
            QCoreApplication.translate("DrawRectActionDialog", "OK", None)
        )
        self.cancelButton.setText(
            QCoreApplication.translate("DrawRectActionDialog", "Cancel", None)
        )

    # retranslateUi
