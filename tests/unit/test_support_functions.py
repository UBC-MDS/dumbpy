"""
Unit tests for dumpy.support_functions.

These tests cover the public behavior of:

- flatten_list
- validate_types

The expected behavior is based on the current implementation:
- flatten_list accepts any non-string iterable (lists, tuples, sets, etc.)
  and recursively flattens nested iterables (excluding str/bytes as "leaf" types).
- validate_types flattens the input via flatten_list and then ensures all values
  are numeric (int, float, bool). It raises TypeError otherwise.

Notes
-----
- When sets are involved, order is inherently unstable, so tests compare element
  *multisets* (via collections.Counter) rather than exact ordering.
"""

from collections import Counter
import pytest

from dumbpy.support_functions import flatten_list, validate_types


def test_flatten_list_one_layer_returns_list_with_same_elements():
    """
    Test flatten_list with a single-layer iterable.

    Parameters
    ----------
    None

    Returns
    -------
    None

    Raises
    ------
    AssertionError
        If the function does not return an equivalent list.
    """
    values = [1, 2, 3, 4]
    expected = [1, 2, 3, 4]
    actual = flatten_list(values)
    assert actual == expected
    assert isinstance(actual, list)


def test_flatten_list_nested_lists_flattens_all_layers_order_irrelevant():
    """
    Test flatten_list with multiple nested list layers.

    Order is not asserted; only element membership and multiplicity are checked.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    values = [1, [2, [3, 4], 5], 6]
    expected_elements = [1, 2, 3, 4, 5, 6]

    actual = flatten_list(values)

    assert isinstance(actual, list)
    assert Counter(actual) == Counter(expected_elements)


def test_flatten_list_nested_mixed_iterables_flattens_to_single_list_order_irrelevant():
    """
    Test flatten_list with mixtures of different iterables (tuple, set, list).

    Parameters
    ----------
    None

    Returns
    -------
    None

    Notes
    -----
    Sets do not preserve ordering, so we compare Counters.
    """
    values = [1, (2, 3), {4, 5}, [6, [7]]]
    expected_elements = [1, 2, 3, 4, 5, 6, 7]

    actual = flatten_list(values)

    assert isinstance(actual, list)
    assert Counter(actual) == Counter(expected_elements)


def test_flatten_list_preserves_duplicates():
    """
    Test that flatten_list does not drop or merge duplicate values.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    values = [1, [1, (1, 2)], 2]
    expected_elements = [1, 1, 1, 2, 2]

    actual = flatten_list(values)

    assert Counter(actual) == Counter(expected_elements)


@pytest.mark.parametrize(
    "bad_input",
    [
        123,                # non-iterable
        3.14,               # non-iterable
        True,               # non-iterable (bool is not Iterable)
        "abc",              # string is explicitly disallowed
    ],
)
def test_flatten_list_raises_typeerror_for_invalid_inputs(bad_input):
    """
    Test flatten_list raises TypeError for invalid inputs.

    Parameters
    ----------
    bad_input : Any
        A value that should be rejected by flatten_list.

    Returns
    -------
    None

    Raises
    ------
    TypeError
        Expected for non-iterables and strings.
    """
    with pytest.raises(TypeError, match="non-string iterable"):
        flatten_list(bad_input)


def test_validate_types_all_int_list_passes():
    """
    Test validate_types passes for an all-integer list.

    Returns
    -------
    None
    """
    validate_types([1, 2, 3, 4])


def test_validate_types_all_float_list_passes():
    """
    Test validate_types passes for an all-float list.

    Returns
    -------
    None
    """
    validate_types([1.0, 2.5, 3.25])


def test_validate_types_all_bool_list_passes():
    """
    Test validate_types passes for an all-bool list.

    Returns
    -------
    None
    """
    validate_types([True, False, True])


def test_validate_types_mixed_numeric_types_passes():
    """
    Test validate_types passes for a mix of int, float, and bool.

    Returns
    -------
    None
    """
    validate_types([1, 2.0, True, 4, 5.5, False])


def test_validate_types_nested_numeric_iterables_passes():
    """
    Test validate_types passes when numeric values are nested across iterables.

    Returns
    -------
    None
    """
    validate_types([1, (2.0, True), [3, [4]]])


@pytest.mark.parametrize(
    "values",
    [
        [1, "a", 3],
        [1, [2, "x"], 4],
        [None],
        [{"k": 1}],          # dict is iterable -> keys ("k") are non-numeric
    ],
)
def test_validate_types_raises_typeerror_for_non_numeric_values(values):
    """
    Test validate_types raises TypeError if any flattened element is non-numeric.

    Parameters
    ----------
    values : Any
        An iterable containing at least one non-numeric value.

    Returns
    -------
    None
    """
    with pytest.raises(TypeError, match="not a numeric value"):
        validate_types(values)


@pytest.mark.parametrize(
    "values",
    [
        (1, 2, 3),           # tuple input (allowed by current implementation)
        {1, 2, 3},           # set input (allowed by current implementation)
        [1, (2, 3), [4]],    # mixed nesting
    ],
)
def test_validate_types_other_iterables_are_accepted_if_numeric(values):
    """
    Test validate_types accepts other iterables (tuple, set, etc.) if numeric.

    Notes
    -----
    Although validate_types is annotated as taking a list, it relies on
    flatten_list which accepts any non-string iterable.
    """
    validate_types(values)


@pytest.mark.parametrize("bad_input", [123, 3.14, True, "abc"])
def test_validate_types_propagates_flatten_list_typeerror_on_invalid_input(bad_input):
    """
    Test validate_types propagates TypeError from flatten_list for invalid inputs.

    Parameters
    ----------
    bad_input : Any
        A value that is not a non-string iterable.

    Returns
    -------
    None
    """
    with pytest.raises(TypeError, match="non-string iterable"):
        validate_types(bad_input)
