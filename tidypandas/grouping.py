"""Helper functions for grouping operations."""

from typing import List

import pandas as pd


class GroupsNotFoundError(Exception):
    """A custom exception that is raised if the groups provided to add_count are not found."""


def add_count(df: pd.DataFrame, group_cols: List, count_name: str = None) -> pd.DataFrame:
    """Add group counts.

    Args:
        df: A pandas DataFrame.
        group_cols: A list of columns to group by.
        count_name: The name of the new column with group counts.

    Raises:
        GroupsNotFoundError: If some columns in group_cols are not present in df.

    Returns:
        A pandas DataFrame with group counts.
    """
    # Copy the input DataFrame
    tbl = df.copy()

    # Check if all groups are included and raise a GroupsNotFoundError if not
    is_group_included = [group in tbl.columns for group in group_cols]
    if not all(is_group_included):
        # Get column names that are not included
        missing_cols = [
            group for (group, is_included) in zip(group_cols, is_group_included) if not is_included
        ]
        if len(missing_cols) == 1:
            raise GroupsNotFoundError(f"Column {missing_cols[0]} is not included in the DataFrame.")
        else:
            missing_cols_fmt = ", ".join(missing_cols)
            raise GroupsNotFoundError(
                f"Columns {missing_cols_fmt} are not included in the DataFrame."
            )

    if count_name is None:
        count_name = "count_" + "_X_".join(group_cols)

    # Get any column name
    any_column = tbl.columns[0]
    tbl[count_name] = tbl.groupby(group_cols)[any_column].transform("count")

    return tbl
