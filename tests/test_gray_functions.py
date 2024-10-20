import pytest
from project.image_convertions import convert_to_gray, convert_pixel_to_gray


@pytest.mark.parametrize(
    "rgb_pixel, expected_gray_pixel",
    [
        ((1, 2, 3), 1),
        ((2, 2, 2), 2),
        ((64, 128, 255), 123),
    ],
)
def test_pixel_to_gray(rgb_pixel, expected_gray_pixel):
    assert convert_pixel_to_gray(rgb_pixel) == expected_gray_pixel


@pytest.mark.parametrize(
    "flatten_rgb_list, expected_gray_list",
    [
        ([(1, 2, 3)], [1]),
        ([(1, 2, 3), (2, 2, 2), (64, 128, 255)], [1, 2, 123]),
    ],
)
def test_image_to_gray(flatten_rgb_list, expected_gray_list):
    assert convert_to_gray(flatten_rgb_list) == expected_gray_list
