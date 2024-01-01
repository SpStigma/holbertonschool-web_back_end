#!/usr/bin/env python3
"""script"""


def sum_list(input_list: list[float]) -> float:
    """returns their sum as a float."""
    total = 0
    for number in input_list:
        total += number
    return total
