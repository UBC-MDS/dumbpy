"""
A module that calculates the standard deviation of a list of numbers.

"""

from dumbpy.support_functions import validate_list, flatten_list
from dumbpy.arithmetic_mean import arithmetic_mean

def std_deviation(values: list[float | int]) -> float:
    """
    Calculate and return the population standard deviation of a list of numeric values.

    Parameters
    ----------
    values : list[float | int]
        A list of numbers.

    Returns
    -------
    float
        The standard deviation of the list of numbers.
    
    Raises
    ------
    ValueError
        If the input list is empty.
    
    TypeError
        If the input list contains a non-numeric datatype

    Examples
    --------
    >>> std_deviation([1, 1, 1, 1])
    0
    >>> std_deviation([1, 2, 3, 4])
    1.118033988749895
    """

    ## This will raise errors if the value type is not compatible. Copied from Hector's arithmetic_mean function
    numbers: list[int | float | bool] = validate_list(values)

    n = len(values)
    mean = arithmetic_mean(values)

    variance = sum((x - mean) ** 2 for x in values) / n
    std_dev = variance ** 0.5
    
    return std_dev

    
