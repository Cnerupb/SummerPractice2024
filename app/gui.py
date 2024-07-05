from typing import List

import app.editor as editor
from app import exceptions
from app.ui_mainwindow import Ui_MainWindow
from app.ui_resizeimageactiondialog import Ui_ResizeImageActionDialog
from app.ui_drawrectactiondialog import Ui_DrawRectActionDialog

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore
import cv2


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Main Window class
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.image_path: str = ""
        self.image: cv2.typing.MatLike = None
        self.output_image: cv2.typing.MatLike = None

    def resizeEvent(self, event):
        self.verticalLayoutWidget.resize(self.width(), self.height())

    def check_if_image_exist(self, error_title, error_message) -> bool:
        if self.image is None:
            error_message = ErrorMessage(self, error_title, error_message)
            error_message.exec_()
            return False
        return True

    def update_pixmap(self):
        """
        Converts a cv2 format image to Pixmap format images and replaces the old one with it
        """
        pixmap = self.convert_mat_like_to_pixmap(self.output_image)
        self.ImageLabel.resize(pixmap.width(), pixmap.height())
        self.ImageLabel.setPixmap(pixmap)

    def loadImage(self):
        """
        Method on action Load in menu bar.
        Loads image on Pixmap. Asks user which image load
        """
        file_dialog = DialogOnActionLoad()

        if not file_dialog.exec_():
            return

        files = file_dialog.selectedFiles()
        if len(files) != 1:  # Only one file should be selected
            error_dialog = ErrorMessage(self, "Load error", "Choose one file!")
            error_dialog.exec_()
            return

        image_path = files[0]
        try:
            image = editor.load_image(image_path)

            if image is None:
                raise exceptions.BrokenImageException(
                    "Unable to open a corrupted image!"
                )

            self.image_path = image_path
            self.image = image
            self.output_image = self.image.copy()
            self.update_pixmap()

            message_on_success = SuccessMessage(self, "", "Image loaded successfully")
            message_on_success.exec_()
        except Exception as e:
            print(e)
            error_dialog = ErrorMessage(self, "Load Error", "Image is corrupted")
            error_dialog.exec_()

    def saveImage(self):
        """
        Method on action Save in menu bar.
        Saves image in .png or .jpg format in path. Asks user where save image
        Returns:

        """
        # Attempt to save unloaded image
        if not self.check_if_image_exist(
                "Image saving error", "Nothing to save. Load image first"
        ):
            return

        filename, _ = QFileDialog.getSaveFileName(
            self, "Saved_image", ".", "Images (*.png *.jpg);;All Files (*)"
        )
        if not filename:
            return

        cv2.imwrite(filename, self.output_image)

        message_on_success = SuccessMessage(self, "", "Image saved successfully")
        message_on_success.exec_()

    def resizeImage(self):
        """
        Method of action Size in menu bar.
        Resizes loaded image and shows changed image
        """
        # Attempt to resize nothing
        if not self.check_if_image_exist(
                "Image resizing error", "Nothing to resize. Load image first"
        ):
            return

        dialog = DialogOnActionResizeImage(self)
        if not dialog.exec_():
            return
        width, height = dialog.get_line_edit_values()
        print(width)
        print(height)
        if not any(
                [self.validate_width_height(width), self.validate_width_height(height)]
        ):
            error_message = ErrorMessage(
                self,
                "Invalid values",
                "width and height must be in range of 0 and 16777215",
            )
            error_message.exec_()
            return

        width, height = int(width), int(height)
        dim = (height, width)

        self.image = cv2.resize(self.image, dim, interpolation=cv2.INTER_AREA)
        self.output_image = self.image.copy()
        self.update_pixmap()

        message_on_success = SuccessMessage(self, "", "Image resized successfully")
        message_on_success.exec_()

    def setBrightness(self):
        """
        Method of Brightness in menu bar.
        Changes brightness of loaded image. Shows changed image
        """
        if not self.check_if_image_exist("Brightness set error", "No image detected"):
            return

        dialog = QInputDialog(self)
        brightness, ok = dialog.getText(
            self,
            "Input brightness",
            "Input brightness value (-255 to +255)",
            QLineEdit.Normal,
        )
        if not ok:
            return
        if not self.validate_brightness(brightness):
            error_message = ErrorMessage(
                self,
                "Brightness setting error",
                "Brightness must be in range of -255 and +255",
            )
            error_message.exec_()
            return

        brightness = int(brightness)
        self.image = editor.change_brightness(self.image, brightness).copy()
        self.output_image = self.image.copy()
        self.update_pixmap()

        message_on_success = SuccessMessage(self, "", "Brightness changed successfully")
        message_on_success.exec_()

    def drawRectangle(self):
        """
        Method of action Rect in menu bar.
        Draws blue rectangle on image. Changes and shows image on screen
        """
        print("Before if")
        if not self.check_if_image_exist("Rectangle draw error", "No image found"):
            return
        print("After if")
        print("Gotcha")
        dialog = DialogOnActionDrawRect(self)
        if not dialog.exec_():
            return

        coordinates = dialog.get_line_edit_values()
        if not all(map(self.validate_rect_coord, coordinates)):
            error_message = ErrorMessage(
                self,
                "Coordinates validation error",
                "Coordinates must be in range of 0 and 16777215",
            )
            error_message.exec_()
            return

        coordinates = list(map(int, coordinates))
        self.image = editor.draw_rect(self.image, *coordinates)
        self.output_image = self.image.copy()
        self.update_pixmap()

        success_message = SuccessMessage(self, "", "Rect drawn")
        success_message.exec_()

    def setAllChannel(self):
        """
        Changes color channels of image to All
        """
        self.output_image = self.image.copy()
        self.update_pixmap()

    def setRedChannel(self):
        """
        Changes color channels of image to Red only
        """
        b = self.image.copy()
        # set green and red channels to 0
        b[:, :, 0] = 0
        b[:, :, 1] = 0
        self.output_image = b
        self.update_pixmap()

    def setGreenChannel(self):
        """
        Changes color channels of image to Green only
        """
        b = self.image.copy()
        # set green and red channels to 0
        b[:, :, 0] = 0
        b[:, :, 2] = 0
        self.output_image = b
        self.update_pixmap()

    def setBlueChannel(self):
        """
        Changes color channels of image to Blue only
        """
        b = self.image.copy()
        # set green and red channels to 0
        b[:, :, 1] = 0
        b[:, :, 2] = 0
        self.output_image = b
        self.update_pixmap()

    @staticmethod
    def convert_mat_like_to_pixmap(image: cv2.typing.MatLike) -> QPixmap:
        """
        Converts cv2 image format
        Args:
            image: image of cv2 format

        Returns:
            image represented in QPixmap class
        """
        image = image.copy()

        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        height, width, channel = image.shape
        bytes_per_line = 3 * width
        q_image = QImage(
            rgb_image.data, width, height, bytes_per_line, QImage.Format_RGB888
        )
        return QPixmap.fromImage(q_image)

    @staticmethod
    def convert_single_channel_mat_like_to_pixmap(image: cv2.typing.MatLike):
        """
        Converts cv2 image format
        Args:
            image: single channel image of cv2 format

        Returns:
            image represented in QPixmap class
        """
        image = image.copy()

        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        height, width = image.shape
        bytes_per_line = 3 * width
        q_image = QImage(
            rgb_image.data, width, height, bytes_per_line, QImage.Format_RGB888
        )
        return QPixmap.fromImage(q_image)

    @staticmethod
    def validate_width_height(value: str) -> bool:
        """
        Validates value on width or height standards
        Args:
            value: value to validate

        Returns:
            result of validation: True or False
        """
        try:
            int_value = int(value)
            return 0 <= int_value <= 16777215
        except Exception:
            return False

    @staticmethod
    def validate_brightness(value: str) -> bool:
        """
        Validates value on brightness standards
        Args:
            value: value to validate

        Returns:
            result of validation: True or False
        """
        try:
            int_brightness = int(value)
            return -255 <= int_brightness <= 255
        except Exception:
            return False

    @staticmethod
    def validate_rect_coord(value: str) -> bool:
        """
        Validates value on rectangle coordinates standards
        Args:
            value: value to validate

        Returns:
            result of validation: True or False
        """
        try:
            int_coord = int(value)
            return 0 <= int_coord <= 16777215
        except Exception:
            return False


class DialogOnActionLoad(QFileDialog):
    """
    Dialog used when Load action in menu bar was called
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFileMode(QFileDialog.FileMode.ExistingFiles)
        self.setNameFilter("Images (*.png *.jpg)")
        self.setViewMode(QFileDialog.List)
        self.setModal = True


class DialogOnActionSave(QFileDialog):
    """
    Dialog used when Save action in menu bar was called
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFileMode(QFileDialog.FileMode.AnyFile)
        self.setNameFilter("Images (*.png *.jpg);;All Files (*)")
        self.setViewMode(QFileDialog.List)
        self.setModal = True


class DialogOnActionResizeImage(QDialog, Ui_ResizeImageActionDialog):
    """
    Dialog used when Size action in menu bar was called
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Input size in pixels")
        self.SubmitButton.clicked.connect(self.accept)
        self.CancelButton.clicked.connect(self.reject)
        self.setModal(True)

    def get_line_edit_values(self) -> List[str]:
        return [self.WidthLine.text(), self.HeightLine.text()]


class DialogOnActionDrawRect(QDialog, Ui_DrawRectActionDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Input rect coordinates")
        self.submitButton.clicked.connect(self.accept)
        self.cancelButton.clicked.connect(self.reject)
        self.setModal(True)

    def get_line_edit_values(self) -> List[str]:
        return [
            self.x1LineEdit.text(),
            self.y1LineEdit.text(),
            self.x2LineEdit.text(),
            self.y2LineEdit.text(),
        ]


class SuccessMessage(QMessageBox):
    def __init__(self, parent, title, text):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setText(text)
        self.addButton("Ok", QMessageBox.ButtonRole.AcceptRole)
        self.setModal(True)


class ErrorMessage(QMessageBox):
    def __init__(self, parent, title, text):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setText(text)
        self.addButton("Ok", QMessageBox.ButtonRole.AcceptRole)
        self.setIcon(QMessageBox.Critical)
        self.setModal(True)
