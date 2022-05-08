"""Helper functions."""

from typing import List


def filter_list(x: List, mask: List, negate: bool = False) -> List:
    """Filter a list by a mask.

    Args:
        x: The list to be filtered by.
        mask: The mask to to be used for filtering.
        negate: Should values in the mask be flipped? Defaults to False.

    Raises:
        ValueError: If the length of the mask does not match.
        TypeError: If mask includes elements that are not boolean.

    Returns:
        A list of elements of x with value True at the corresponding mask index.
    """
    if len(x) != len(mask):
        raise ValueError("The length of the mask does not match.")

    is_boolean = [isinstance(mask_elem, bool) for mask_elem in mask]

    if not all(is_boolean):
        raise TypeError("The mask to be used for filtering can only include boolean values.")

    if negate:
        mask = [not mask_elem for mask_elem in mask]

    return [elem for (elem, mask_elem) in zip(x, mask) if mask_elem]
