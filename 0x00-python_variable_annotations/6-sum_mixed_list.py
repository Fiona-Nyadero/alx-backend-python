#!/usr/bin/env python3
'''Module sums up floats and integers components of a list'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''Function returns a sum of floats/Integers in a list'''
    summation = sum(mxd_lst)

    return float(summation)
