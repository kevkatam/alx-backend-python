#!/usr/bin/env python3
"""
module containing a function that returns first element of a list if the list
is not empty, else returns none
"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ function that either returns 1st element of a list or none """
    if lst:
        return lst[0]
    else:
        return None
