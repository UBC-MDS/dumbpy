"""
Unit tests for arithmetic_mean.arithmetic_mean.

Test cases covered
------------------
Required:
- All int values
- All float values
- All bool values
- Mixed numeric types (int, float, bool)
- Empty input raises ValueError

Bonus:
- Nested numeric iterables are flattened via validate_list
- Non-numeric values raise TypeError (from validate_list)
"""

import pytest

from dumbpy.arithmetic_mean import arithmetic_mean


def test_arithmetic_mean_all_ints():
    """
    arithmetic_mean should compute the mean of an int-only list.
    """
    values = [1, 2, 3, 4]
    expected = 2.5

    actual = arithmetic_mean(values)

    assert actual == expected


def test_arithmetic_mean_all_floats():
    """
    arithmetic_mean should compute the mean of a float-only list.
    """
    values = [1.0, 2.0, 3.5]
    expected = (1.0 + 2.0 + 3.5) / 3

    actual = arithmetic_mean(values)

    assert actual == expected


def test_arithmetic_mean_all_bools():
    """
    arithmetic_mean should compute the mean of a bool-only list.

    Notes
    -----
    In Python, bool is a subclass of int:
    True == 1 and False == 0.
    """
    values = [True, False, True, True]  # sum=3, n=4 => 0.75
    expected = 0.75

    actual = arithmetic_mean(values)

    assert actual == expected


def test_arithmetic_mean_mixed_numeric_including_bool():
    """
    arithmetic_mean should compute the mean of a mixed numeric list (int/float/bool).
    """
    values = [1, 2.5, True, False]  # 1 + 2.5 + 1 + 0 = 4.5, /4 = 1.125
    expected = 1.125

    actual = arithmetic_mean(values)

    assert actual == expected


def test_arithmetic_mean_empty_list_raises_valueerror():
    """
    arithmetic_mean should raise ValueError for an empty list.
    """
    with pytest.raises(ValueError, match="at least one numeric element"):
        arithmetic_mean([])


def test_arithmetic_mean_nested_numeric_iterables_are_flattened():
    """
    Bonus: arithmetic_mean should work with nested numeric iterables because validate_list
    flattens them before calculation.
    """
    values = [1, [2, 3]]  # flattened -> [1, 2, 3], mean = 2.0
    expected = 2.0

    actual = arithmetic_mean(values)

    assert actual == expected


@pytest.mark.parametrize(
    "values",
    [
        [1, "x", 3],
        [1, [2, "nope"], 3],
        [{"a": 1}],  # dict is iterable -> keys are strings -> non-numeric
    ],
)
def test_arithmetic_mean_non_numeric_raises_typeerror(values):
    """
    Bonus: arithmetic_mean should raise TypeError when validate_list finds a non-numeric value.
    """
    with pytest.raises(TypeError, match="not a numeric value"):
        arithmetic_mean(values)
