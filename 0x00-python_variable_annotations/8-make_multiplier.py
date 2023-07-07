#!/usr/bin/env python3
"""defines a function make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function tha multiplies a float by multiplier"""
    return (lambda x: float(x) * multiplier)
