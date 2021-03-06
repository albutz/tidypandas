"""Helper functions for grouping operations."""

from typing import List

import pandas as pd
import pandas_flavor as pf
from utils import filter_list


class GroupsNotFoundError(Exception):
    """A custom exception that is raised if the groups provided to add_count are not found."""


@pf.register_dataframe_method
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
    df_aug = df.copy()

    # Check if all groups are included and raise a GroupsNotFoundError if not
    is_group_included = [group in df_aug.columns for group in group_cols]
    if not all(is_group_included):
        missing_cols = filter_list(group_cols, is_group_included, negate=True)

        # Pluralize error message if necessary
        if len(missing_cols) == 1:
            raise GroupsNotFoundError(f"Column {missing_cols[0]} is not included.")
        else:
            if len(missing_cols) == 2:
                missing_cols_fmt = " and ".join(missing_cols)
            else:
                missing_cols_fmt = ", ".join(missing_cols[:-1]) + " and " + missing_cols[-1]
            raise GroupsNotFoundError(f"Columns {missing_cols_fmt} are not included.")

    # Set name of new column if not specified
    if count_name is None:
        sep = "_" if len(group_cols) > 1 else ""
        count_name = "count_" + sep.join(group_cols)

    # Get any column name
    any_column = df_aug.columns[0]
    df_aug[count_name] = df_aug.groupby(group_cols)[any_column].transform("count")

    return df_aug
