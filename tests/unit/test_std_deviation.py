"""
Unit tests for std_deviation.std_deviation.

Test cases covered 
------------------
- All int values
- All float values
- All bool values
- Mixed numeric types (int, float, bool)
- Single numeric element list
- List containing negative numbers
- Empty input raises ValueError
- Non-numeric input raises TypeError

"""

from dumbpy.std_deviation import std_deviation
import pytest

def test_std_dev_one_type():
    """
    std_deviation should compute the standard deviation of an int-only list, a float-only list, and a bool-only list. 
    """
    int_input = [1, 1, 1, 1]
    expected = 0
    actual = std_deviation(int_input)
    assert actual == pytest.approx(expected)

    flt_input = [0.1, 0.2, 0.1, 0.2]
    expected = 0.05
    actual = std_deviation(flt_input)
    assert actual == pytest.approx(expected)

    bool_input = [True, True, False, False]
    expected = 0.5
    actual = std_deviation(bool_input)
    assert actual == pytest.approx(expected)

def test_std_dev_mixed_type():
    """
    std_deviation should compute the standard deviation of a mixed numeric type list. 
    """
    mix_input = [1, 1.0, True]
    expected = 0
    actual = std_deviation(mix_input)
    assert actual == pytest.approx(expected)

def test_std_dev_single():
    """
    std_deviation should compute the standard deviation of an single element list. 
    """
    single_input = [1]
    expected = 0
    actual = std_deviation(single_input)
    assert actual == pytest.approx(expected)

def test_std_dev_neg():
    """
    std_deviation should compute the standard deviation of a list containing negative numbers.
    """
    neg_input = [-1, -1, 0, 0]
    expected = 0.5
    actual = std_deviation(neg_input)
    assert actual == pytest.approx(expected)

def test_std_dev_empty():
    """
    std_deviation should raise a Value Error for an empty list.
    """
    with pytest.raises(ValueError):
        mt_input = []
        std_deviation(mt_input)

def test_std_dev_nonnum():
    """
    std_deviation should raise a Type Error for an list with non-numeric elements.
    """
    with pytest.raises(TypeError):
        std_deviation([1, "a", 3])