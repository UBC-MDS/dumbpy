"""
Unit tests for dumbpy.support_functions.

Covered functions
-----------------
- flatten_list
- validate_list

Behavior assumptions (based on current implementation)
------------------------------------------------------
flatten_list:
- Accepts any non-string, non-bytes iterable
- Recursively flattens nested iterables
- Treats str/bytes as atomic leaf values when nested
- Raises TypeError for non-iterables and for string/bytes at top-level
- Flattens dictionaries by iterating over their keys (standard Python behavior)

validate_list:
- Flattens input via flatten_list
- Ensures every flattened element is int, float, or bool
- Returns the flattened list if valid
- Raises TypeError if any flattened element is non-numeric
- Propagates flatten_list TypeError for invalid top-level input
- Accepts dictionaries if their flattened keys are numeric (dict values are not iterated)
"""

from collections import Counter
from typing import Any

import pytest

from dumbpy.support_functions import flatten_list, validate_list


def test_flatten_list_one_layer_returns_list_with_same_elements() -> None:
    """
    Test flatten_list with a single-layer list.

    Returns
    -------
    None
    """
    values: list[int] = [1, 2, 3, 4]
    expected: list[int] = [1, 2, 3, 4]

    actual: list[Any] = flatten_list(values)

    assert actual == expected
    assert isinstance(actual, list)


def test_flatten_list_nested_lists_flattens_all_layers_order_irrelevant() -> None:
    """
    Test flatten_list with multiple nested list layers.

    Notes
    -----
    Order is not asserted; only element membership and multiplicity are checked.

    Returns
    -------
    None
    """
    values: list[Any] = [1, [2, [3, 4], 5], 6]
    expected_elements: list[int] = [1, 2, 3, 4, 5, 6]

    actual: list[Any] = flatten_list(values)

    assert isinstance(actual, list)
    assert Counter(actual) == Counter(expected_elements)


def test_flatten_list_nested_mixed_iterables_flattens_order_irrelevant() -> None:
    """
    Test flatten_list with different iterable types (tuple, set, list).

    Notes
    -----
    Sets do not preserve ordering, so comparisons use Counter.

    Returns
    -------
    None
    """
    values: list[Any] = [1, (2, 3), {4, 5}, [6, [7]]]
    expected_elements: list[int] = [1, 2, 3, 4, 5, 6, 7]

    actual: list[Any] = flatten_list(values)

    assert isinstance(actual, list)
    assert Counter(actual) == Counter(expected_elements)


def test_flatten_list_preserves_duplicates() -> None:
    """
    Test that flatten_list does not drop duplicate values.

    Returns
    -------
    None
    """
    values: list[Any] = [1, [1, (1, 2)], 2]
    expected_elements: list[int] = [1, 1, 1, 2, 2]

    actual: list[Any] = flatten_list(values)

    assert Counter(actual) == Counter(expected_elements)


def test_flatten_list_treats_nested_strings_as_atomic() -> None:
    """
    Test that nested strings are treated as atomic leaf elements.

    Returns
    -------
    None
    """
    values: list[Any] = [["ab", ["cd"]]]
    actual: list[Any] = flatten_list(values)

    assert actual == ["ab", "cd"]


@pytest.mark.parametrize("bad_input", [123, 3.14, True, "abc", b"bytes"])
def test_flatten_list_raises_typeerror_for_invalid_top_level_inputs(bad_input: Any) -> None:
    """
    Test flatten_list raises TypeError for invalid top-level inputs.

    Parameters
    ----------
    bad_input : Any
        A value that is either non-iterable or a string/bytes object.

    Returns
    -------
    None
    """
    with pytest.raises(TypeError, match="non-string, non-bytes iterable"):
        flatten_list(bad_input)

def test_flatten_list_dict_is_flattened_by_iterating_over_keys_order_irrelevant() -> None:
    """
    Test flatten_list flattens dictionaries by iterating over their keys.

    Notes
    -----
    Dict iteration yields keys. Ordering is not asserted; only membership and
    multiplicity are checked.

    Returns
    -------
    None
    """
    values: list[Any] = [{"a": 1, "b": 2}, ["c"]]
    expected_elements: list[str] = ["a", "b", "c"]

    actual: list[Any] = flatten_list(values)

    assert isinstance(actual, list)
    assert Counter(actual) == Counter(expected_elements)

def test_validate_list_all_int_list_returns_flat_list() -> None:
    """
    Test validate_list on an all-integer list.

    Returns
    -------
    None
    """
    values: list[int] = [1, 2, 3, 4]
    expected: list[int] = [1, 2, 3, 4]

    actual = validate_list(values)

    assert actual == expected
    assert isinstance(actual, list)


def test_validate_list_all_float_list_returns_flat_list() -> None:
    """
    Test validate_list on an all-float list.

    Returns
    -------
    None
    """
    values: list[float] = [1.0, 2.5, 3.25]
    expected: list[float] = [1.0, 2.5, 3.25]

    assert validate_list(values) == expected


def test_validate_list_all_bool_list_returns_flat_list() -> None:
    """
    Test validate_list on an all-bool list.

    Returns
    -------
    None
    """
    values: list[bool] = [True, False, True]
    expected: list[bool] = [True, False, True]

    assert validate_list(values) == expected


def test_validate_list_mixed_numeric_types_returns_flat_list() -> None:
    """
    Test validate_list on mixed numeric types.

    Returns
    -------
    None
    """
    values: list[Any] = [1, 2.0, True, 4, 5.5, False]
    expected: list[Any] = [1, 2.0, True, 4, 5.5, False]

    assert validate_list(values) == expected


def test_validate_list_nested_numeric_iterables_returns_flat_list() -> None:
    """
    Test validate_list flattens nested iterables and returns a flat list.

    Returns
    -------
    None
    """
    values: list[Any] = [1, (2.0, True), [3, [4]]]
    expected_elements: list[Any] = [1, 2.0, True, 3, 4]

    actual = validate_list(values)

    assert isinstance(actual, list)
    assert Counter(actual) == Counter(expected_elements)


@pytest.mark.parametrize(
    "values",
    [
        [1, "a", 3],
        [1, [2, "x"], 4],
        [None],
        [{"k": 1}],
    ],
)
def test_validate_list_raises_typeerror_for_non_numeric_values(values: Any) -> None:
    """
    Test validate_list raises TypeError when any flattened element is non-numeric.

    Parameters
    ----------
    values : Any
        A value that will flatten to include at least one non-numeric element.

    Returns
    -------
    None
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
def test_validate_list_other_iterables_are_accepted_if_numeric(values: Any, expected_elements: list[int]) -> None:
    """
    Test validate_list accepts non-list iterables if they are numeric.

    Parameters
    ----------
    values : Any
        A non-list iterable containing numeric values.
    expected_elements : list[int]
        The expected multiset of numeric elements after flattening.

    Returns
    -------
    None
    """
    actual = validate_list(values)
    assert isinstance(actual, list)
    assert Counter(actual) == Counter(expected_elements)


@pytest.mark.parametrize("bad_input", [123, 3.14, True, "abc", b"bytes"])
def test_validate_list_propagates_flatten_list_typeerror_on_invalid_input(bad_input: Any) -> None:
    """
    Test validate_list propagates TypeError from flatten_list for invalid inputs.

    Parameters
    ----------
    bad_input : Any
        A value that is invalid as a top-level input to flatten_list.

    Returns
    -------
    None
    """
    with pytest.raises(TypeError, match="non-string, non-bytes iterable"):
        validate_list(bad_input)

def test_validate_list_dict_with_numeric_keys_returns_flat_key_list() -> None:
    """
    Test validate_list accepts a dictionary with numeric keys.

    Notes
    -----
    Dictionaries are iterated by keys, so values are not validated.

    Returns
    -------
    None
    """
    values: dict[int, str] = {1: "x", 2: "y", 3: "z"}
    expected_elements: list[int] = [1, 2, 3]

    actual = validate_list(values)

    assert isinstance(actual, list)
    assert Counter(actual) == Counter(expected_elements)
