from dumbpy.median import median
import pytest

def test_median():
    # Odd number of data points
    values = [3, 1, 2]
    expected = 2
    actual = median(values)
    assert actual == expected

    # Even number of data points
    values = [4, 1, 3, 2]
    expected = 2.5
    actual = median(values)
    assert actual == expected

    # Empty array
    with pytest.raises(ValueError, match="at least one numeric element"):
        median([])
