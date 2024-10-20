import pytest
from project.transform import transform_datalist_to_matrix


@pytest.mark.parametrize(
    "flatten_list, width, height, expected_matrix",
    [
        ([1, 2, 3, 4, 5, 6, 7, 8], 4, 2, [[1, 5], [2, 6], [3, 7], [4, 8]]),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 3, [[1, 4, 7], [2, 5, 8], [3, 6, 9]]),
        ([1, 2, 3, 4], 1, 4, [[1, 2, 3, 4]]),
    ],
)
def test_datalist_to_matrix(flatten_list, width, height, expected_matrix):
    assert transform_datalist_to_matrix(flatten_list, width, height) == expected_matrix
