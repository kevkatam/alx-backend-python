#!/usr/bin/env python3
"""
module containing a function that retrieve a value from a dictionary using
a given key
"""
from typing import Mapping, Any, Union, Any, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T,
                     None] = None) -> Union[Any, T]:
    if key in dct:
        return dct[key]
    else:
        return default
