from PIL import Image
from matplotlib import pyplot as plt

from project.image_characteristics import get_brightness_histogram
from project.image_convertions import convert_to_gray, convert_pixel_to_gray


def otsu_method(rgb_data: list[tuple[int, int, int]], levels: int = 256) -> list[int]:
    """
    This functions provides Otsu method for automatic binarization

    Parameters
    ----------
    rgb_data: list[tuple[int, int, int]]
        Flatten list of rgb pixels
    levels: int
        Levels of brightness
    Returns
    -------
    binary_image: list[int]
        Flatten list with binary pixels
    """
    number_of_pixels = len(rgb_data)

    # 0 шаг --- перевод изображения в серое
    gray_data = convert_to_gray(rgb_data)

    # 1 шаг --- расчёт гистограммы яркости
    histogram = get_brightness_histogram(gray_data, levels)

    # 2 шаг --- нормализация гистограммы
    normalized_histogram = []
    for level, pixels in histogram:
        normalized_histogram.append(pixels / number_of_pixels)

    # 3 шаг --- цикл T от 1 до L-1
    best_t = 1  # T*
    max_variance = 0  # дисперсия при T*
    for t in range(1, levels - 1):
        # Гистограмма до T-1 и гистограмма с T до L-1
        first_part = normalized_histogram[:t]
        second_part = normalized_histogram[t:]

        # Вероятности классов
        omega_0 = sum(first_part)
        omega_1 = sum(second_part)
        if (
            omega_0 == 0 or omega_1 == 0
        ):  # Один из классов отсутствует, его вероятность нулевая
            continue

        # Средние яркости классов
        nu_0 = 1 / omega_0 * sum(map(lambda i, p_i: i * p_i, range(t), first_part))
        nu_1 = (
            1
            / omega_1
            * sum(map(lambda i, p_i: i * p_i, range(t, levels), second_part))
        )

        # Общая средняя яркость
        nu_t = omega_0 * nu_0 + omega_1 * nu_1

        # Межклассовая дисперсия
        variance = omega_0 * omega_1 * (nu_0 - nu_1) ** 2

        # 4 шаг --- найти T* при котором дисперсия максимальна
        if variance > max_variance:
            max_variance = variance
            best_t = t

    # 5 шаг --- использовать T* для бинаризации
    binary_image_m = binarization(rgb_data, threshold=best_t)

    return binary_image_m


def binarization(
    rgb_data: list[tuple[int, int, int]], threshold: int = 128
) -> list[int]:
    """
    Converting flatten list of RGB pixels to binary image.

    Parameters
    ----------
    rgb_data: list[tuple[int, int, int]]
        List of pixels in RGB mode
    threshold: int
        Threshold for pixel brightness

    Returns
    -------
    pixels:
        Grayscale pixels
    """
    return [0 if convert_pixel_to_gray(p) <= threshold else 255 for p in rgb_data]
