"""Construct a random pd.DataFrame with passed column names and specs."""

# import numpy as np
import random
from typing import Any

import pandas as pd


class ColumnSpecificationNotImplementedError(Exception):
    """A custom exception that is raised if a column spec is passed that isn't implemented."""


def random_dataframe(n_rows: int, **cols: Any) -> pd.DataFrame:
    """Random pd.DataFrame constructor.

    Args:
        n_rows: Number of rows.
        cols: A type specification for each column.

    Raises:
        ColumnSpecificationNotImplementedError: If some column specifications are not implemented.

    Returns:
        A random pd.DataFrame with specified number of rows and columns specs.
    """
    # Sets to sample from based on column specs
    str_sample = list(
        "\t\n\r\v\f"
        + "abcdefghijklmnopqrstuvwxyz"
        + "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        + "0123456789"
        + r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
    )

    # Check that all column specs are valid
    allowed_specs = [str]
    is_allowed_spec = [col_spec in allowed_specs for col_spec in cols.values()]
    if not all(is_allowed_spec):
        not_allowed_cols = [
            col_name for col_name, is_allowed in zip(cols.keys(), is_allowed_spec) if not is_allowed
        ]
        if len(not_allowed_cols) == 1:
            err_msg = f"Column {not_allowed_cols[0]} has an invalid column specification."
        else:
            if len(not_allowed_cols) == 2:
                err_msg_end = " have an invalid column specification."
                err_msg = f"Columns {' and '.join(not_allowed_cols)}" + err_msg_end
            else:
                err_msg = (
                    f"Columns {', '.join(not_allowed_cols[:-1])} and {not_allowed_cols[-1]}"
                    + err_msg_end
                )

        raise ColumnSpecificationNotImplementedError(
            err_msg + " Check the available specifications in the documentation."
        )

    cols_dict = {}

    for col_name, col_spec in cols.items():
        if col_spec is str:
            col_sample = str_sample.copy()
        col_values = []
        for _ in range(n_rows):
            # Shuffle the col_sample
            random.shuffle(col_sample)
            col_values.append("".join(col_sample[: random.randint(1, 10)]))
        cols_dict[col_name] = col_values

    return pd.DataFrame(cols_dict)
