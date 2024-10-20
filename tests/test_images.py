import pytest
from project.binary_images import otsu_method
from PIL import Image


@pytest.mark.parametrize(
    "path, expected",
    [
        ("tests/data/1_pixel.jpg", [255]),
        ("tests/data/empty_black.jpg", [0] * 256),
        ("tests/data/empty_white.jpg", [255] * 256),
        ("tests/data/high_contrast.jpg", [255] * 16 * 7 + [0] * 16 * 2 + [255] * 16 * 7),
    ],
)
def test_image_binarization(path, expected):
    image = Image.open(path)
    actual_binary = otsu_method(image)
    assert actual_binary == expected


@pytest.mark.parametrize(
    "path",
    [
        ("tests/data/1_pixel.jpg"),
        ("tests/data/empty_black.jpg"),
        ("tests/data/empty_white.jpg"),
        ("tests/data/gradient.jpg"),
        ("tests/data/high_contrast.jpg"),
        ("tests/data/high_contrast_color.jpg"),
        ("tests/data/monotonic.jpg"),
        ("tests/data/noise.jpg"),
        ("tests/data/noised_color.jpg"),
        ("tests/data/non_square.jpg"),
        ("tests/data/text.jpg"),
    ],
)
def test_picture_proccessing(path):
    image = Image.open(path)
    actual_binary = otsu_method(image)
    assert isinstance(
        actual_binary, list
    )  # Мы действительно получаем список из метода оцу
    assert all(
        isinstance(pixel, int) for pixel in actual_binary
    )  # это плоский список, каждый элемент целое число
    assert all(
        0 <= pixel <= 255 for pixel in actual_binary
    )  # каждое число не выходит за границы уровня яркости
    assert (
        len(actual_binary) == image.width * image.height
    )  # количество чисел (пикселей) совпадает с исходным
