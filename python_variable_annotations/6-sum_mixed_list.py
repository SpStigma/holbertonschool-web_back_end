#!/usr/bin/env python3
"""script"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """return a float on a mixed list"""
    total = 0
    for number in mxd_lst:
        total += number
    return total
