#!/usr/bin/env python3
"""defines a function sum_mixed_list"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """takes in a list of integers of int and float and returns the sum"""
    return float(sum(mxd_list))
