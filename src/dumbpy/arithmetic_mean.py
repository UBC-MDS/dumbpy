"""
dumbpy.arithmetic_mean
======================

Compute the arithmetic mean of numeric values.

The input may be a nested iterable; nesting is flattened via
:func:`dumbpy.support_functions.validate_list`.
"""

from collections.abc import Iterable
from typing import Any

from dumbpy.support_functions import Numeric, validate_list


def arithmetic_mean(values: Iterable[Any]) -> float:
    """
    Compute the arithmetic mean of numeric values.

    Parameters
    ----------
    values : Iterable[Any]
        A (possibly nested) iterable containing numeric values.

    Returns
    -------
    float
        The arithmetic mean of the numeric values.

    Raises
    ------
    ValueError
        If the flattened input contains no elements.
    TypeError
        If the input is not a valid iterable for flattening, or if any element
        is non-numeric (raised by :func:`validate_list`).

    Examples
    --------
    >>> arithmetic_mean([1, 2, 3, 4])
    2.5
    >>> arithmetic_mean([1, [2, 3]])
    2.0
    """
    numbers: list[Numeric] = validate_list(values)
    n_elements: int = len(numbers)

    if n_elements == 0:
        raise ValueError("The number list needs to have at least one numeric element")

    total: float | int = 0
    for x in numbers:
        total += x

    return total / n_elements
