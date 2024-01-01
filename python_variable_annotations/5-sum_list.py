#!/usr/bin/env python3
"""script"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """returns their sum as a float."""
    total = 0
    for number in input_list:
        total += number
    return total
