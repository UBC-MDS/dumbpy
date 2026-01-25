"""
Unit tests for dumbpy.arithmetic_mean.arithmetic_mean.

Covered behavior
----------------
- Works on homogeneous numeric types (int, float, bool)
- Works on mixed numeric types (int/float/bool)
- Flattens nested iterables via validate_list
- Accepts general iterables (e.g., tuples, generators)
- Raises ValueError on empty input
- Raises TypeError when non-numeric values appear after flattening
- Raises TypeError on top-level string/bytes inputs (propagated from flatten_list)
"""


from typing import Any, Iterable

import pytest

from dumbpy.arithmetic_mean import arithmetic_mean


def test_arithmetic_mean_all_ints() -> None:
    """
    Test arithmetic_mean on an int-only list.

    Returns
    -------
    None
    """
    values: list[int] = [1, 2, 3, 4]
    expected: float = 2.5

    assert arithmetic_mean(values) == pytest.approx(expected)


def test_arithmetic_mean_all_floats() -> None:
    """
    Test arithmetic_mean on a float-only list.

    Returns
    -------
    None
    """
    values: list[float] = [1.0, 2.0, 3.5]
    expected: float = (1.0 + 2.0 + 3.5) / 3

    assert arithmetic_mean(values) == pytest.approx(expected)


def test_arithmetic_mean_all_bools() -> None:
    """
    Test arithmetic_mean on a bool-only list.

    Notes
    -----
    In Python, ``bool`` is a subclass of ``int``:
    ``True == 1`` and ``False == 0``.

    Returns
    -------
    None
    """
    values: list[bool] = [True, False, True, True]
    expected: float = 0.75

    assert arithmetic_mean(values) == pytest.approx(expected)


def test_arithmetic_mean_mixed_numeric_including_bool() -> None:
    """
    Test arithmetic_mean on a mixed numeric list (int/float/bool).

    Returns
    -------
    None
    """
    values: list[int | float | bool] = [1, 2.5, True, False]
    expected: float = 1.125

    assert arithmetic_mean(values) == pytest.approx(expected)


def test_arithmetic_mean_empty_raises_valueerror() -> None:
    """
    Test that arithmetic_mean raises ValueError on empty input.

    Returns
    -------
    None
    """
    with pytest.raises(ValueError, match="at least one numeric element"):
        arithmetic_mean([])


def test_arithmetic_mean_nested_numeric_iterables_are_flattened() -> None:
    """
    Test that arithmetic_mean works with nested numeric iterables.

    Returns
    -------
    None
    """
    values: list[int | list[int]] = [1, [2, 3]]
    expected: float = 2.0

    assert arithmetic_mean(values) == pytest.approx(expected)


def test_arithmetic_mean_accepts_tuple_input() -> None:
    """
    Test that arithmetic_mean accepts a tuple as input.

    Returns
    -------
    None
    """
    values: tuple[int, int, int] = (2, 4, 6)
    expected: float = 4.0

    assert arithmetic_mean(values) == pytest.approx(expected)


def test_arithmetic_mean_accepts_generator_input() -> None:
    """
    Test that arithmetic_mean accepts a generator as input.

    Returns
    -------
    None
    """
    values: Iterable[int] = (x for x in [1, 2, 3, 4])
    expected: float = 2.5

    assert arithmetic_mean(values) == pytest.approx(expected)


@pytest.mark.parametrize(
    "values",
    [
        [1, "x", 3],
        [1, [2, "nope"], 3],
        [{"a": 1}],
    ],
)
def test_arithmetic_mean_non_numeric_raises_typeerror(values: Any) -> None:
    """
    Test that arithmetic_mean raises TypeError for non-numeric values.

    Parameters
    ----------
    values : Any
        A value that will flatten to include at least one non-numeric element.

    Returns
    -------
    None
    """
    with pytest.raises(TypeError, match="not a numeric value"):
        arithmetic_mean(values)

def test_arithmetic_mean_top_level_string_raises_typeerror() -> None:
    """
    Test that arithmetic_mean raises TypeError on top-level string input.

    Returns
    -------
    None
    """
    with pytest.raises(TypeError, match="non-string, non-bytes iterable"):
        arithmetic_mean("1234")
