#!/usr/bin/env python3
"""
module that contains a function that zooms in to array repeating items
according to factor
"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """ return list of integers multiplied by a factor """
    zoomed_in:  List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array: Tuple = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
