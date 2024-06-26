#!/usr/bin/env python3
'''Module creates a parameterized unittest'''

import unittest
from parameterized import parameterized
from typing import Any, Dict, Tuple
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    '''Unittests for the utils.access_nested_map Fx'''
    @parameterized.expand([
        ({"a": 1}, ("a",)),
        ({"a": {"b": 2}}, ("a",)),
        ({"a": {"b": 2}}, ("a", "b")),
    ])
    def test_access_nested_map(self, nested_map: Dict[str, Any],
                               path: Tuple[str, ...], expected: Any) -> None:
        '''Tests whether the method returns the correct value'''
        answer = access_nested_map(nested_map, path)
        self.AssertEqual(answer, expected)


if __name__ = '__main__':
    import unittest
    from typing import cast

    unittest.main()
