"""Read a subset of a delimited file with pattern-based starting point."""

import re
from pathlib import Path
from typing import Any, List, TextIO, Union

import pandas as pd


class PatternNotFoundError(Exception):
    """An exception raised when the pattern for subsetting is not found."""


def locate_pattern(file: Union[str, Path], pattern: str) -> int:
    """Locate the index at which the pattern is located.

    Args:
        file: Path to the file.
        pattern: Regex to locate the starting point.

    Returns:
        Index of the starting point. In case of no match -1 is returned.
    """

    def get_index(lines: Union[List, TextIO]) -> int:
        for index, line in enumerate(lines):
            if re.search(pattern, line) is not None:
                return index

        return -1

    # Case when file is a raw string
    if isinstance(file, str) and file.count("\n") > 0:
        return get_index(file.splitlines())

    # Case when file is a path
    with open(file) as f:
        return get_index(f)


def read_sub(file: Union[str, Path], pattern: Union[str, None], **kwargs: Any) -> pd.DataFrame:
    """Pattern-based subsetting and reading.

    Identify the pattern-based starting point to read in a delimited file and pass the relevant
    lines to pandas read_csv function.

    Args:
        file: Path to the file.
        pattern: Regex to locate the starting point.
        kwargs: Additional parameters passed to pandas read_csv function.

    Raises:
        PatternNotFoundError: If a pattern is passed but cannot be located.

    Returns:
        A pandas DataFrame.
    """
    starting_point = locate_pattern(file, pattern) if pattern is not None else 0

    if starting_point == -1:
        raise PatternNotFoundError("Pattern could not be found.")

    return pd.read_csv(file, skiprows=starting_point, **kwargs)
