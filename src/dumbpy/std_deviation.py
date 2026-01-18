"""
dumbpy.std_deviation
====================

Compute the population standard deviation of numeric values.

The input may be a nested iterable; nesting is flattened via
:func:`dumbpy.support_functions.validate_list`.
"""

from collections.abc import Iterable
from typing import Any

from dumbpy.arithmetic_mean import arithmetic_mean
from dumbpy.support_functions import Numeric, validate_list


def std_deviation(values: Iterable[Any]) -> float:
    """
    Compute the population standard deviation of numeric values.

    This uses the population variance definition:

    ``variance = sum((x - mean)**2) / n``

    Parameters
    ----------
    values : Iterable[Any]
        A (possibly nested) iterable containing numeric values.

    Returns
    -------
    float
        The population standard deviation of the numeric values.

    Raises
    ------
    ValueError
        If the flattened input contains no elements.
    TypeError
        If the input is not a valid iterable for flattening, or if any element
        is non-numeric (raised by :func:`validate_list`).

    Examples
    --------
    >>> std_deviation([1, 1, 1, 1])
    0.0
    >>> std_deviation([1, 2, 3, 4])
    1.118033988749895
    """
    numbers: list[Numeric] = validate_list(values)

    if len(numbers) == 0:
        raise ValueError("The number list needs to have at least one numeric element")

    n: int = len(numbers)
    mean: float = arithmetic_mean(numbers)

    variance: float = sum((x - mean) ** 2 for x in numbers) / n
    return variance**0.5
