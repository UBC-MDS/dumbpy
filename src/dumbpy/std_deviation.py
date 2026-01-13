"""
A module that calculates the standard deviation of a list of numbers.

"""

from dumbpy.support_functions import validate_types, flatten_list
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

    #I will remove these 2 lines once the mean function has exception handling for this.
    if not values:
        raise ValueError("List must contain at least 1 element.")

    n = len(values)
    mean = sum(values)/n
    #mean = arithmetic_mean(values)
    #I will remove the above mean calculation and uncomment the arithmetic_mean line once Hector's part is ready.

    variance = sum((x - mean) ** 2 for x in values) / n
    std_dev = variance ** 0.5
    
    return std_dev

    
