"""
Unit tests for dumbpy.support_functions.

Covered functions
-----------------
- flatten_list
- validate_list

Behavior assumptions (based on current implementation)
------------------------------------------------------
flatten_list:
- Accepts any non-string iterable (lists, tuples, sets, dicts, etc.)
- Recursively flattens nested iterables
- Treats str/bytes as atomic leaf values when nested, but rejects string input at top-level
- Raises TypeError for non-iterables and for string inputs

validate_list:
- Flattens input via flatten_list
- Ensures every flattened element is int, float, or bool
- Returns the flattened list if valid
- Raises TypeError if any flattened element is non-numeric
- Propagates flatten_list TypeError for invalid top-level input
"""

from collections import Counter
import pytest

from dumbpy.support_functions import flatten_list, validate_list


# -----------------------
# flatten_list tests
# -----------------------

def test_flatten_list_one_layer_returns_list_with_same_elements():
    """
    Test flatten_list with a single-layer list.

    Returns
    -------
    None
    """
    values = [1, 2, 3, 4]
    expected = [1, 2, 3, 4]

    actual = flatten_list(values)

    assert actual == expected
    assert isinstance(actual, list)


def test_flatten_list_nested_lists_flattens_all_layers_order_irrelevant():
    """
    Test flatten_list with multiple nested list layers.

    Notes
    -----
    Order is not asserted; only element membership and multiplicity are checked.
    """
    values = [1, [2, [3, 4], 5], 6]
    expected_elements = [1, 2, 3, 4, 5, 6]

    actual = flatten_list(values)

    assert isinstance(actual, list)
    assert Counter(actual) == Counter(expected_elements)


def test_flatten_list_nested_mixed_iterables_flattens_to_single_list_order_irrelevant():
    """
    Test flatten_list with mixtures of different iterables (tuple, set, list).

    Notes
    -----
    Sets do not preserve ordering, so comparisons use Counter.
    """
    values = [1, (2, 3), {4, 5}, [6, [7]]]
    expected_elements = [1, 2, 3, 4, 5, 6, 7]

    actual = flatten_list(values)

    assert isinstance(actual, list)
    assert Counter(actual) == Counter(expected_elements)


def test_flatten_list_preserves_duplicates():
    """
    Test that flatten_list does not drop duplicate values.
    """
    values = [1, [1, (1, 2)], 2]
    expected_elements = [1, 1, 1, 2, 2]

    actual = flatten_list(values)

    assert Counter(actual) == Counter(expected_elements)


@pytest.mark.parametrize("bad_input", [123, 3.14, True, "abc"])
def test_flatten_list_raises_typeerror_for_invalid_inputs(bad_input):
    """
    Test flatten_list raises TypeError for non-iterables and strings.
    """
    with pytest.raises(TypeError, match="non-string iterable"):
        flatten_list(bad_input)


# -----------------------
# validate_list tests
# -----------------------

def test_validate_list_all_int_list_returns_flat_list():
    """
    validate_list should return the flattened list for all-integer inputs.
    """
    values = [1, 2, 3, 4]
    expected = [1, 2, 3, 4]

    actual = validate_list(values)

    assert actual == expected
    assert isinstance(actual, list)


def test_validate_list_all_float_list_returns_flat_list():
    """
    validate_list should return the flattened list for all-float inputs.
    """
    values = [1.0, 2.5, 3.25]
    expected = [1.0, 2.5, 3.25]

    actual = validate_list(values)

    assert actual == expected


def test_validate_list_all_bool_list_returns_flat_list():
    """
    validate_list should return the flattened list for all-bool inputs.
    """
    values = [True, False, True]
    expected = [True, False, True]

    actual = validate_list(values)

    assert actual == expected


def test_validate_list_mixed_numeric_types_returns_flat_list():
    """
    validate_list should return the flattened list for mixed numeric types.
    """
    values = [1, 2.0, True, 4, 5.5, False]
    expected = [1, 2.0, True, 4, 5.5, False]

    actual = validate_list(values)

    assert actual == expected


def test_validate_list_nested_numeric_iterables_returns_flat_list():
    """
    validate_list should flatten nested iterables and return the flat list.
    """
    values = [1, (2.0, True), [3, [4]]]
    expected_elements = [1, 2.0, True, 3, 4]

    actual = validate_list(values)

    assert isinstance(actual, list)
    # tuple/list nesting preserves order here, but we keep order-agnostic to match your earlier requirement
    assert Counter(actual) == Counter(expected_elements)


@pytest.mark.parametrize(
    "values",
    [
        [1, "a", 3],
        [1, [2, "x"], 4],
        [None],
        [{"k": 1}],     # dict is iterable -> keys ("k") are non-numeric
    ],
)
def test_validate_list_raises_typeerror_for_non_numeric_values(values):
    """
    validate_list should raise TypeError when any flattened element is non-numeric.
    """
    with pytest.raises(TypeError, match="not a numeric value"):
        validate_list(values)


@pytest.mark.parametrize(
    ("values", "expected_elements"),
    [
        ((1, 2, 3), [1, 2, 3]),
        ({1, 2, 3}, [1, 2, 3]),
        ([1, (2, 3), [4]], [1, 2, 3, 4]),
    ],
)
def test_validate_list_other_iterables_are_accepted_if_numeric(values, expected_elements):
    actual = validate_list(values)
    assert isinstance(actual, list)
    assert Counter(actual) == Counter(expected_elements)


@pytest.mark.parametrize("bad_input", [123, 3.14, True, "abc"])
def test_validate_list_propagates_flatten_list_typeerror_on_invalid_input(bad_input):
    """
    validate_list should propagate TypeError from flatten_list for invalid top-level inputs.
    """
    with pytest.raises(TypeError, match="non-string iterable"):
        validate_list(bad_input)


