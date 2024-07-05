from typing import Tuple

import numpy
import cv2


def load_image(img_path: str):
    """Load image from specific path

    Args:
        img_path (str): path to image

    Returns:
        cv.typing.MatLike: loaded image
    """
    with open(img_path, "rb") as file:
        bytes_array = bytearray(file.read())
        numpy_array = numpy.asarray(bytes_array, dtype=numpy.uint8)
        img = cv2.imdecode(numpy_array, cv2.IMREAD_UNCHANGED)
    return img


def save_image(img, img_name: str) -> bool:
    """Save image to specific path

    Args:
        img (cv.typing.MatLike): _description_
        img_name (str): _description_

    Returns:
        bool: _description_
    """
    return cv2.imwrite(filename=img_name, img=img)


def change_size(img, size: Tuple[int, int]):
    """Resizes image

    Args:
        img (cv.typing.MatLike): input image
        size (Tuple[int, int]): resulting size

    Returns:
        cv.typing.MatLike: resulting image
    """
    return cv2.resize(src=img.copy(), dsize=size)


def change_brightness(
    inp_img, brightness: float
):
    """_summary_

    Args:
        inp_img (cv.Umat): cv loaded image
        brightness (float): -255 (all black) to +255 (all white)

    Returns:
        cv.Umat: result image
    """
    if not (-255 <= brightness <= 255):
        raise ValueError("Argument brightness must be in range of -255 to 255!")

    img = inp_img.copy()
    cv2.convertScaleAbs(src=img, dst=img, alpha=1, beta=brightness)
    return img


def draw_rect(
    img, x1: int, y1: int, x2: int, y2: int
):
    """Draws a blue color rect on image

    Args:
        img (cv.Umat): input image
        x1 (int): left top corner x coord
        y1 (int): left top corner y coord
        x2 (int): right bottom corner x coord
        y2 (int): right bottom corner y coord

    Returns:
        cv.Umat: result image
    """
    img = cv2.rectangle(img.copy(), (x1, y1), (x2, y2), color=(255, 0, 0), thickness=2)
    return img
