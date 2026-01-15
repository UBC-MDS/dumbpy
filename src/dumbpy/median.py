from dumbpy.support_functions import validate_list


def median(values: list[float | int | bool]) -> float:
    """
    Calculate the median of the inputted list and return the result.

    Parameters
    ----------
    values : list[float | int | bool]
        A list of numbers.

    Returns
    -------
    float
        The median value of the input list. If the list has an even number of
        elements, returns the average of the two middle values.

    Raises
    ------
    ValueError
        If the input list is empty.
    TypeError
        If the input contains non-numeric values (raised by validate_list).

    Examples
    --------
    >>> median([3, 1, 2])
    2.0
    >>> median([1, 2, 3, 4])
    2.5
    """
    numbers: list[int | float | bool] = validate_list(values)

    n_elements: int = len(numbers)
    if not (n_elements > 0):
        raise ValueError("The number list needs to have at least one numeric element")

    numbers_sorted = sorted(numbers)
    mid = n_elements // 2

    if n_elements % 2 == 1:
        return float(numbers_sorted[mid])

    return (numbers_sorted[mid - 1] + numbers_sorted[mid]) / 2

