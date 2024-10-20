def convert_pixel_to_gray(pixel: tuple[int, int, int]) -> int:
    """
    Converting RGB pixel to gray pixel.
    Coefficients for red_channel, green_channel and blue_channel is 0.2125, 0.7154, 0.0721 respectively

    Parameters
    ----------
    pixel: tuple[int, int, int]
        pixel in RGB mode
    Returns
    -------
    pixels: int
        Grayscale pixels
    """
    return int(0.2125 * pixel[0] + 0.7154 * pixel[1] + 0.0721 * pixel[2])


def convert_to_gray(rgb_data: list[tuple[int, int, int]]) -> list[int]:
    """
    Converting RGB Image.get_data to gray picture.

    Parameters
    ----------
    rgb_data: list[tuple[int, int, int]]
        List of pixels in RGB mode
    Returns
    -------
    pixels: list[int]
        Grayscale pixels
    """
    return [convert_pixel_to_gray(p) for p in rgb_data]
