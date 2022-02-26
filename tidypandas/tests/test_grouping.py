# flake8: noqa
import pandas as pd
import pytest

from tidypandas import add_count
from tidypandas.grouping import GroupsNotFoundError


@pytest.fixture
def example_df() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "x_1": ["a", "b", "a", "a", "c", "b", "a", "a", "b", "a"],
            "x_2": [True, False, False, True, True, True, False, False, True, True],
        }
    )


def test_add_count_single(example_df: pd.DataFrame) -> None:
    df_expected = pd.DataFrame(
        {
            "x_1": ["a", "b", "a", "a", "c", "b", "a", "a", "b", "a"],
            "x_2": [True, False, False, True, True, True, False, False, True, True],
            "count_x_1": [6, 3, 6, 6, 1, 3, 6, 6, 3, 6],
        }
    )
    pd.testing.assert_frame_equal(add_count(example_df, ["x_1"]), df_expected)


def test_add_count_multiple(example_df: pd.DataFrame) -> None:
    df_expected = pd.DataFrame(
        {
            "x_1": ["a", "b", "a", "a", "c", "b", "a", "a", "b", "a"],
            "x_2": [True, False, False, True, True, True, False, False, True, True],
            "count_x_1_X_x_2": [3, 1, 3, 3, 1, 2, 3, 3, 2, 3],
        }
    )
    pd.testing.assert_frame_equal(add_count(example_df, ["x_1", "x_2"]), df_expected)


def test_add_count_missing_single_col(example_df: pd.DataFrame) -> None:
    with pytest.raises(GroupsNotFoundError) as excinfo:
        add_count(example_df, ["some_missing_col"])
    assert "Column some_missing_col is not included in the DataFrame." in str(excinfo.value)
