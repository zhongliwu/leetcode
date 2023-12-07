# -*- coding: utf-8 -*--

import pytest
from arrays import BinarySearch as Bs
from utils import compare_arr


class Test658FindKClosestElements:

    @pytest.fixture
    def solution(self):
        return Bs.BinarySearch()

    def test_right_boundary(self, solution):
        a = [1, 4, 6, 10, 20]
        result = solution.q658_find_k_closest_elements(a, 21, 4)
        expected = [20, 10, 6, 4]
        for i in range(0, len(expected)):
            assert result[i] == expected[i]

    def test_func(self, solution):
        a = [1, 4, 8, 12, 16, 28, 38]
        result = solution.q658_find_k_closest_elements(a, 12, 4)
        expected = [12, 8, 16, 4]
        assert compare_arr(result, expected) is True
