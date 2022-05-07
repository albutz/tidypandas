"""Read a subset of a delimited file with pattern-based starting point."""

import re
from pathlib import Path
from typing import List, TextIO, Union


def locate_pattern(file: Union[str, Path], pattern: str) -> int:
    """Locate the index at which the pattern is located.

    Args:
        file: Path to the file.
        pattern: Regex pattern to locate the starting point.

    Returns:
        Index of the starting point. In case of no match -1 is returned.
    """

    def get_index(lines: Union[List, TextIO]) -> int:
        for index, line in enumerate(lines):
            if re.search(pattern, line) is not None:
                return index

        return -1

    # Case when file is a raw string
    if isinstance(file, str) and len(file) > 1:
        return get_index(file.splitlines())

    # Case when file is a path
    with open(file) as f:
        return get_index(f)
