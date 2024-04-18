#!/usr/bin/env python3
'''Modules tuples out oa string, float or int variables'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''Returns a tuple (string and square of an int/float)'''
    return (k, v ** 2)
