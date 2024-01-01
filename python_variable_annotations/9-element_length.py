#!/usr/bin/env python3
"""script"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Annotate The fct given in the task"""
    return [(i, len(i)) for i in lst]
