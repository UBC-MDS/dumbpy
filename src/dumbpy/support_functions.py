"""
dumbpy.support_functions
========================

Support utilities for the dumbpy package.

This module provides:

- ``flatten_list``: recursively flattens nested (non-string/bytes) iterables
  into a one-dimensional Python list.
- ``validate_list``: flattens the input and ensures all resulting elements are
  numeric (``int``, ``float``, or ``bool``).

Notes
-----
- Strings and bytes are treated as atomic leaf values when nested, but are
  rejected as the *top-level* input to ``flatten_list`` (and therefore to
  ``validate_list``).
- Dictionaries are iterables in Python; flattening a dict will iterate over its
  keys (standard Python behavior).
"""

from collections.abc import Iterable
from typing import Any

Numeric = int | float | bool


def flatten_list(values: Iterable[Any]) -> list[Any]:
    """
    Flatten a nested iterable into a single, one-dimensional list.

    This function takes an iterable that may contain nested iterables and
    returns a new list with all elements flattened into a single level.

    Parameters
    ----------
    values : Iterable[Any]
        An iterable object (except strings and bytes) that may contain nested
        iterables of arbitrary depth.

    Returns
    -------
    list[Any]
        A flattened list containing all elements from `values`.

    Raises
    ------
    TypeError
        If `values` is not an iterable or if it is a string/bytes object.

    Examples
    --------
    >>> flatten_list([1, 2, [3, 4]])
    [1, 2, 3, 4]
    >>> flatten_list([[1, 2], [3, [4, 5]]])
    [1, 2, 3, 4, 5]
    >>> flatten_list([])
    []
    """
    if not isinstance(values, Iterable) or isinstance(values, (str, bytes)):
        raise TypeError("Input should be a non-string, non-bytes iterable object")

    output_list: list[Any] = []

    def _flatten_layer(layer: Iterable[Any]) -> None:
        for element in layer:
            if isinstance(element, Iterable) and not isinstance(element, (str, bytes)):
                _flatten_layer(element)
            else:
                output_list.append(element)

    _flatten_layer(values)
    return output_list


def validate_list(values: Iterable[Any]) -> list[Numeric]:
    """
    Validate that the input is a nested iterable of numeric values.

    The input is flattened using :func:`dumbpy.support_functions.flatten_list`,
    then each flattened element is checked to be an ``int``, ``float``, or
    ``bool``. If all elements are numeric, the flattened list is returned.

    Parameters
    ----------
    values : Iterable[Any]
        Any nested iterable that may contain numeric values.

    Returns
    -------
    list[Numeric]
        A flattened list containing all elements from `values`, if all values
        are numeric.

    Raises
    ------
    TypeError
        If `values` is not a valid top-level input for :func:`flatten_list`, or
        if any flattened element is not numeric.

    Examples
    --------
    >>> validate_list([1, 2, 3.5])
    [1, 2, 3.5]
    >>> validate_list([1, True, 6])
    [1, True, 6]
    >>> validate_list([1, "a", 3])
    Traceback (most recent call last):
        ...
    TypeError: a is not a numeric value.
    """
    flat_values: list[Any] = flatten_list(values)

    numeric_values: list[Numeric] = []
    for value in flat_values:
        if not isinstance(value, (int, float, bool)):
            raise TypeError(f"{value} is not a numeric value.")
        numeric_values.append(value)

    return numeric_values
