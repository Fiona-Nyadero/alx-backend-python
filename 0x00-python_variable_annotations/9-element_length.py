#!/usr/bin/env python3
'''Module return components'''
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Function returns a Iterable List'''
    return [(i, len(i)) for i in lst]
