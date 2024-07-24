#!/usr/bin/env python3
""" Simple helper function module """

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Returns a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.
    Args:
        page (int): the page number (1-indexed)
        page_size (int): the number of items per page
        Returns:
        Tuple[int, int]: a tuple containing the start index and end index
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
