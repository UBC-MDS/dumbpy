from dumbpy.std_deviation import std_deviation
import pytest

# Test list of one datatype - integers, floats, boolean separately
def test_std_dev_one_type():
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

# Test list of mixed datatypes - int, float, bool mixed together
def test_std_dev_mixed_type():
    mix_input = [1, 1.0, True]
    expected = 0
    actual = std_deviation(mix_input)
    assert actual == pytest.approx(expected)

# Test list with a single element
def test_std_dev_single():
    single_input = [1]
    expected = 0
    actual = std_deviation(single_input)
    assert actual == pytest.approx(expected)

# Test list with negative numbers
def test_std_dev_neg():
    neg_input = [-1, -1, 0, 0]
    expected = 0.5
    actual = std_deviation(neg_input)
    assert actual == pytest.approx(expected)

# Test that an empty list should raise a ValueError
def test_std_dev_empty():
    with pytest.raises(ValueError):
        mt_input = []
        std_deviation(mt_input)

# Test that non-numeric input should raise a TypeError
def test_std_dev_nonnum():
    with pytest.raises(TypeError):
        std_deviation([1, "a", 3])