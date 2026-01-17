"""
Unit tests for median.median.

Test cases covered
------------------
- Odd number of data points
- Even number of data points
- Empty input raises ValueError
"""

from dumbpy.median import median
import pytest


def test_median_odd_length():
    """
    median should return the middle value (after sorting) for an odd-length list.
    """
    values = [3, 1, 2]
    expected = 2.0
    actual = median(values)
    assert actual == expected


def test_median_even_length():
    """
    median should return the average of the two middle values for an even-length list.
    """
    values = [4, 1, 3, 2]
    expected = 2.5
    actual = median(values)
    assert actual == expected


def test_median_empty_raises_valueerror():
    """
    median should raise ValueError when the input list is empty.
    """
    with pytest.raises(ValueError, match="at least one numeric element"):
        median([])
