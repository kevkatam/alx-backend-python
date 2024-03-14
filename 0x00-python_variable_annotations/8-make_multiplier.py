#!/usr/bin/env python3
"""
module that contains a function that takes a float multiplier as argument
and returns a function that multiplies a float by multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ function that returns a function that multiplies a float by
        multiplier"""
    def multiplier_func(num: float) -> float:
        """ function that multiplies a float with multiplier """
        return num * multiplier
    return multiplier_func
