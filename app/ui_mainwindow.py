# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionLoadFromFile = QAction(MainWindow)
        self.actionLoadFromFile.setObjectName("actionLoadFromFile")
        self.actionLoadFromCamera = QAction(MainWindow)
        self.actionLoadFromCamera.setObjectName("actionLoadFromCamera")
        self.actionResize = QAction(MainWindow)
        self.actionResize.setObjectName("actionResize")
        self.actionBrightness = QAction(MainWindow)
        self.actionBrightness.setObjectName("actionBrightness")
        self.actionRect = QAction(MainWindow)
        self.actionRect.setObjectName("actionRect")
        self.actionAll = QAction(MainWindow)
        self.actionAll.setObjectName("actionAll")
        self.actionRed = QAction(MainWindow)
        self.actionRed.setObjectName("actionRed")
        self.actionGreen = QAction(MainWindow)
        self.actionGreen.setObjectName("actionGreen")
        self.actionBlue = QAction(MainWindow)
        self.actionBlue.setObjectName("actionBlue")
        self.actionVisitSite = QAction(MainWindow)
        self.actionVisitSite.setObjectName("actionVisitSite")

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, -0, 800, 560))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.ImageLabel = QLabel(self.verticalLayoutWidget)
        self.ImageLabel.setObjectName("ImageLabel")
        self.ImageLabel.setGeometry(QRect(1, 0, 800, 550))
        sizePolicy.setHeightForWidth(self.ImageLabel.sizePolicy().hasHeightForWidth())
        self.ImageLabel.setSizePolicy(sizePolicy)
        self.ImageLabel.setFrameShape(QFrame.Panel)
        self.ImageLabel.setPixmap(QPixmap(""))
        self.ImageLabel.setScaledContents(True)
        self.ImageLabel.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.ImageLabel, alignment=Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuDraw = QMenu(self.menubar)
        self.menuDraw.setObjectName("menuDraw")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuChannels = QMenu(self.menubar)
        self.menuChannels.setObjectName("menuChannels")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuDraw.menuAction())
        self.menubar.addAction(self.menuChannels.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.menuFile.addAction(self.actionLoadFromFile)
        self.menuFile.addAction(self.actionLoadFromCamera)
        self.menuFile.addAction(self.actionSave)
        self.menuEdit.addAction(self.actionResize)
        self.menuEdit.addAction(self.actionBrightness)
        self.menuDraw.addAction(self.actionRect)
        self.menuChannels.addAction(self.actionAll)
        self.menuChannels.addAction(self.actionRed)
        self.menuChannels.addAction(self.actionGreen)
        self.menuChannels.addAction(self.actionBlue)
        self.menuHelp.addAction(self.actionVisitSite)

        self.actionLoadFromFile.triggered.connect(self.load_image)
        self.actionLoadFromCamera.triggered.connect(self.load_image_from_camera)
        self.actionSave.triggered.connect(self.save_image)
        self.actionResize.triggered.connect(self.resize_image)
        self.actionBrightness.triggered.connect(self.set_brightness)
        self.actionRect.triggered.connect(self.draw_rectangle)
        self.actionAll.triggered.connect(self.set_all_channel)
        self.actionRed.triggered.connect(self.set_red_channel)
        self.actionGreen.triggered.connect(self.set_green_channel)
        self.actionBlue.triggered.connect(self.set_blue_channel)
        self.actionVisitSite.triggered.connect(self.show_help)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.actionLoadFromFile.setText(
            QCoreApplication.translate("MainWindow", "Load from File", None)
        )
        self.actionLoadFromCamera.setText(
            QCoreApplication.translate("MainWindow", "Load from Camera", None)
        )
        self.actionSave.setText(QCoreApplication.translate("MainWindow", "Save", None))
        self.actionResize.setText(
            QCoreApplication.translate("MainWindow", "Size", None)
        )
        self.actionBrightness.setText(
            QCoreApplication.translate("MainWindow", "Brightness", None)
        )
        self.actionRect.setText(QCoreApplication.translate("MainWindow", "Rect", None))
        self.actionAll.setText(QCoreApplication.translate("MainWindow", "All", None))
        self.actionRed.setText(QCoreApplication.translate("MainWindow", "Red", None))
        self.actionGreen.setText(
            QCoreApplication.translate("MainWindow", "Green", None)
        )
        self.actionBlue.setText(QCoreApplication.translate("MainWindow", "Blue", None))
        self.actionVisitSite.setText(QCoreApplication.translate("MainWindow", "Visit Site", None))
        self.ImageLabel.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", "File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", "Edit", None))
        self.menuDraw.setTitle(QCoreApplication.translate("MainWindow", "Draw", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", "Help", None))
        self.menuChannels.setTitle(
            QCoreApplication.translate("MainWindow", "Channels", None)
        )

    # re translate Ui
    def load_image(self):
        pass

    def load_image_from_camera(self):
        pass

    def save_image(self):
        pass

    def resize_image(self):
        pass

    def set_brightness(self):
        pass

    def draw_rectangle(self):
        pass

    def set_all_channel(self):
        pass

    def set_red_channel(self):
        pass

    def set_green_channel(self):
        pass

    def set_blue_channel(self):
        pass

    def show_help(self):
        pass
