#!/usr/bin/env python3
"""script"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """The first element of the tuple is the string k.
    The second element is the square of the int/float v and should
    be annotated as a float."""
    return (k, v ** 2)
