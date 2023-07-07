#!/usr/bin/env python3
"""defines a function to_kv"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """takes a string(k) and an int or float(v) and return a tuple"""
    return tuple([k, v ** 2])
