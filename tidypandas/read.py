"""Read a subset of a csv file with pattern-based starting point."""

import re
from pathlib import Path
from typing import Union


def locate_pattern(file: Union[str, Path], pattern: str) -> int:
    """Locate the index at which the pattern is located.

    Args:
        file: Path to the file.
        pattern: Regex pattern to locate the starting point.

    Returns:
        Index of the starting point. In case of no match -1 is returned.
    """
    with open(file) as f:
        for index, line in enumerate(f):
            if re.search(pattern, line) is not None:
                return index

    return -1
