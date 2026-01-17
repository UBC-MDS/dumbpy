"""
Unit tests for dumbpy.median.median.

Covered behavior
----------------
- Odd number of data points
- Even number of data points
- Even-length branch where the middle two values are equal
- Nested numeric iterables are flattened via validate_list
- Empty input raises ValueError
- Non-numeric input raises TypeError
"""

from typing import Any

import pytest

from dumbpy.median import median


def test_median_odd_length() -> None:
    """
    Test median on an odd-length list.

    Returns
    -------
    None
    """
    values: list[int] = [3, 1, 2]
    expected: int = 2

    assert median(values) == expected


def test_median_even_length() -> None:
    """
    Test median on an even-length list.

    Returns
    -------
    None
    """
    values: list[int] = [4, 1, 3, 2]
    expected: float = 2.5

    assert median(values) == pytest.approx(expected)


def test_median_even_length_equal_middle_values_returns_middle_value() -> None:
    """
    Test the even-length branch where the two middle values are identical.

    Returns
    -------
    None
    """
    values: list[int] = [1, 2, 2, 100]
    expected: int = 2

    assert median(values) == expected


def test_median_nested_numeric_iterables_are_flattened() -> None:
    """
    Test that median works with nested numeric iterables.

    Returns
    -------
    None
    """
    values: list[Any] = [10, [2, 3], 4]
    expected: float = (3 + 4) / 2

    assert median(values) == pytest.approx(expected)


def test_median_empty_raises_valueerror() -> None:
    """
    Test that median raises ValueError on empty input.

    Returns
    -------
    None
    """
    with pytest.raises(ValueError, match="at least one numeric element"):
        median([])


@pytest.mark.parametrize("values", [[1, "a", 3], [1, [2, "x"], 4], [{"k": 1}]])
def test_median_non_numeric_raises_typeerror(values: Any) -> None:
    """
    Test that median raises TypeError when non-numeric values are present.

    Parameters
    ----------
    values : Any
        A value that will flatten to include at least one non-numeric element.

    Returns
    -------
    None
    """
    with pytest.raises(TypeError, match="not a numeric value"):
        median(values)
