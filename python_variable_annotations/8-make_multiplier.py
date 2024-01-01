#!/usr/bin/env python3
"""Create a higher-order function that generates a multiplier function."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Create a higher-order function that generates a multiplier function."""
    def operation(x: float) -> float:
        """Multiply the given input by the multiplier."""
        return multiplier * x
    return operation
