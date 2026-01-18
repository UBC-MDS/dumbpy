"""
Unit tests for dumbpy.std_deviation.std_deviation.

Covered behavior
----------------
- Works on homogeneous numeric types (int, float, bool)
- Works on mixed numeric types
- Works on a single-element list
- Works with negative values
- Nested numeric iterables are flattened via validate_list
- Empty input raises ValueError
- Non-numeric input raises TypeError
"""

from typing import Any

import pytest

from dumbpy.std_deviation import std_deviation


def test_std_deviation_homogeneous_types() -> None:
    """
    Test std_deviation on int-only, float-only, and bool-only inputs.

    Returns
    -------
    None
    """
    int_input: list[int] = [1, 1, 1, 1]
    assert std_deviation(int_input) == pytest.approx(0.0)

    flt_input: list[float] = [0.1, 0.2, 0.1, 0.2]
    assert std_deviation(flt_input) == pytest.approx(0.05)

    bool_input: list[bool] = [True, True, False, False]
    assert std_deviation(bool_input) == pytest.approx(0.5)


def test_std_deviation_mixed_types() -> None:
    """
    Test std_deviation on a mixed numeric list.

    Returns
    -------
    None
    """
    mix_input: list[int | float | bool] = [1, 1.0, True]
    assert std_deviation(mix_input) == pytest.approx(0.0)


def test_std_deviation_single_element() -> None:
    """
    Test std_deviation on a single-element list.

    Returns
    -------
    None
    """
    single_input: list[int] = [1]
    assert std_deviation(single_input) == pytest.approx(0.0)


def test_std_deviation_negative_values() -> None:
    """
    Test std_deviation on a list containing negative numbers.

    Returns
    -------
    None
    """
    neg_input: list[int] = [-1, -1, 0, 0]
    assert std_deviation(neg_input) == pytest.approx(0.5)


def test_std_deviation_known_value() -> None:
    """
    Test std_deviation against a known value.

    Returns
    -------
    None
    """
    values: list[int] = [1, 2, 3, 4]
    expected: float = 1.118033988749895
    assert std_deviation(values) == pytest.approx(expected)


def test_std_deviation_nested_numeric_iterables_are_flattened() -> None:
    """
    Test that std_deviation works with nested numeric iterables.

    Returns
    -------
    None
    """
    values: list[Any] = [1, [2, 3], 4]
    expected: float = 1.118033988749895
    assert std_deviation(values) == pytest.approx(expected)


def test_std_deviation_empty_raises_valueerror() -> None:
    """
    Test that std_deviation raises ValueError on empty input.

    Returns
    -------
    None
    """
    with pytest.raises(ValueError, match="at least one numeric element"):
        std_deviation([])


def test_std_deviation_non_numeric_raises_typeerror() -> None:
    """
    Test that std_deviation raises TypeError on non-numeric input.

    Returns
    -------
    None
    """
    with pytest.raises(TypeError, match="not a numeric value"):
        std_deviation([1, "a", 3])
