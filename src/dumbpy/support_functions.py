"""
A module of support functions for the dumbpy main functionality

"""

from typing import Any

def validate_types(values: Any):
    """
    Validate that the input is an iterable of numeric values.

    This function checks whether the provided input is an iterable
    containing only numeric types (integers or floats). If the input
    is not iterable or contains non-numeric values, a TypeError is raised.

    Parameters
    ----------
    values : Any
        Any input provided by the user.

    Raises
    ------
    TypeError
        If `values` is not iterable or if any element in `values`
        is not a numeric type.

    Examples
    --------
    >>> validate_types([1, 2, 3.5])
    >>> validate_types((1, 2, 3))
    >>> validate_types([1, "a", 3])
    Traceback (most recent call last):
        ...
    TypeError: All elements must be numeric.
    """
    pass

def flatten_list(values: list):
    """
    Flatten a nested list into a single, one-dimensional list.

    This function takes a list that may contain nested lists and
    returns a new list with all elements flattened into a single
    level, preserving their original order.

    Parameters
    ----------
    values : list
        A list that may contain nested lists of arbitrary depth.

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
    pass

