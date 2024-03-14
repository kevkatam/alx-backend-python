#!/usr/bin/env python3
"""
module containing a function that  takes a list input_list of floats as
argument and returns their sum as a float.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ returns sum of floats in a list """
    return sum(input_list)
