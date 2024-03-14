#!/usr/bin/env python3
"""
module containing a function that takes a list mxd_lst of integers and
floats and returns their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ function that adds integers and floats and returns float """
    return sum(mxd_lst)
