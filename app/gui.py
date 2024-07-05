from typing import List

import app.editor as editor
from app import exceptions
from app.ui_mainwindow import Ui_MainWindow
from app.ui_selectcameradialog import Ui_SelectCameraDialog
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
        self.setWindowTitle("Image Editor")

        self.image_path: str = ""
        self.image = None
        self.output_image= None

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

    def load_image(self):
        """
        Method on action Load in menu bar.
        Loads image on Pixmap. Asks user which image load
        """
        file_dialog = DialogOnActionLoadFromFile(self)

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

            message_on_success = SuccessMessage(self, "Image load status", "Image loaded successfully")
            message_on_success.exec_()
        except Exception as e:
            print(e)
            error_dialog = ErrorMessage(self, "Load Error", "Image is corrupted")
            error_dialog.exec_()

    def load_image_from_camera(self):
        # ports = self.get_list_of_camera_ports()
        #
        # select_camera_dialog = DialogOnActionLoadFromCamera(self, ports)
        # if not select_camera_dialog.exec_():
        #     return
        #
        # selected_port = select_camera_dialog.cameraSelectComboBox.currentText()
        # if selected_port == "":
        #     return
        #
        # selected_port = int(selected_port)
        cam = cv2.VideoCapture(cv2.CAP_DSHOW)

        # reading the input using the camera
        result, image = cam.read()

        # If image will detect with any error,
        if not result:
            error_msg = ErrorMessage(self, "Camera capturing error",
                                     "Error occurred due to camera connecting. Please, check is camera working")
            error_msg.exec_()
            return

        self.image = image
        self.output_image = self.image.copy()
        self.update_pixmap()

        success_message = SuccessMessage(self, "Image load status", "Image loaded")
        success_message.exec_()

    def save_image(self):
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

    def resize_image(self):
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

    def set_brightness(self):
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

    def draw_rectangle(self):
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

    def set_all_channel(self):
        """
        Changes color channels of image to All
        """
        if self.image is None:
            error_message = ErrorMessage(self, "Channel error", "Select image first")
            error_message.exec_()
            return
        self.output_image = self.image.copy()
        self.update_pixmap()

    def set_red_channel(self):
        """
        Changes color channels of image to Red only
        """
        if self.image is None:
            error_message = ErrorMessage(self, "Channel error", "Select image first")
            error_message.exec_()
            return
        b = self.image.copy()
        # set green and red channels to 0
        b[:, :, 0] = 0
        b[:, :, 1] = 0
        self.output_image = b
        self.update_pixmap()

    def set_green_channel(self):
        """
        Changes color channels of image to Green only
        """
        if self.image is None:
            error_message = ErrorMessage(self, "Channel error", "Select image first")
            error_message.exec_()
            return
        b = self.image.copy()
        # set green and red channels to 0
        b[:, :, 0] = 0
        b[:, :, 2] = 0
        self.output_image = b
        self.update_pixmap()

    def set_blue_channel(self):
        """
        Changes color channels of image to Blue only
        """
        if self.image is None:
            error_message = ErrorMessage(self, "Channel error", "Select image first")
            error_message.exec_()
            return
        b = self.image.copy()
        # set green and red channels to 0
        b[:, :, 1] = 0
        b[:, :, 2] = 0
        self.output_image = b
        self.update_pixmap()

    @staticmethod
    def get_list_of_camera_ports():
        # """
        # Test the ports and returns a tuple with the available ports and the ones that are working.
        # """
        # non_working_ports = []
        # dev_port = 0
        # working_ports = []
        # available_ports = []
        # while (
        #     len(non_working_ports) < 6
        # ):  # if there are more than 5 non-working ports stop the testing.
        #     camera = cv2.VideoCapture(dev_port)
        #     if not camera.isOpened():
        #         non_working_ports.append(dev_port)
        #         print("Port %s is not working." % dev_port)
        #     else:
        #         is_reading, img = camera.read()
        #         w = camera.get(3)
        #         h = camera.get(4)
        #         if is_reading:
        #             print(
        #                 "Port %s is working and reads images (%s x %s)"
        #                 % (dev_port, h, w)
        #             )
        #             working_ports.append(dev_port)
        #         else:
        #             print(
        #                 "Port %s for camera ( %s x %s) is present but does not read."
        #                 % (dev_port, h, w)
        #             )
        #             available_ports.append(dev_port)
        #     dev_port += 1
        # return available_ports, working_ports, non_working_ports
        available_cameras = []
        for i in range(10):
            cap = cv2.VideoCapture(i)
            if cap.isOpened():
                available_cameras.append(i)
                cap.release()
        return available_cameras

    @staticmethod
    def convert_mat_like_to_pixmap(image) -> QPixmap:
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
    def convert_single_channel_mat_like_to_pixmap(image):
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


class DialogOnActionLoadFromFile(QFileDialog):
    """
    Dialog used when Load action in menu bar was called
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Choose file")
        self.setFileMode(QFileDialog.ExistingFile)
        self.setNameFilter("Images (*.png *.jpg)")
        self.setModal(True)


class DialogOnActionLoadFromCamera(QDialog, Ui_SelectCameraDialog):
    def __init__(self, parent=None, port_list=None):
        super().__init__(parent)
        if port_list is None:
            port_list = [""]
        self.setupUi(self)
        self.submitButton.clicked.connect(self.accept)
        self.cancelButton.clicked.connect(self.reject)
        self.setModal(True)
        self.add_cameras(port_list)

    def add_cameras(self, port_list):
        self.cameraSelectComboBox.addItems(map(str, port_list))


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
    """
    Dialog used when Rect action in menu bar was called
    """

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
    """
    Message when some Action is complete right
    """

    def __init__(self, parent, title, text):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setText(text)
        self.addButton("Ok", QMessageBox.ButtonRole.AcceptRole)
        self.setModal(True)


class ErrorMessage(QMessageBox):
    """
    Message when some Action is complete not right
    """

    def __init__(self, parent, title, text):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setText(text)
        self.addButton("Ok", QMessageBox.ButtonRole.AcceptRole)
        self.setIcon(QMessageBox.Critical)
        self.setModal(True)
