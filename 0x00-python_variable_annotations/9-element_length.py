#!/usr/bin/env python3
"""annotetes a function parameters & return the value with appropriate types"""
from typing import Sequence, List, Iterable, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
