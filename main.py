import sys
import logging

from PySide2 import QtWidgets
from app.gui import MainWindow
from app.ui_mainwindow import Ui_MainWindow


def main(*args):
    logging.basicConfig(level=logging.INFO)
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
