from PIL import Image


def transform_image_to_matrix(image: Image.Image) -> list[list[int]]:
    """
    This function transform gray Image to matrix of pixel brightness

    Parameters
    ----------
    image: Image.Image
        single layer gray scaled image

    Returns
    -------
    matrix: list[list[int]]
        Matrix of pixel brightness
    """
    res: list[list[int]] = [[] for _ in range(image.width)]
    for x in range(image.width):
        for y in range(image.height):
            clr = image.getpixel(xy=(x, y))  # значение пикселя
            if not isinstance(clr, int):
                raise ValueError("The image must be single layer.")
            res[x].append(clr)
    return res


def transform_datalist_to_matrix(
    image: list[int], width: int, height: int
) -> list[list[int]]:
    """
    This function transform flatten list of pixels to a matrix of pixel

    Parameters
    ----------
    image: list[int]
        Image.get_data object
    width: int
        Width of Image
    height: int
        Height of Image
    Returns
    -------
    matrix: list[list[int]]
        Matrix of pixel brightness
    """
    res: list[list[int]] = [[] for _ in range(width)]
    for y in range(height):
        for x in range(width):
            res[x].append(image[y * width + x])
    return res


def image_from_datalist(data: list[int], width: int, height: int) -> Image.Image:
    """
    Create image from flatten list of pixels

    Parameters
    ----------
    data: list[int]
        Flatten list of pixels
    width: int
        Width of Image
    height: int
        Height of Image

    Returns
    -------
    image: Image
    """
    matrix = transform_datalist_to_matrix(data, width, height)

    img = Image.new("RGB", (width, height))

    for x, row in enumerate(matrix):
        for y, value in enumerate(row):
            if isinstance(value, int):
                img.putpixel((x, y), (value, value, value))
            elif isinstance(value, tuple):
                img.putpixel((x, y), value)
    return img
