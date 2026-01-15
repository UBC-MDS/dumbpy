"""
A module that calculates the arithmetic mean of a list of numbers

"""

from dumbpy.support_functions import *

def arithmetic_mean(values: list[float | int | bool]) -> float:
    """
    Calculate the arithmetic mean of the inputted list and return the result.

    Parameters
    ----------
    values : list[float | int | bool]
        A list of numbers.

    Returns
    -------
    float
        The arithmetic mean of the list of numbers.

    Examples
    --------
    >>> arithmetic_mean([1, 2, 3, 4])
    2.5
    """
    
    ## This will raise errors if the value type is not compatible.
    numbers: list[int | float | bool] = validate_list(values)
    

    n_elements: int = len(numbers)

    if not (n_elements > 0):
        raise ValueError(
            "The number list needs to have at least one numeric element"
        )

    addition: int | float = 0

    for x in numbers:
        addition += x
    
    return addition / n_elements
    



