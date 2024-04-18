#!/usr/bin/env python3
'''Module multiples numbers by a constant from a function'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Function returns a multiple function'''
    def multple(mult: float) -> float:
        '''Function multiples a multiplier by a mult variable'''
        return mult * multiplier

    return multple
