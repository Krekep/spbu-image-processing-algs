def get_brightness_histogram(
    brightness_values: list[int], brightness_levels: int = 256
) -> list[tuple[int, int]]:
    """
    This functions build brightness histogram from flatten list of gray pixels

    Parameters
    ----------
    brightness_values: list[int]
        List of brightness for each pixel
    brightness_levels: int

    Returns
    -------
    histogram: list[tuple[int, int]]
        List of pairs (brightness_level, pixels_number)
    """
    histogram = dict((i, 0) for i in range(brightness_levels))
    for value in brightness_values:
        histogram[value] += 1

    return sorted(histogram.items())
