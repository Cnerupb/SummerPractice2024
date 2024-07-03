import sys
from PySide2 import QtWidgets
from gui import MainWindow


def main(*args):
    # print(PySide2.__version__)
    # print(PySide2.QtCore.__version__)  # type: ignore
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
