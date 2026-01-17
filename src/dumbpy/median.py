"""
dumbpy.median
=============

Compute the median of numeric values.

The input may be a nested iterable; nesting is flattened via
:func:`dumbpy.support_functions.validate_list`.
"""

from collections.abc import Iterable
from typing import Any

from dumbpy.support_functions import Numeric, validate_list


def median(values: Iterable[Any]) -> Numeric | float:
    """
    Compute the median of numeric values.

    Parameters
    ----------
    values : Iterable[Any]
        A (possibly nested) iterable containing numeric values.

    Returns
    -------
    Numeric | float
        The median value of the input after sorting. For odd-length inputs, the
        middle element is returned (so the type may be ``int``, ``float``, or
        ``bool``). For even-length inputs, the average of the two middle values
        is returned, which is typically a ``float`` (but can be an ``int``/``bool``
        when the middle values are equal in this implementation).

    Raises
    ------
    ValueError
        If the flattened input contains no elements.
    TypeError
        If the input is not a valid iterable for flattening, or if any element
        is non-numeric (raised by :func:`validate_list`).

    Examples
    --------
    >>> median([3, 1, 2])
    2
    >>> median([1, 2, 3, 4])
    2.5
    """
    numbers: list[Numeric] = validate_list(values)
    n_elements: int = len(numbers)

    if n_elements == 0:
        raise ValueError("The number list needs to have at least one numeric element")

    numbers_sorted: list[Numeric] = sorted(numbers)
    mid: int = n_elements // 2

    if n_elements % 2 == 1:
        return numbers_sorted[mid]

    if numbers_sorted[mid - 1] == numbers_sorted[mid]:
        return numbers_sorted[mid - 1]

    return (numbers_sorted[mid - 1] + numbers_sorted[mid]) / 2
