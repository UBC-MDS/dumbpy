"""
A module of support functions for the dumbpy main functionality

"""

from typing import Any
from collections.abc import Iterable


def flatten_list(values: Iterable) -> list:
    """
    Flatten a nested list into a single, one-dimensional list.

    This function takes a list that may contain nested lists and
    returns a new list with all elements flattened into a single
    level, preserving their original order.

    Parameters
    ----------
    values : Iterable
        An iterable object (except strings) that may contain nested iterables of arbitrary depth.

    Returns
    -------
    list
        A flattened list containing all elements from `values`.

    Raises
    ------
    TypeError
        If `values` is not a list.

    Examples
    --------
    >>> flatten_list([1, 2, [3, 4]])
    [1, 2, 3, 4]

    >>> flatten_list([[1, 2], [3, [4, 5]]])
    [1, 2, 3, 4, 5]

    >>> flatten_list([])
    []
    """
    
    if not isinstance(values, Iterable) or isinstance(values, str):
        raise TypeError("Input should be a non-string iterable object")

    output_list: list[Any] = []

    def _flatten_layer(layer: Iterable) -> None:
        for element in layer:
            if isinstance(element, Iterable) and not isinstance(element, (str, bytes)):
                _flatten_layer(element)
            else:
                output_list.append(element)
        return None
    
    _flatten_layer(values)

    return output_list



def validate_list(values: list) -> list[int | float | bool]:
    """
    Validate that the input is a list of numeric values.

    This function checks whether the provided input is a list
    containing only numeric types (integers or floats). If the input
    contains non-numeric values, a TypeError is raised.

    Parameters
    ----------
    values : list
        A list input provided by the user.

    Returns
    -------
    list[int | float | bool]
        A flattened list containing all elements from `values`, if
        values are all numeric.

        
    Raises
    ------
    TypeError
        If any element in `values` is not a numeric type.

    Examples
    --------
    >>> validate_types([1, 2, 3.5])
    >>> validate_types([1, True, 6])
    >>> validate_types([1, "a", 3])
    Traceback (most recent call last):
        ...
    TypeError: All elements must be numeric.
    """
    flat_values: list[Any] = flatten_list(values)

    for value in flat_values:

        if not isinstance(value, (float, int, bool)):
            raise TypeError(f"{value} is not a numeric value.")

    return flat_values


