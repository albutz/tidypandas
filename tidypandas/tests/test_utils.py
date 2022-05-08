# flake8: noqa
from typing import List

import pytest

from tidypandas.utils import filter_list


@pytest.fixture
def example_list() -> List:
    return ["hello", "darkness", "my", "old", "friend"]


@pytest.fixture
def example_mask() -> List:
    return [True, False, True, False, True]


def test_filter_list_length_mismatch(example_list: List) -> None:
    short_mask = [True, False, True]
    with pytest.raises(ValueError) as excinfo:
        filter_list(example_list, short_mask)
    assert "The length of the mask does not match." == str(excinfo.value)


def test_filter_list_non_boolean_mask(example_list: List) -> None:
    nonboolean_mask = [True, False, "nonsense", True, True]
    with pytest.raises(TypeError) as excinfo:
        filter_list(example_list, nonboolean_mask)
    assert "The mask to be used for filtering can only include boolean values." == str(
        excinfo.value
    )


def test_filter_list_default(example_list: List, example_mask: List) -> None:
    assert filter_list(example_list, example_mask) == ["hello", "my", "friend"]


def test_filter_list_negate(example_list: List, example_mask: List) -> None:
    assert filter_list(example_list, example_mask, negate=True) == ["darkness", "old"]
