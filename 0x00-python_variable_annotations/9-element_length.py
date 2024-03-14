#!/usr/bin/env python3
"""
module that contains a function that returns a list of tuples each
containing an element and it's length
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ returns a list of tuples """
    return [(i, len(i)) for i in lst]
