import cv2 as cv
from typing import Tuple
from numpy import int8


def load_image(img_path: str) -> cv.typing.MatLike:
    """Load image from specific path

    Args:
        img_path (str): path to image

    Returns:
        cv.typing.MatLike: loaded image
    """
    return cv.imread(filename=img_path)


def save_image(img: cv.typing.MatLike, img_name: str) -> bool:
    """Save image to specific path

    Args:
        img (cv.typing.MatLike): _description_
        img_name (str): _description_

    Returns:
        bool: _description_
    """
    return cv.imwrite(filename=img_name, img=img)


def change_size(img: cv.typing.MatLike, size: Tuple[int, int]) -> cv.typing.MatLike:
    """Resizes image

    Args:
        img (cv.typing.MatLike): input image
        size (Tuple[int, int]): resulting size

    Returns:
        cv.typing.MatLike: resulting image
    """
    return cv.resize(src=img, dsize=size)


def change_brightness(
    inp_img: cv.typing.MatLike, brightness: float
) -> cv.typing.MatLike:
    """_summary_

    Args:
        img (cv.Umat): cv loaded image
        brightness (int8): -255 (all black) to +255 (all white)

    Returns:
        cv.Umat: result image
    """
    if not (-255 <= brightness <= 255):
        raise ValueError("Argument brightness must be in range of -255 to 255!")

    img = inp_img.copy()
    cv.convertScaleAbs(src=img, dst=img, alpha=1, beta=brightness)
    return img


def draw_rect(img: cv.typing.MatLike, x1: int, y1, x2, y2) -> cv.typing.MatLike:
    """Draws a blue color rect on image

    Args:
        img (cv.Umat): inpu image
        x1 (int): left top corner x coord
        y1 (int): left top corner y coord
        x2 (int): right bottom corner x coord
        y2 (int): right bottom corner y coord

    Returns:
        cv.Umat: result image
    """
    cv.rectangle(img, (x1, y1), (x2, y2), color=(0, 0, 255), thickness=2)
    return img
